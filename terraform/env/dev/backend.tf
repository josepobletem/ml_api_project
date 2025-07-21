terraform {
  backend "local" {
    bucket = "terraform-state-ml-api"
    prefix = "env/dev"
  }
}
