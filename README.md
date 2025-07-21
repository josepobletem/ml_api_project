# 🧠 ML API Project

API desarrollada con FastAPI para servir modelos de Machine Learning (XGBoost) y un chatbot basado en OpenAI. Incluye autenticación JWT y  y una arquitectura de despliegue profesional en GCP usando Terraform, Docker y CI/CD con GitHub Actions. Con pruebas automatizadas con `pytest`.

---

## 📦 Características

- Endpoint `/predict/` que responde con predicciones usando un modelo entrenado (`model.joblib`)
- Endpoint `/chatbot/` que responde preguntas utilizando la API de OpenAI
- Autenticación JWT vía `/token`
- Pruebas unitarias con `pytest`
- Mock de dependencias como OpenAI y el modelo en testing
- Preparado para uso local o despliegue con Docker/Terraform

---

## ✅ Pre-requisitos

- Python 3.10 o 3.11 (❌ Python 3.13 puede causar errores con `numpy`, `scikit-learn`, etc.)
- Git
- OpenAI API Key (para funcionalidad completa del chatbot)
- (Opcional) Docker
- (Opcional) Cuenta GCP si quieres usar backend remoto con Terraform

---

## 🚀 Instalación y ejecución local

```bash
git clone https://github.com/josepobletem/ml_api_project.git
cd ml_api_project

# Crear entorno virtual
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Instalar dependencias
pip install --no-build-isolation -r requirements.txt

# Ejecutar la API
uvicorn api.main:app --reload
```

🔐 Autenticación

Solicita un token:

```bash
curl -X POST http://localhost:8000/token
```
Respuesta:
```bash
{
  "access_token": "<jwt_token>",
  "token_type": "bearer"
}
```

Usa este token para acceder a /predict/ y /chatbot/ con el header:

```bash
Authorization: Bearer <jwt_token>
```

📡 Endpoints
| Método | Ruta        | Descripción                           |
| ------ | ----------- | ------------------------------------- |
| POST   | `/token`    | Devuelve JWT de autenticación         |
| POST   | `/predict/` | Predicción ML con XGBoost             |
| POST   | `/chatbot/` | Chatbot que usa OpenAI para responder |


---

## 📦 Estructura del Proyecto

```
ml_api_project/
├── .github/
│   └── workflows/
│       ├── ci_dev.yml
│       ├── ci_stg.yml
│       └── ci_prod.yml
├── api/
│   ├── main.py
│   ├── auth.py
│   ├── dependencies.py
│   ├── endpoints/
│   │   ├── predict.py
│   │   └── chatbot.py
│   ├── chatbot/
│   │   ├── prompts.py
│   │   └── feedback.py
├── ml_pipeline/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── trainer.py
│   ├── predictor.py
│   ├── metrics.py
│   └── model_registry.py
├── tests/
│   ├── test_auth.py
│   ├── test_predict.py
│   ├── test_chatbot.py
│   ├── test_trainer.py
│   ├── test_data_loader.py
│   ├── test_preprocessor.py
│   ├── test_metrics.py
│   ├── test_model_registry.py
│   └── conftest.py
├── terraform/
│   ├── env/
│   │   ├── dev/backend.tf
│   │   ├── stg/backend.tf
│   │   └── prod/backend.tf
│   └── modules/
│       └── app_infra/
│           ├── main.tf
│           ├── outputs.tf
│           └── variables.tf
├── Dockerfile
├── docker-compose.yml
├── Makefile
├── requirements.txt
└── README.md
```

---

## 🧠 Pipeline de ML

1. `data_loader.py` - Carga de datos desde CSV o DB
2. `preprocessor.py` - Preprocesamiento (escalado, OHE, etc.)
3. `trainer.py` - Entrenamiento con XGBoost
4. `predictor.py` - Inferencia
5. `metrics.py` - Métricas de evaluación
6. `model_registry.py` - Guardado/carga de modelo

---

## 🔐 Seguridad

- Autenticación vía JWT (Bearer Token)
- Endpoints protegidos con `Depends(verify_token)`

---

## ⚙️ CI/CD

- GitHub Actions para `dev`, `stg`, `prod`
- Terraform para desplegar en GCP (Cloud Run + Cloud SQL)
- Lint, test y despliegue automatizado

---

## 🧪 Tests

```bash
make test         # Ejecuta tests unitarios
make test-cov     # Ejecuta tests con cobertura
```

---

## 🐳 Docker

```bash
make docker-build   # Construye la imagen
make docker-run     # Corre API y DB en local
make docker-stop    # Detiene los servicios
```

---


---


## 📄 Licencia

MIT - Libre uso y modificación.

---

## 🛠️ Cómo usar la API

### 1. Obtener un token JWT

```bash
curl http://localhost:8000/token
```

La respuesta será un token tipo:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI...",
  "token_type": "bearer"
}
```

### 2. Realizar una predicción

```bash
curl -X POST http://localhost:8000/predict/ \
  -H "Authorization: Bearer <tu_token>" \
  -H "Content-Type: application/json" \
  -d '{"feature1": 1, "feature2": 2}'
```

### 3. Consultar al chatbot

```bash
curl -X POST http://localhost:8000/chatbot/?question=¿Qué+es+IA \
  -H "Authorization: Bearer <tu_token>"
```

---

## ☁️ Despliegue en Google Cloud con Terraform

### 1. Crear bucket de estado remoto

```bash
gsutil mb -l us-central1 gs://terraform-state-ml-api
```

### 2. Configurar backend en cada entorno

Ya incluido en `terraform/env/dev/backend.tf`, `stg`, y `prod`.

### 3. Inicializar e instalar infraestructura

```bash
cd terraform/env/dev
terraform init
terraform plan
terraform apply -auto-approve
```

### 4. Variables necesarias (`terraform.tfvars`)

```hcl
project_id    = "tu-proyecto-gcp"
region        = "us-central1"
docker_image  = "gcr.io/tu-proyecto/ml-api:latest"
db_password   = "clave-supersecreta"
```

Puedes duplicar el flujo para `stg` y `prod`, cambiando `prefix` y `docker_image` según corresponda.

---
---
---

## ✅ GitHub Actions para Terraform (validación de todos los entornos)

Este proyecto incluye un único workflow combinado para validar los planes de Terraform en los tres entornos (`dev`, `stg`, `prod`) sin necesidad de una cuenta GCP activa.

📄 Archivo:
```
.github/workflows/terraform_plan_all_envs.yml
```

🔁 Se activa al hacer un `pull_request` o `workflow_dispatch` y automáticamente:

- Detecta si estás en la rama `dev`, `stg` o `main`
- Ejecuta:
  - `terraform init -backend=false`
  - `terraform validate`
  - `terraform plan` con variables dummy

Esto permite validar la infraestructura como código en CI de forma segura, sin aplicar cambios y sin acceso a GCP.
---

🤝 Contribuciones

¡Contribuciones son bienvenidas!

- 1.-Haz un fork del repositorio.
- 2.-Crea una rama (feature/nueva-funcionalidad).
- 3.-Abre un Pull Request.


## 👨‍💻 Créditos

Proyecto desarrollado por **José Poblete M.**

> Esta estructura ha sido diseñada con dedicación para servir como base robusta y flexible para cualquier Data Scientist, Ingeniero de Datos o profesional del aprendizaje automático que busque desplegar sus modelos de forma profesional.  
>
> Que este proyecto te sirva como trampolín para lanzar tus ideas, compartir tu talento y construir soluciones que generen impacto.  
>
> ¡Adáptalo, mejóralo y hazlo tuyo! 🚀
