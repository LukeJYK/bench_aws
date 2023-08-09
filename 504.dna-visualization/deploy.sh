# !/bin/bash
aws lambda create-function \
--function-name 504 \
--runtime python3.10 \
--handler function.handler \
--role arn:aws:iam::814724636602:role/sizeFunction \
--timeout 60 \
--memory-size 2048 \
--code S3Bucket=504code,S3Key=504.zip
