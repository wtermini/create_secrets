# AWS Secrets Manager Automation

This repository contains a Python script and AWS CodeBuild configuration to automate the creation and deletion of secrets in AWS Secrets Manager using AWS CodePipeline.

## Overview

The `create_secret.py` Python script reads the `CREATE_SECRET_NAMES` and `DELETE_SECRET_NAMES` environment variables, which contain comma-separated lists of secret names to be created and deleted, respectively. The script then iterates over each list, creating or deleting secrets as specified.

The `buildspec.yml` file is used by AWS CodeBuild to configure the build environment and execute the Python script.

## Usage

1. Create an AWS CodePipeline with a source stage pointing to this repository.
2. Set up an AWS CodeBuild project as a build stage in the pipeline, with the following environment variables:

   - `CREATE_SECRET_NAMES`: A comma-separated list of secret names to be created (e.g., "Secret1,Secret2,Secret3").
   - `DELETE_SECRET_NAMES`: A comma-separated list of secret names to be deleted (e.g., "Secret4,Secret5,Secret6").

3. In the CodeBuild project, use the `buildspec.yml` file provided in this repository.
4. Ensure that the IAM role associated with the CodeBuild project has the necessary permissions to create, delete, and describe secrets in AWS Secrets Manager. The required permissions are:

   - `secretsmanager:DescribeSecret`
   - `secretsmanager:CreateSecret`
   - `secretsmanager:DeleteSecret`

5. Start the pipeline, which will create or delete secrets in AWS Secrets Manager based on the environment variables provided.

## Customizing

You can customize the Python script or the `buildspec.yml` file to add more features or change the behavior of the automation. For example, you can add more environment variables to control other aspects of secret creation or deletion, or you can modify the script to handle more complex scenarios.

## License

This project is licensed under the [WTFPL](LICENSE).
