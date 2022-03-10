#!/usr/bin/env python3
import os

import aws_cdk as cdk
import common.get_environment as get_environment
from stacks.tech_challenge_vpc import TechChallengeVpc
from stacks.tech_challenge_app import TechChallengeApp
from stacks.tech_challenge_rds import TechChallengeRds


app = cdk.App()

# Get Cdk Environment of the AWS account
env, env_context = get_environment.env_context("devopstesting")

# Deploy VPC Stack
vpc = TechChallengeVpc(app, "Tech-Challenge-Vpc", env=env).vpc

# Deploy Postgres RDS Stack
TechChallengeRds(app, "Tech-Challenge-Rds", vpc=vpc, env=env)

# Deploy Tech Challenge App
TechChallengeApp(app, "Tech-Challenge-App", vpc=vpc, env=env)

app.synth()
