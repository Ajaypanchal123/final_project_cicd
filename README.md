# Comprehensive CI/CD Pipeline for Web Application Deployment

## Description
This project implements a CI/CD pipeline to automate the deployment of a simple web application using AWS CDK. The application consists of a frontend (HTML) and a backend (Python Flask API). The pipeline is triggered on code pushes to the GitHub repository and automates the deployment of AWS infrastructure (S3, Lambda, API Gateway).

## Infrastructure
- S3 bucket for static site hosting.
- Lambda function for backend API.
- API Gateway to serve the backend.

## CI/CD Pipeline
- **GitHub Actions** is used for automating the build, test, and deploy process.
- Stages: Source → Build → Test → Deploy.

## Deployment
1. Ensure AWS credentials are configured in GitHub Secrets.
2. Push code to the `main` branch.
3. The pipeline will automatically deploy the application.

## Testing
Tests for the API routes are located in the `tests/` folder.

