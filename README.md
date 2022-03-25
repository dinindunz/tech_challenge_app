
# Welcome to Tech Challenge App CDK Python project!

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ python3 -m pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `requirements.txt` file and rerun the `python3 -m pip install -r requirements.txt`
command.

## Pre-Requisites
 
 * `Install Go` 
 * `Install Python`                      Supported versions -> 3.8, 3.9, 3.10
 * `Setup AWS Credentials Profile`       Set AWS credentials in ~/.aws/credentials
 * `Add Credentials profile to cdk.json` Include aws_region and aws_account_id

## Steps to Deploy

 * `Run ./cdk_deploy.sh`
Format and lint the code
Bootstrap AWS account
Deploy VPC, RDS, Build Docker Image, Deploy Fargate Cluster

## Useful CDK Commands

 * `cdk ls --profile aws_creds_profile`          List all stacks in the app
 * `cdk synth --profile aws_creds_profile`       Emits the synthesized CloudFormation template to cdk.out folder
 * `cdk deploy --profile aws_creds_profile`      Deploy this stack to your default AWS account/region
 * `cdk diff --profile aws_creds_profile`        Compare deployed stack with current state
 * `cdk docs`                                    Open CDK documentation
 * `cdk bootstrap --profile aws_creds_profile`   Bootstrap AWS account

Enjoy!
