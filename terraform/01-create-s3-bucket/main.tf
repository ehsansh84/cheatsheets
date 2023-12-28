resource "aws_s3_bucket" "example" {
  bucket = "social-dash"

  tags = {
    Name        = "Social dashboard"
    Environment = "Dev"
  }
}