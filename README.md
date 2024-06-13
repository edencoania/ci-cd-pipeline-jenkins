# CI/CD Pipeline for Weather Application

This Jenkins pipeline automates the CI/CD process for deploying the Weather Application. It includes stages for cleaning up resources, building Docker images, running tests, pushing images to Docker Hub, deploying to AWS, and handling post-build notifications.

## Pipeline Overview

The pipeline consists of the following stages:

1. **SCM**: Checks out the source code repository.
2. **Clean**: Cleans up Docker images, containers, and system resources.
3. **Build**: Builds Docker images for the application and nginx.
4. **Test**: Executes unit tests and Selenium tests for the Weather Application.
5. **Push to Docker Hub**: Tags and pushes Docker images to Docker Hub.
6. **Deploy**: Deploys the application to AWS using Docker Compose.
7. **Post-Build Actions**: Performs cleanup and sends notifications based on build status.

## Prerequisites

- Jenkins with necessary plugins (Pipeline, Git, Docker, etc.)
- Docker Hub credentials stored in Jenkins credentials as `docker-hub-creds`.
- AWS EC2 instance with Docker installed and accessible via SSH.

## How to Run the Pipeline

1. **Configure Jenkins**:
   - Ensure Jenkins is set up with the necessary plugins and configurations.
   - Add Docker Hub credentials (`docker-hub-creds`) in Jenkins credentials.

2. **Set Up AWS**:
   - Create an EC2 instance with Docker installed.
   - Place your `weather.pem` SSH key in the project directory.

3. **Configure Pipeline**:
   - Create a new pipeline job in Jenkins.
   - Copy and paste the Jenkinsfile content provided in this repository.

4. **Run the Pipeline**:
   - Trigger the pipeline manually or set up webhook for automatic triggering.
   - Monitor the pipeline stages in Jenkins console.

5. **Deployment Verification**:
   - After successful deployment, verify the application is running correctly on AWS.

## Example

To run the pipeline manually:

1. Open Jenkins and navigate to your pipeline job.
2. Click on "Build Now" to trigger the pipeline.

## Cleanup

- After deployment, the pipeline automatically cleans up Docker resources using `docker system prune -f`.
- Ensure to monitor and manage Docker resources to avoid excessive buildup.

