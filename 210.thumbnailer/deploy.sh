# !/bin/bash
aws lambda create-function \
--function-name 210 \
--runtime python3.10 \
--handler function.handler \
--role arn:aws:iam::814724636602:role/sizeFunction \
--timeout 60 \
--memory-size 256 \
--zip-file fileb://210.zip
