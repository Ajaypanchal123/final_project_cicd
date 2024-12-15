# Comprehensive CI/CD Pipeline for Application Deployment

## Description
This project demonstrates a CI/CD pipeline for deploying a web application and its associated AWS infrastructure.

## Features
- A Flask web application with frontend and API.
- Infrastructure defined using AWS CDK.
- CI/CD pipeline using GitHub Actions.

## Steps to Run Locally
1. Install dependencies:

final-project-cicd/
├── .github/
│   └── workflows/
│       └── ci-cd-pipeline.yml
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
├── cdk/
│   ├── __init__.py
│   ├── app_stack.py
├── requirements.txt
├── requirements-dev.txt
├── cdk.json
├── tests/
│   └── test_app.py
└── README.md
