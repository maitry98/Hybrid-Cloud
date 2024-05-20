import boto3

s3Client = boto3.client('s3',
					aws_secret_access_key="nBnsFemGh6BHDQzgekz1N3iqLZzAEQLEaM4vOLpf",
					aws_access_key_id="DC9YC0T3XBBVJLC0SIOA",
					endpoint_url="http://192.168.0.47:6969")


response = s3Client.list_objects_v2(Bucket="cloudspades-input-bucket")
print(response)
for item in response['Contents']:
	print(item['Key'])
