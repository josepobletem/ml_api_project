terraform {
  backend "gcs" {
    bucket = "terraform-state-ml-api"
    prefix = "env/dev"
  }
}
