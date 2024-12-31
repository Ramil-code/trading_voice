# **Crypto Online Radio with Icecast and AWS CloudFormation**

This project sets up a fully functional online radio streaming platform using AWS resources. The radio streams background music combined with real-time cryptocurrency quotes, utilizing services such as EC2, Icecast, AWS S3, and Polly.. 

The setup is designed to be reusable, customizable, and easy to deploy, making it an ideal starting point for building your own internet radio service.

---
## **Project Features**
- **Icecast Streaming Server:** Pre-configured for streaming audio.
- **Background Music:** Synthesizes dynamic audio (e.g., cryptocurrency quotes).
- **Real-time Crypto Quotes:** Fetches background tracks and Python scripts.
- **Scalable & Secure:** Uses AWS best practices for scalability and IAM security.
- **AWS Infrastructure:** Launch in minutes using AWS CloudFormation.


---

## **Template Features**
- **Internet Radio with Icecast:** Pre-configured for streaming audio.
- **Amazon Polly Integration:** Synthesizes dynamic audio (e.g., cryptocurrency quotes).
- **S3 Storage Support:** Fetches background tracks and Python scripts.
- **Scalable & Secure:** Uses AWS best practices for scalability and IAM security.
- **Fast Deployment:** Launch in minutes using AWS CloudFormation.

---
# Crypto Online Radio with AWS CloudFormation

## Overview

This project sets up a fully functional online radio streaming platform using AWS resources. The radio streams background music combined with real-time cryptocurrency quotes, utilizing services such as EC2, Icecast, AWS S3, and Polly.

## Features

- **Icecast Streaming Server:** Streams MP3 audio with cryptocurrency quotes.
- **Background Music:** Hosted on S3 and streamed alongside quotes.
- **Real-time Crypto Quotes:** Dynamically fetched and converted to audio via AWS Polly.
- **AWS Infrastructure:** Fully managed through CloudFormation.

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
| BucketName            | Name of the S3 bucket                   | `bucket19888`           |
| BackgroundTrackName   | Name of the background music file in S3 | `Chai.mp3`              |
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
6. Wait for the stack creation to complete.

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

## Customization

- Modify `crypto_quote_radio.py` for custom audio processing.
- Replace `Chai.mp3` with your preferred background track.

## Troubleshooting

- **Stack Creation Failed:** Ensure your IAM role has sufficient permissions.
- **No Stream Available:** Check Icecast server logs on the EC2 instance.
- **Elastic IP Not Accessible:** Verify the security group rules.

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

## Contributing

Feel free to fork this repository, create feature branches, and submit pull requests.

## Contact

For questions or feedback, contact [[your\_email@example.com](mailto\:your_email@example.com)].

а можно это все в виде кода мне чтобы я просто

