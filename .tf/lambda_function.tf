resource "aws_lambda_function" "realtor_scraper" {
  description                    = "scrape realtor.com and upload csv to s3"
  function_name                  = "realtor_scraper"
  handler                        = "realtor_scrape.lambda_handler"
  memory_size                    = "128"
  package_type                   = "Zip"
  role                           = "${aws_iam_role.lambda_execution_role.arn}"
  runtime                        = "python3.6"
  timeout                        = "900"
}
