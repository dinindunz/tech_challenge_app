from aws_cdk import Duration, Stack, aws_ec2 as ec2, aws_rds as rds
from constructs import Construct


class TechChallengeRds(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Deploy Postgres RDS Instance in Private Subnet with MultiAZ
        db = rds.DatabaseCluster(
            self,
            id=f"{construct_id}-Postgres",
            cluster_identifier=f"{construct_id}-Postgres",
            engine=rds.DatabaseClusterEngine.aurora_postgres(version=rds.AuroraPostgresEngineVersion.VER_13_3),
            instance_props=rds.InstanceProps(
                vpc=vpc,
                vpc_subnets=ec2.SubnetSelection(
                    subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
                ),
                instance_type=ec2.InstanceType.of(
                    ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MEDIUM
                ),
                publicly_accessible=True,
            ),
            deletion_protection=False
        )