resource "aws_s3_bucket" "documents" {

  bucket = "enterprise-rag-documents"

  tags = {
    Environment = "production"
  }
}