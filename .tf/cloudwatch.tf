resource "aws_cloudwatch_event_rule" "realtor_scraper_lambda_rule" {
  description         = "Invoke realtor scraper lambda once a week."
  event_bus_name      = "default"
  is_enabled          = "false"
  name                = "realtor-scraper-lambda-rule"
  schedule_expression = "rate(7 days)"
}

resource "aws_cloudwatch_event_target" "realtor-scraper-lambda--rule-002F-Id193058953225" {
  arn       = aws_lambda_function.realtor_scraper.arn
  rule      = aws_cloudwatch_event_rule.realtor_scraper_lambda_rule.name
  target_id = aws_lambda_function.realtor_scraper.name
}
