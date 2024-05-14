# Dockerized Flask Joke App

This repository contains a simple Flask application that generates jokes using the `pyjokes` library and displays them via a web interface.


## Setup Instructions

### Prerequisites
- [Docker](https://www.docker.com/) installed on your machine

### Running the Application

1. **Clone the Repository:**

```
git clone https://github.com/EdagPSIT/Joke-App-Flask.git
cd Joke-App-Flask
```

2. **Build the Docker Image:**

`docker build -t joke-web-app .`

3. **Run the Docker Container**

`docker run -d -p 5000:5000 joke-web-app`


4. **Access the Application:**

Open a web browser and go to `http://localhost:5000` to view the application.

### Application Details

- The Flask application is contained in `app.py`.
- HTML templates are stored in the `templates` directory.
- `requirements.txt` contains the necessary Python dependencies.
- The Dockerfile specifies the steps to build the Docker image.

## Application Usage

- **Home Page (`/`):** Displays a random joke fetched from the `pyjokes` library.



# Building and Pushing Docker Image to Private Elastic Container Registry (ECR)

In this guide, we'll walk through the steps to build and push a Docker image to a private Elastic Container Registry (ECR) repository on AWS.

### Prerequisites
1. **AWS CLI:** Install the AWS Command Line Interface (CLI) on your machine.
2. **AWS Configuration:** Configure AWS CLI with your credentials by running `aws configure`.
3. **AWS IAM User:** Create an IAM user with necessary permissions to access ECR. Attach the `AmazonEC2ContainerRegistryFullAccess` policy to the user.
4. **Docker:** Ensure Docker is installed on your machine.

### Steps

#### 1. Create ECR Repository
   - Log in to the AWS Management Console.
   - Navigate to the Amazon ECR service.
   - Click on "Create repository".
   - Enter a name for your repository (e.g., `my-docker-repo`) and click "Create repository".

#### 2. Build Docker Image
   - In your terminal, navigate to the directory containing your Dockerfile and application code.
   - Build the Docker image using the `docker build` command:
     ```
     docker build -t my-docker-image .
     ```

#### 3. Tag the Docker Image
   - Tag the Docker image with the URI of your ECR repository:
     ```
     docker tag my-docker-image:latest <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my-docker-repo:latest
     ```
     Replace `<aws_account_id>` with your AWS account ID and `<region>` with your AWS region.

#### 4. Authenticate Docker to ECR
   - Authenticate Docker to your ECR registry:
     ```
     aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<region>.amazonaws.com
     ```
     Replace `<aws_account_id>` and `<region>` with your AWS account ID and region.

#### 5. Push Docker Image to ECR
   - Push the Docker image to your ECR repository:
     ```
     docker push <aws_account_id>.dkr.ecr.<region>.amazonaws.com/my-docker-repo:latest
     ```
     This command will push the Docker image to your ECR repository.

### Conclusion
You have successfully built and pushed a Docker image to your private Elastic Container Registry (ECR) repository on AWS. You can now use this image in your containerized applications deployed on AWS.

For further integration with CI/CD pipelines or deployment, refer to AWS documentation or consult with your team's DevOps engineer.



  

