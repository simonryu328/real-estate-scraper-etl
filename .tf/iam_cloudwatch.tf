resource "aws_lambda_permission" "allow_excution_from_cloudwatch" {
  statement_id = "AllowExecutionFromCloudWatch"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.realtor_scraper.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.realtor_scraper_lambda_rule.arn
}