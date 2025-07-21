terraform {
  backend "local" {
    #bucket = "terraform-state-ml-api"
    #prefix = "env/prod"
    path = "terraform.tfstate"
  }
}
