import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


df = pd.read_csv("../data/housingdataset.csv")


df.drop("Id", axis=1, inplace=True)

# feature engineering to create a new feature called "HouseAge" by subtracting the "YearBuilt" from the current year (2026)
current_year = 2026
df["HouseAge"] = current_year - df["YearBuilt"]
df.drop("YearBuilt", axis=1, inplace=True)

# map the "Garage" column to binary values (1 for "Yes" and 0 for "No")
df["Garage"] = df["Garage"].map({"Yes": 1, "No": 0})
