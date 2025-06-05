from fastapi import APIRouter, HTTPException, Depends, UploadFile, File

from app.model.schemas import PredictionResponse, PredictionResultItem
from app.services.classify_service import get_classify_service
from app.util.logger import show_log

router = APIRouter()


@router.post("/classify", response_model=PredictionResponse)
async def classify(
        input_data: UploadFile = File(...),
        classify_service: get_classify_service = Depends()
):
    if not input_data.content_type.startswith("image/"):
        raise HTTPException(
            status_code=400,
            detail="File provided is not image."
        )

    try:
        input_image = await input_data.read()
        result = await classify_service.classify(input_image)

        predict_list = []

        for i, res in enumerate(result):
            predict_list.append(
                PredictionResultItem(
                    label = i,
                    confidence = res,
                )
            )

        return PredictionResponse(
            predict_results=predict_list,
        )
    except Exception as e:
        show_log(__name__).error(e)

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
