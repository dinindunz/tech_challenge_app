from aws_cdk import Stack, aws_ec2 as ec2, aws_rds as rds
from constructs import Construct


class TechChallengeRds(Stack):
    def __init__(
        self, scope: Construct, construct_id: str, vpc: ec2.Vpc, **kwargs
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create RDS Security Group
        rds_sg = ec2.SecurityGroup(
            self,
            f"{construct_id}-RDS-SG",
            security_group_name=f"{construct_id}-RDS-SG",
            vpc=vpc,
        )
        rds_sg.add_ingress_rule(peer=ec2.Peer.any_ipv4(), connection=ec2.Port.tcp(5432))

        # Deploy Postgres RDS Instance in Private Subnet with MultiAZ
        self.db = rds.DatabaseCluster(
            self,
            id=f"{construct_id}-Postgres",
            cluster_identifier=f"{construct_id}-Postgres",
            engine=rds.DatabaseClusterEngine.aurora_postgres(
                version=rds.AuroraPostgresEngineVersion.VER_13_3
            ),
            instance_props=rds.InstanceProps(
                vpc=vpc,
                vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
                instance_type=ec2.InstanceType.of(
                    ec2.InstanceClass.BURSTABLE3, ec2.InstanceSize.MEDIUM
                ),
                publicly_accessible=True,
                security_groups=[rds_sg],
            ),
            deletion_protection=False,
        )
