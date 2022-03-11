from aws_cdk import Stack, aws_ec2 as ec2
from constructs import Construct
from custom_constructs import (
    build_ecr_image as image,
    deploy_ecs_fargate_cluster as fargate,
)


class TechChallengeApp(Stack):
    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        vpc: ec2.Vpc,
        **kwargs,
    ) -> None:
        super().__init__(scope, construct_id, **kwargs)

        image_tag = "1.4.0"

        # Build the Docker Image
        image.BuildEcrImage(
            self,
            f"{construct_id}-Image",
            ecr_repo_name="servian/techchallengeapp",
            image_tag=image_tag,
            directory="./source/tech_challenge_app",
            account=self.account,
            region=self.region,
        )

        # Deploy the Fargate Cluster
        fargate.DeployEcsFargateCluster(
            self,
            f"{construct_id}-Fargate",
            ecr_repo_name="servian/techchallengeapp",
            image_tag=image_tag,
            container_port=3000,
            vpc=vpc,
            task_definition="tech_challenge_app_task_definition",
        )
