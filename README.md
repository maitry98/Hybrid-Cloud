# Project-Hybrid Cloud
This project involves the integration of AWS services, OpenFaaS, Ceph, and other tools to perform cloud-based video processing and data analysis. The primary goal is to develop a system that can handle automated video analysis tasks, such as face recognition, using serverless functions and distributed storage.

![hybridcloud image](https://github.com/maitry98/Hybrid-Cloud/assets/147111812/d39a976c-3522-43fe-b2df-e70a3d8c1e1c)
## Project Components
Dockerfile:
A multi-stage build for an OpenFaaS function with Python runtime. The final runtime image includes the required dependencies, such as ffmpeg, and copies the function code, dependencies, and handler script. The CMD instruction specifies the default command to execute when the container starts, pointing to the handler function for the OpenFaaS function.

handler.py:
This Python script serves as a crucial component in a system designed for video processing and face recognition. The code is intended to be deployed as an OpenFaas handler function. It processes video files that are uploaded to the CEPH input bucket

check.py:
This script checks the correctness of the video processing workflow. It verifies the results obtained from the face recognition function by comparing them with predefined mappings. The mappings are specified in the mapping file.

face-recognition.yml: Defines the OpenFaaS function for face recognition. It specifies the Docker image and dependencies required for the serverless function.

student_data.json:
A JSON file containing sample student data. This data is used for populating a DynamoDB table in the upload_data.py script.

upload_data.py:
This script uploads student data to a DynamoDB table. It reads data from the student_data.json file and uses the AWS SDK for Python (Boto3) to interact with DynamoDB.

workload.py:
The workload script generates a test case by uploading video files to the input bucket. It prepares the system for testing the video processing workflow.

.env:
Contain environment variable settings for AWS and Ceph configurations.

notification.py:
The notification script monitors the input bucket and triggers the face recognition function when new objects are uploaded. It uses a simple HTTP listener to invoke the OpenFaaS function.

## Getting Started


1. Setup Environment: Ensure that you have the necessary environment variables set, including AWS and Ceph credentials.

2. Install Dependencies: Install the required Python packages using pip install -r requirements.txt.

3. Run the Workload Script: Execute workload.py to simulate a workload by uploading test videos to the input bucket.

4. Triggers notification: Execute notification.py to trigger the openfaas function.
