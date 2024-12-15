# Final Project - CI/CD

This project demonstrates how to deploy a simple Flask application using AWS CDK and integrate it with AWS services such as S3, Lambda, and API Gateway.

## File Structure

- `app/`: Contains the Flask app and frontend (HTML) files.
- `cdk/`: AWS CDK stack configuration.
- `tests/`: Unit tests for the Flask app.
- `Dockerfile`: Containerizes the Flask app.
- `requirements.txt`: Lists the dependencies for the project.
- `pipeline.yaml`: AWS CodePipeline configuration for CI/CD.
- `buildspec.yml`: AWS CodeBuild configuration for building the app.
- `README.md`: Project documentation.

## Steps to Run the Application

1. **Set Up the Environment:**
   - Install AWS CDK and dependencies using the following:
     ```bash
     npm install -g aws-cdk
     pip install -r requirements.txt
     ```

2. **Deploy Using AWS CDK:**
   - Run the following command to bootstrap and deploy the CDK stack:
     ```bash
     cdk deploy --profile <your-aws-profile>
     ```

3. **Run the Flask App Locally (Optional):**
   - If you want to test the Flask app locally, run:
     ```bash
     python app/app.py
     ```

4. **CI/CD Pipeline:**
   - The `pipeline.yaml` and `buildspec.yml` files will automatically trigger the build and deployment on code push to the `main` branch in GitHub.

## Author

Ajay Panchal
