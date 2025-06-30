from fastapi import APIRouter, Depends
from ml_pipeline.predictor import predict
from api.auth import verify_token

router = APIRouter()

@router.post("/")
def predict_endpoint(data: dict, user=Depends(verify_token)):
    return predict(data)
