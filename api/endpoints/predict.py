from fastapi import APIRouter, Depends

from api.auth import verify_token
from ml_pipeline.predictor import predict

router = APIRouter()


@router.post("/")
def predict_endpoint(data: dict, user=Depends(verify_token)):
    return predict(data)
