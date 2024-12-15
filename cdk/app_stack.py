from aws_cdk import (
    aws_s3 as s3,
    aws_iam as iam,
    Stack
)
from constructs import Construct

class AppStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket
        bucket = s3.Bucket(self, "MyBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=s3.RemovalPolicy.DESTROY
        )
        
        # Grant the CloudFormation role the necessary permission to put the bucket policy
        cfn_exec_role = iam.Role(self, "CFNExecutionRole",
            assumed_by=iam.ServicePrincipal("cloudformation.amazonaws.com")
        )

        bucket.grant_put_bucket_policy(cfn_exec_role)


# from aws_cdk import (
#     aws_s3 as s3,
#     aws_ec2 as ec2,
#     aws_iam as iam,
#     aws_lambda as _lambda,
#     aws_apigateway as apigateway,
#     Stack,
#     CfnOutput,
#     CfnParameter
# )
# from constructs import Construct
# import hashlib


# class AppStack(Stack):
#     def __init__(self, scope: Construct, id: str, **kwargs):
#         super().__init__(scope, id, **kwargs)

#         # Generate a unique bucket name using stack name and region
#         unique_bucket_name = f"{self.stack_name}-staging-{hashlib.md5(self.region.encode()).hexdigest()}"

#         # S3 bucket for frontend with secure public access
#         frontend_bucket = s3.Bucket(
#             self,
#             "FrontendBucket",
#             website_index_document="index.html",
#             public_read_access=False,
#             block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
#             removal_policy=s3.RemovalPolicy.DESTROY,
#             auto_delete_objects=True,
#         )

#         # Grant permissions for public-read access via a policy
#         frontend_bucket.add_to_resource_policy(
#             iam.PolicyStatement(
#                 actions=["s3:GetObject"],
#                 resources=[f"{frontend_bucket.bucket_arn}/*"],
#                 principals=[iam.AnyPrincipal()],
#             )
#         )

#         # VPC for backend
#         vpc = ec2.Vpc(self, "MyVpc", max_azs=2)

#         # Security group for EC2 instance
#         security_group = ec2.SecurityGroup(
#             self,
#             "InstanceSecurityGroup",
#             vpc=vpc,
#             allow_all_outbound=True,
#         )
#         security_group.add_ingress_rule(
#             ec2.Peer.any_ipv4(), ec2.Port.tcp(22), "Allow SSH access"
#         )

#         # EC2 instance for backend
#         instance = ec2.Instance(
#             self,
#             "MyInstance",
#             instance_type=ec2.InstanceType("t2.micro"),
#             machine_image=ec2.MachineImage.latest_amazon_linux(),
#             vpc=vpc,
#             security_group=security_group,
#         )

#         # Lambda function for API backend
#         backend_lambda = _lambda.Function(
#             self,
#             "BackendLambda",
#             runtime=_lambda.Runtime.PYTHON_3_9,
#             handler="app.lambda_handler",
#             code=_lambda.Code.from_asset("app"),
#         )

#         # API Gateway for the Lambda
#         api = apigateway.LambdaRestApi(self, "MyApi", handler=backend_lambda)

#         # S3 bucket for staging with a unique name
#         staging_bucket = s3.Bucket(
#             self,
#             "StagingBucket",
#             versioned=True,  # Optional but useful for staging
#             removal_policy=s3.RemovalPolicy.DESTROY,  # Cleanup when stack is deleted
#             auto_delete_objects=True,  # Automatically delete objects when the bucket is removed
#             bucket_name=unique_bucket_name,  # Unique name to avoid conflicts
#         )

#         # Outputs
#         self.add_outputs(frontend_bucket, instance, api, staging_bucket)

#     def add_outputs(self, frontend_bucket, instance, api, staging_bucket):
#         CfnOutput(self, "FrontendBucketURL", value=frontend_bucket.bucket_website_url)
#         CfnOutput(self, "InstancePublicIP", value=instance.instance_public_ip)
#         CfnOutput(self, "ApiEndpoint", value=api.url)
#         CfnOutput(self, "StagingBucketName", value=staging_bucket.bucket_name)
