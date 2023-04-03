import boto3
import os

create_secret_names = os.environ.get('CREATE_SECRET_NAMES', '').split(',')
delete_secret_names = os.environ.get('DELETE_SECRET_NAMES', '').split(',')
region_name = os.environ['AWS_REGION']

secrets_manager = boto3.client('secretsmanager', region_name=region_name)

for secret_name in create_secret_names:
    secret_name = secret_name.strip()
    if secret_name:
        try:
            secrets_manager.describe_secret(SecretId=secret_name)
            print(f"Secret {secret_name} already exists.")
        except secrets_manager.exceptions.ResourceNotFoundException:
            secrets_manager.create_secret(Name=secret_name)
            print(f"Created secret {secret_name}.")

for secret_name in delete_secret_names:
    secret_name = secret_name.strip()
    if secret_name:
        try:
            secrets_manager.describe_secret(SecretId=secret_name)
            secrets_manager.delete_secret(SecretId=secret_name, ForceDeleteWithoutRecovery=True)
            print(f"Deleted secret {secret_name}.")
        except secrets_manager.exceptions.ResourceNotFoundException:
            print(f"Secret {secret_name} does not exist.")
