import numpy as np
import joblib

from sklearn.datasets import fetch_california_housing

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

dataset = fetch_california_housing(as_frame=True)

df = dataset.frame

x = df.drop("MedHouseVal", axis=1)
y = df["MedHouseVal"]

# feature engineering to create a new feature called "HouseAge" by subtracting the "YearBuilt" from the current year (2026)
# current_year = 2026
# df["HouseAge"] = current_year - df["YearBuilt"]
# df.drop("YearBuilt", axis=1, inplace=True)

# map the "Garage" column to binary values (1 for "Yes" and 0 for "No")
# df["Garage"] = df["Garage"].map({"Yes": 1, "No": 0})

# create features and target
# x = df.drop("Price", axis=1)
# y = df["Price"]

# seperate the numeric and categorical features
numeric_features = x.select_dtypes(include=["int64", "float64"]).columns.tolist()
# categorical_features = x.select_dtypes(include=["str"]).columns.tolist()

# create numric pipeline to scale the numeric features using StandardScaler
numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

# # create categorical pipeline to one-hot encode the categorical features using OneHotEncoder
# categorical_transformer = Pipeline(
#     steps=[("onehot", OneHotEncoder(handle_unknown="ignore"))]
# )

# combine the numeric and categorical transformers into a single preprocessor
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        # ("cat", categorical_transformer, categorical_features),
    ]
)

# create model pipeline to combine the preprocessor and the RandomForestRegressor model
model_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("regressor", RandomForestRegressor(n_estimators=100, random_state=42)),
    ]
)

# split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# fit the model pipeline to the training data
model_pipeline.fit(x_train, y_train)

# make predictions on the test data
prediction = model_pipeline.predict(x_test)

rmse = np.sqrt(mean_squared_error(y_test, prediction))
r2 = r2_score(y_test, prediction)
mae = mean_absolute_error(y_test, prediction)

print("Mean Squared Error:", rmse)
print("R-squared:", r2)
print("Mean Absolute Error:", mae)

joblib.dump(model_pipeline, "model.pkl")
