import aws_cdk as cdk
import functools


@functools.lru_cache(maxsize=32)
def env_context(aws_account: str = None) -> list:
    app = cdk.App()
    env_context = app.node.try_get_context(aws_account)
    aws_account_id = env_context["aws_account_id"]
    aws_region = env_context["aws_region"]
    env = cdk.Environment(account=aws_account_id, region=aws_region)
    return env, env_context
