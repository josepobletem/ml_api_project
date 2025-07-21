from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

# Configuración básica de seguridad
SECRET_KEY = "secret"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_token(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Verifica la validez de un token JWT.
    Devuelve el contenido del payload si es válido.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=403, detail="Token inválido o expirado")


# Ejemplo de dependencia para inyectar configuración global
def get_model_path() -> str:
    """
    Retorna la ruta al modelo entrenado.
    Puedes expandir esto con rutas dinámicas por ambiente.
    """
    return "model.joblib"


# Ejemplo de conexión a base de datos o recurso compartido
def get_db_conn():
    """
    Devuelve una conexión o recurso de base de datos si fuera necesario.
    (en este ejemplo, None como placeholder)
    """
    return None
