# **Crypto Online Radio with Icecast and AWS CloudFormation**

This project sets up a fully functional online radio streaming platform using AWS resources. The radio streams background music combined with real-time cryptocurrency quotes, utilizing services such as EC2, Icecast, AWS S3, and Polly.

The setup is designed to be reusable, customizable, and easy to deploy, making it an ideal starting point for building your own internet radio service.

<div align="center">
  <img src="https://github.com/user-attachments/assets/1a093c5d-089a-4507-b7f1-03bc41531f9e" alt="aws crypto radio">
</div>


## **Project Features**
- **Icecast Streaming Server:** Pre-configured for streaming audio.
- **Background Music:** Synthesizes dynamic audio (e.g., cryptocurrency quotes).
- **Real-time Crypto Quotes:** Fetches background tracks and Python scripts.
- **Scalable & Secure:** Uses AWS best practices for scalability and IAM security.
- **AWS Infrastructure:** Launch in minutes using AWS CloudFormation.


## **Template Features**
- **Internet Radio with Icecast:** Pre-configured for streaming audio.
- **Amazon Polly Integration:** Synthesizes dynamic audio (e.g., cryptocurrency quotes).
- **S3 Storage Support:** Fetches background tracks and Python scripts.
- **Scalable & Secure:** Uses AWS best practices for scalability and IAM security.
- **Fast Deployment:** Launch in minutes using AWS CloudFormation.


## Prerequisites

Before deploying the template, ensure the following:

1. An AWS account with required permissions to create resources.
2. An existing EC2 KeyPair.
3. Background music and [Python script](https://github.com/Ramil-code/trading_voice/blob/main/crypto_quote_radio.py) uploaded to an S3 bucket.
4. AWS CLI installed locally.

## Parameters

The CloudFormation template requires the following input parameters:

| Parameter Name        | Description                             | Default Value           |
| --------------------- | --------------------------------------- | ----------------------- |
| BucketName            | Name of the S3 bucket                   | `defaul_tbucket`        |
| BackgroundTrackName   | Name of the background music file in S3 | `default_track.mp3.mp3` |
| ScriptFileName        | Name of the Python script file in S3    | `crypto_quote_radio.py` |
| IcecastSourcePassword | Password for Icecast source connections | `Required`              |
| IcecastAdminPassword  | Password for Icecast admin interface    | `Required`              |
| KeyPairName           | Name of an existing EC2 KeyPair         | `Required`              |
| InstanceType          | EC2 instance type                       | `t2.micro`              |

## Resources Created

The template creates the following AWS resources:

- **VPC and Subnet**: Network setup for the EC2 instance.
- **Security Groups**: To allow SSH, HTTP, and Icecast streaming.
- **IAM Role**: Grants permissions for Polly and S3 access.
- **EC2 Instance**: Hosts the Icecast server and streams the audio.
- **Elastic IP**: Provides a public IP for accessing the stream.

## Deployment Instructions

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Navigate to the AWS Management Console and upload the `cloudformation-template.yaml` file.
3. In the CloudFormation console, click **Create Stack** > **With new resources**.
4. Provide the required parameters as prompted.
5. Review and launch the stack.
6. Wait 4-5 minutes after the stack creation is complete.

## Outputs

After the stack is deployed, note the following outputs:

| Output Name     | Description                         |
| --------------- | ----------------------------------- |
| RadioStreamURL  | URL for the Icecast radio stream    |
| IcecastAdminURL | URL for the Icecast admin interface |

Example output:

```
RadioStreamURL: http://<ElasticIP>:8000/stream
IcecastAdminURL: http://<ElasticIP>:8000/admin/
```

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Contributing

Feel free to fork this repository, create feature branches, and submit pull requests.

## Contact

For questions or feedback, contact [[your\_rk5027972@gmail.com](mailto\:your_rk5027972@gmail.com)].

