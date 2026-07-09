import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schema import HousePriceInput

app = FastAPI()

# Allow CORS for local development (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("model.pkl")


@app.get("/")
def read_root():
    return {"message": "Welcome to the House Price Prediction API"}


@app.post("/predict")
def predict_price(house_data: HousePriceInput):
    # Dump using aliases so keys match the training dataset column names.
    # Support both pydantic v2 (`model_dump`) and v1 (`dict`).

    input_dict = house_data.model_dump(by_alias=True)

    input_df = pd.DataFrame([input_dict])

    prediction = model.predict(input_df)

    return {"predicted_price": f"{float(prediction[0]):.2f}"}
