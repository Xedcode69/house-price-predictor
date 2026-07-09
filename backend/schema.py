"""
Pydantic model for incoming house price prediction requests.

Define the model differently depending on the installed Pydantic major
version so FastAPI validation accepts either the dataset aliases (e.g.
`MedInc`) or developer-friendly field names (e.g. `median_income`).
"""

from typing import Any

import pydantic as _pydantic
from pydantic import BaseModel, Field


def _pydantic_major() -> int:
    try:
        return int(_pydantic.__version__.split(".")[0])
    except Exception:
        return 1


if _pydantic_major() >= 2:

    class HousePriceInput(BaseModel):
        median_income: float = Field(..., alias="MedInc")
        house_age: float = Field(..., alias="HouseAge")
        average_rooms: float = Field(..., alias="AveRooms")
        average_bedrooms: float = Field(..., alias="AveBedrms")
        population: float = Field(..., alias="Population")
        average_occupancy: float = Field(..., alias="AveOccup")
        latitude: float = Field(..., alias="Latitude")
        longitude: float = Field(..., alias="Longitude")

        model_config = {"populate_by_name": True}  # pydantic v2

else:

    class HousePriceInput(BaseModel):
        median_income: float = Field(..., alias="MedInc")
        house_age: float = Field(..., alias="HouseAge")
        average_rooms: float = Field(..., alias="AveRooms")
        average_bedrooms: float = Field(..., alias="AveBedrms")
        population: float = Field(..., alias="Population")
        average_occupancy: float = Field(..., alias="AveOccup")
        latitude: float = Field(..., alias="Latitude")
        longitude: float = Field(..., alias="Longitude")

        class Config:  # pydantic v1
            allow_population_by_field_name = True

    HousePriceInput.Config = _Config
