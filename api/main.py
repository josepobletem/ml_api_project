from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.endpoints import predict, chatbot
from api.auth import router as auth_router

app = FastAPI(
    title="ML API with ChatGPT",
    description="API REST para predicción ML con XGBoost e integración con ChatGPT",
    version="1.0.0"
)

# Configuración de CORS (opcional)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambiar en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth_router, tags=["Auth"])
app.include_router(predict.router, prefix="/predict", tags=["Predictions"])
app.include_router(chatbot.router, prefix="/chatbot", tags=["Chatbot"])

# Eventos opcionales
@app.on_event("startup")
async def startup_event():
    print("🚀 API iniciada.")

@app.on_event("shutdown")
async def shutdown_event():
    print("🛑 API detenida.")
