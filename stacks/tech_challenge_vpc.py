from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct


class TechChallengeVpc(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Deploy the VPC in two AZs with Private and Public Subnets
        self.vpc = ec2.Vpc(
            self,
            construct_id,
            vpc_name=construct_id,
            cidr="192.168.50.0/24",
            max_azs=2,
            enable_dns_hostnames=True,
            enable_dns_support=True,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="Public-Subent",
                    subnet_type=ec2.SubnetType.PUBLIC,
                    cidr_mask=26,
                ),
                ec2.SubnetConfiguration(
                    name="Private-Subnet",
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED,
                    cidr_mask=26,
                ),
            ],
        )
