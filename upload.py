# Edit the file '.env' and provide the required parameters
# Install the required libraries in the environment by executing: 'pip install -r env.req'

# Importing the required libraries
from dotenv import load_dotenv
import boto3
import os
import datetime

load_dotenv()  # This line brings all environment variables from '.env' into 'os.environ'

# Set up AWS credentials
aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
region_name = os.environ['REGION_NAME']

# Set up S3 client
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Set up the source and destination S3 bucket names
destination_bucket_name = os.environ['DESTINATION_BUCKET_NAME']

# Define the name of the directory where the downloaded files will be stored
input_directory = os.environ['INPUT_DIRECTORY']

# Recursively upload files to S3
for root, dirs, files in os.walk(input_directory):
    for file in files:
        #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print(timestamp, ': Uploading ' + file)
        local_path = os.path.join(root, file)
        s3_path = os.path.relpath(local_path, input_directory)
        print(s3_path)
        #s3.upload_file(local_path, destination_bucket_name, s3_path)
        #timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        #print(timestamp, ':', file, 'transferred')
