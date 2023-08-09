#!/bin/bash

start_time1=$(date +%s.%3N)  # Record the start time with millisecond precision

aws lambda invoke --function-name arn:aws:lambda:us-east-1:814724636602:function:503 --payload file://event.json --cli-binary-format raw-in-base64-out response.json

end_time1=$(date +%s.%3N)    # Record the end time with millisecond precision

execution_time1=$(echo "$end_time1 - $start_time1" | bc -l)  # Calculate the execution time in seconds

execution_time_ms1=$(echo "$execution_time1 * 1000" | bc -l)  # Convert to milliseconds
start_time2=$(date +%s.%3N)  # Record the start time with millisecond precision

aws lambda invoke --function-name arn:aws:lambda:us-east-1:814724636602:function:503 --payload file://event.json --cli-binary-format raw-in-base64-out response.json

end_time2=$(date +%s.%3N)    # Record the end time with millisecond precision

execution_time2=$(echo "$end_time2 - $start_time2" | bc -l)  # Calculate the execution time in seconds

execution_time_ms2=$(echo "$execution_time2 * 1000"| bc -l)  # Convert to milliseconds


cold=$(echo "$execution_time_ms1 - $execution_time_ms2"| bc -l)
echo "Cold start time is: $cold milliseconds"
