from fastapi import APIRouter, Depends

from api.auth import verify_token
from api.chatbot.feedback import save_feedback
from api.chatbot.prompts import generate_response

router = APIRouter()


@router.post("/")
def chat_with_bot(question: str, user=Depends(verify_token)):
    response = generate_response(question)
    save_feedback(question, response)
    return {"response": response}
