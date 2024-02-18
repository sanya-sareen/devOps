#!/bin/bash

# Create a sample file
echo "This is a sample file created by the upload-to-s3.sh script." > sample_file.txt

# Upload the file to S3 bucket
aws s3 cp sample_file.txt s3://uploading-shell-script/sample_file.txt

# Send notification to SQS queue
aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/582285444681/shell-script-updates --message-body "File uploaded to S3: sample_file.txt"
