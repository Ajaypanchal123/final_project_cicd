from aws_cdk import (
    Stack,
    aws_s3 as s3,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_s3_deployment as s3_deployment,
)
from constructs import Construct

class AppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # S3 bucket for frontend
        bucket = s3.Bucket(self, "FrontendBucket", 
                           website_index_document="index.html", 
                           public_read_access=True)

        # Deploy frontend to S3 bucket
        s3_deployment.BucketDeployment(self, "DeployFrontend", 
            sources=[s3_deployment.Source.asset("./app/templates")],
            destination_bucket=bucket)

        # Lambda function for backend (Flask app)
        backend_function = _lambda.Function(
            self, "BackendFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            handler="app.lambda_handler",
            code=_lambda.Code.from_asset("../app")
        )

        # API Gateway to expose Lambda function
        api = apigateway.LambdaRestApi(self, "APIGateway", handler=backend_function)

        # Outputs to show the URLs of S3 and API Gateway
        self.bucket = bucket
        self.api = api
