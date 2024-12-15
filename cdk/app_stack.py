from aws_cdk import (
    core,
    aws_s3 as s3,
    aws_ec2 as ec2,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    aws_iam as iam,
    aws_s3_deployment as s3_deployment,
)

class WebAppStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # S3 bucket for hosting the frontend
        bucket = s3.Bucket(self, "WebAppBucket", website_index_document="index.html", website_error_document="error.html")

        # Lambda function for backend
        backend_lambda = _lambda.Function(self, "BackendFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="app.api",  # This points to the function in app.py
            code=_lambda.Code.from_asset("app"),  # Folder where app.py is located
        )

        # API Gateway to trigger Lambda
        api = apigateway.LambdaRestApi(self, "WebApi",
            handler=backend_lambda,
        )

        # Deployment of frontend content to S3
        s3_deployment.BucketDeployment(self, "DeployWebsite",
            sources=[s3_deployment.Source.asset("app/templates")],
            destination_bucket=bucket,
        )

        # Output the URL of the S3 bucket
        core.CfnOutput(self, "WebsiteURL", value=bucket.bucket_website_url)
