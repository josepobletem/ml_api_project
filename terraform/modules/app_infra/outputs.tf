output "cloud_run_url" {
  description = "URL pública de la API desplegada en Cloud Run"
  value       = google_cloud_run_service.default.status[0].url
}

output "cloud_sql_instance_connection_name" {
  description = "Nombre de conexión a la instancia de Cloud SQL"
  value       = google_sql_database_instance.default.connection_name
}

output "database_user" {
  description = "Usuario de la base de datos"
  value       = google_sql_user.default.name
  sensitive   = true
}

output "database_password" {
  description = "Contraseña del usuario de la base de datos"
  value       = google_sql_user.default.password
  sensitive   = true
}

output "database_name" {
  description = "Nombre de la base de datos creada"
  value       = google_sql_database.default.name
}
