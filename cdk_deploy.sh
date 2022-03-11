#!/bin/bash

echo "Activating Virtual Env"
source .venv/bin/activate 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Virtual Env not Active. Activating..."
    python3 -m venv .venv 2>/dev/null
    if [ $? -ne 0 ]; then
        echo "Python Virtual Env not found. Installing..."
        python3 -m pip install --user venv
        python3 -m venv .venv 2>/dev/null
    fi
    source .venv/bin/activate
fi

echo "Installing Requirements..."
python3 -m pip install -r requirements.txt

echo "Format the CDK Code using Black"
black app.py
black custom_constructs
black stacks

echo "Bootstrap AWS Account..."
#cdk bootstrap --profile $1

echo "Deploy VPC"
cdk deploy Tech-Challenge-Networking --require-approval never --profile $1

echo "Deploy RDS"
cdk deploy Tech-Challenge-Rds --require-approval never --profile $1

echo "Configure RDS"
cd ./tech_challenge_app/source/tech_challenge_app
./build.sh
./dist/TechChallengeApp updatedb

echo "Deploy APP"
cd ./tech_challenge_app
cdk deploy Tech-Challenge-App --require-approval never --profile $1