from preprocessing.cleaning_data import preprocess
from predict.prediction import predict
from fastapi import FastAPI, Body, Query
from typing import Optional
from pydantic import BaseModel, Field
import os

tags_metadata = [
    {
        "name": "Status",
        "description": "Check server status.",
    },
    {
        "name": "Predict",
        "description": "Make house price prediction",
    },
]

class Data(BaseModel):

    area: int
    property_type: str = Query("APARTMENT", alias="property-type")
    rooms_number: int = Field(alias="rooms-number")
    zip_code: int = Field(alias="zip-code")
    land_area: Optional[int] = Field(alias="land-area")
    garden: Optional[bool] 
    garden_area: Optional[int] = Field(alias="garden-area")
    equipped_kitchen: Optional[bool] = Field(alias="equipped-kitchen")
    full_address: Optional[str] = Field(alias="full-address")
    swimming_pool: Optional[bool] = Field(alias="swimming-pool")
    furnished: Optional[bool]
    open_fire: Optional[bool] = Field(alias="open-fire")
    terrace: Optional[bool]
    terrace_area: Optional[int] = Field(alias="terrace-area")
    facades_number: Optional[int] = Field(alias="facades-number")
    building_state: Optional[str] = Query("NEW", alias="building_state")
 
    class Config:
        allow_population_by_field_name = True

class response(BaseModel):
    prediction: Optional[float]
    error: Optional[float]


app = FastAPI(title="ImmoEliza API", docs_url="/predict")

@app.get("/", tags=["Status"])
async def status():
    return "alive"

@app.post("/predict/", response_model=response, tags=["Predict"])
async def prediction(data:Data = Body(None, embed=True)):
    request_data = data.dict()
    preprocessed_data = preprocess(request_data)
    prediction, error = predict(preprocessed_data)
    return {"prediction": prediction, "error": error}
    
