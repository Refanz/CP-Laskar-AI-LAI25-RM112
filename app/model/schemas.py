from pydantic import BaseModel
from typing import List, Any


class PredictionRequest(BaseModel):
    input_data: List[float]

    class Config:
        json_schema_extra = {
            "example": {
                "input_data": [1.2, 3.4, 5.6, 7.8]
            }
        }


class PredictionResultItem(BaseModel):
    label: str|int
    confidence: float

    class Config:
        json_schema_extra = {
            "example": {
                "label": "healthy",
                "confidence": 0.85
            }
        }


class PredictionResponse(BaseModel):
    predict_results: List[PredictionResultItem]

    class Config:
        json_schema_extra = {
            "example": {
                "results": [
                    {"label": "healthy", "confidence": 0.96},
                    {"label": "disease_A", "confidence": 0.03},
                    {"label": "disease_B", "confidence": 0.01}
                ]
            }
        }
