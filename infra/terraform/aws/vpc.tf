provider "aws" {
  region = "ap-south-1"
}

resource "aws_vpc" "enterprise_rag_vpc" {

  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "enterprise-rag-vpc"
  }
}