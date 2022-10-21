import boto3
import json
import os
from botocore.exceptions import ClientError
import logging

directory='/home/gopay/s3data'
url='https://source.golabs.io'

s3 = boto3.resource('s3')
client = boto3.client('s3')

# Delete Content of the Bucket (optional you can remove from the application)
try:
    my_bucket = s3.Bucket('s3appdvversion2')
    my_bucket.objects.all().delete()
    print("All Bucket Objects deleted succesfully")
except ClientError as e:
    print(logging.error(e))

# delete the bucket after removing all objects in the bucket (Optional)
try:
    response = client.delete_bucket(
    Bucket='s3appdvversion2')
    print("Bucket Deleted Successfully")
    print(json.dumps(response, indent=2))
except ClientError as e:
    print(logging.error(e))


# Create a new bucket (Optional)
response = client.create_bucket(
    ACL='public-read-write',
    Bucket='s3appdvversion2',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-southeast-1',
    },
)

print(json.dumps(response, indent=2))

# Upload File to our Bucket
for file in os.listdir(directory):
    client.upload_file(directory+'\\'+file, 's3appdvversion2',file)

#List content of the Bucket
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
