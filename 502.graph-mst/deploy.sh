# !/bin/bash
aws lambda create-function \
--function-name 502 \
--runtime python3.10 \
--handler function.handler \
--role arn:aws:iam::814724636602:role/sizeFunction \
--timeout 120 \
--memory-size 512 \
--zip-file fileb://502.zip
