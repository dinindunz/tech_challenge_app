from aws_cdk import aws_ecr as ecr, aws_ecr_assets as ecr_assets
from constructs import Construct
import cdk_ecr_deployment as cdk_ecr_deployment


class BuildEcrImage(Construct):
    """ECR Repo Construct."""

    def __init__(
        self,
        scope: Construct,
        construct_id: str,
        ecr_repo_name: str,
        image_tag: str,
        directory: str,
        account: str,
        region: str,
        **kwargs,
    ) -> None:

        """This construct can be used to create a new ECR repo, build the docker image and push it to the ECR repo.

        Args:
            scope (Construct):
            construct_id (str):
            ecr_repo_name (str):
            image_tag (str):
            directory (str):
            account (str):
            region (str):
        """

        super().__init__(scope, construct_id, **kwargs)

        # Create ECR Repo
        ecr_repo = ecr.Repository(
            self, f"{construct_id}-Ecr-Repo", repository_name=ecr_repo_name
        )

        # Build Docker Image
        docker_image = ecr_assets.DockerImageAsset(
            self, ecr_repo_name, directory=directory
        )

        # Push Image to ECR
        ecr_deployment = cdk_ecr_deployment.ECRDeployment(
            self,
            f"{construct_id}-Ecr-Deployment",
            src=cdk_ecr_deployment.DockerImageName(docker_image.image_uri),
            dest=cdk_ecr_deployment.DockerImageName(
                f"{account}.dkr.ecr.{region}.amazonaws.com/{ecr_repo_name}:{image_tag}"
            ),
        )
