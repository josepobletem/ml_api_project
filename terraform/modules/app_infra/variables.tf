variable "project_id" {
  description = "ID del proyecto de GCP"
  type        = string
}

variable "region" {
  description = "Región de GCP donde se desplegará la infraestructura"
  type        = string
  default     = "us-central1"
}

variable "cloud_run_service_name" {
  description = "Nombre del servicio de Cloud Run"
  type        = string
  default     = "ml-api"
}

variable "docker_image" {
  description = "Imagen de contenedor que se desplegará en Cloud Run"
  type        = string
}

variable "db_instance_name" {
  description = "Nombre de la instancia de Cloud SQL"
  type        = string
  default     = "ml-api-db"
}

variable "db_name" {
  description = "Nombre de la base de datos"
  type        = string
  default     = "ml_project"
}

variable "db_user" {
  description = "Usuario de la base de datos"
  type        = string
  default     = "user"
}

variable "db_password" {
  description = "Contraseña del usuario de la base de datos"
  type        = string
  sensitive   = true
}
