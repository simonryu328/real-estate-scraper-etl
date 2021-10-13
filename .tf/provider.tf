provider "aws" {
  region = var.region
  access_key = var.TF_VAR_ACCESS_KEY
  secret_key = var.TF_VAR_SECRET_KEY
}

terraform {
	required_providers {
		aws = {
	    version = "~> 3.57.0"
		}
  }
}
