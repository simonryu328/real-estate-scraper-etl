resource "aws_s3_bucket" "realtor-data" {
  arn            = "arn:aws:s3:::realtor-data"
  bucket         = "realtor-data"
  request_payer  = "BucketOwner"

  versioning {
    enabled    = "false"
    mfa_delete = "false"
  }
}