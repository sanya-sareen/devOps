#!/bin/bash

# Create a sample file
echo "This is a sample file created by the upload_to_s3.sh script." > sample_file.txt

# Upload the file to S3 bucket
aws s3 cp sample_file.txt s3://uploading-shell-script/sample_file.txt

# Send notification to SQS queue
aws sqs send-message --queue-url https://sqs.region.amazonaws.com/123456789012/shell-script-updates --message-body "File uploaded to S3: sample_file.txt"
