# !/bin/bash
aws lambda create-function \
--function-name 110 \
--runtime python3.10 \
--handler function.handler \
--role arn:aws:iam::814724636602:role/sizeFunction \
--timeout 10 \
--memory-size 128 \
--zip-file fileb://110.zip
