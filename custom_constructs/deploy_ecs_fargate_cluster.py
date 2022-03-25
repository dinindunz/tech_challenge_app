from aws_cdk import (
    aws_ecs as ecs,
    aws_ecs_patterns as ecs_patterns,
    aws_ec2 as ec2,
    aws_ecr as ecr,
)
from constructs import Construct


class DeployEcsFargateCluster(Construct):
    """ECS Fargate Construct."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        ecr_repo_name: str,
        image_tag: str,
        container_port: int,
        vpc: ec2.Vpc,
        task_definition: str,
        **kwargs,
    ) -> None:

        """This construct can be used to deploy Fargate clusters with the application.

        Args:
            scope (Construct):
            construct_id (str):
            ecr_repo_name (str):
            image_tag (str):
            container_port (int):
            vpc (ec2.Vpc):
            task_definition (str):
            security_groups (ec2.SecurityGroup):
        """
        super().__init__(scope, construct_id, **kwargs)

        # Get ECR Repo
        ecr_repo = ecr.Repository.from_repository_name(
            self, f"{construct_id}-Cluster-Ecr-Repo", repository_name=ecr_repo_name
        )

        # Create ECS Cluster
        cluster = ecs.Cluster(self, f"{construct_id}-Cluster", vpc=vpc)

        # Create Fargate Task Definition
        task_definition = ecs.FargateTaskDefinition(
            self, f"{construct_id}-Cluster-Task-Definition", family=task_definition
        )

        # Create Container
        container = task_definition.add_container(
            f"{construct_id}-Cluster-Container",
            image=ecs.ContainerImage.from_ecr_repository(ecr_repo, image_tag),
        )
        container.add_port_mappings(ecs.PortMapping(container_port=container_port))

        # Deploy Fargate Service
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self,
            f"{construct_id}-Service",
            service_name=f"{construct_id}-Service",
            cluster=cluster,
            cpu=256,
            desired_count=2,
            task_definition=task_definition,
            memory_limit_mib=512,
            public_load_balancer=True,
            task_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            #security_groups=[ecs_sg],
            platform_version=ecs.FargatePlatformVersion.VERSION1_3
        )
