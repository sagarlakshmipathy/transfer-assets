# imports
import boto3

account_id = '733585711144'
region_id = 'us-east-1'

session = boto3.Session(region_name=region_id)
qs_client = session.client('quicksight')

# Specify the user you want to delete
user_name_for_revoke = 'test_admin2'
user_namespace_for_revoke = 'default'

data_source_id = '61976948-be7b-432b-97ba-1d696a8232a0'
data_set_id = 'bfd27db6-28de-426d-97e3-3e5b35ba29f1'
dashboard_id = '6029d740-2bf3-4a5b-bde6-4691eedbabbc'
analysis_id = 'ab1cb626-d7ac-4539-9894-62428acc91bf'
theme_id = '5c6bf0df-ac73-452e-86b3-e7dfdda811e1'
template_id = 'Test1'
folder_id = '1d461ea8-728b-4250-8167-c4fb8b8df368'

old_user_arn = f"arn:aws:quicksight:us-east-1:{account_id}:user/{user_namespace_for_revoke}/{user_name_for_revoke}"

def get_dashboard_owner_actions(dashboard_id):
    permissions_response = qs_client.describe_dashboard_permissions(
        AwsAccountId=account_id,
        DashboardId=dashboard_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == old_user_arn:
            return permission


def get_analysis_owner_actions(analysis_id):
    permissions_response = qs_client.describe_analysis_permissions(
        AwsAccountId=account_id,
        AnalysisId=analysis_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == old_user_arn:
            return permission


def get_theme_owner_actions(theme_id):
    permissions_response = qs_client.describe_theme_permissions(
        AwsAccountId=account_id,
        ThemeId=theme_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == old_user_arn:
            return permission


def get_template_owner_actions(template_id):
    permissions_response = qs_client.describe_template_permissions(
        AwsAccountId=account_id,
        TemplateId=template_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == old_user_arn:
            return permission


def get_data_source_owner_actions(data_source_id):
    permissions_response = qs_client.describe_data_source_permissions(
        AwsAccountId=account_id,
        DataSourceId=data_source_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == old_user_arn:
            return permission


def get_data_set_owner_actions(data_set_id):
    permissions_response = qs_client.describe_data_set_permissions(
        AwsAccountId=account_id,
        DataSetId=data_set_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == old_user_arn:
            return permission


def get_folder_owner_actions(folder_id):
    permissions_response = qs_client.describe_folder_permissions(
        AwsAccountId=account_id,
        FolderId=folder_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == old_user_arn:
            return permission


def revoke_dashboard_ownership(account_id, old_user_arn):
    if get_dashboard_owner_actions(dashboard_id):
        qs_client.update_dashboard_permissions(
            AwsAccountId=account_id,
            DashboardId=dashboard_id,
            RevokePermissions=[
                {
                    'Principal': old_user_arn,
                    'Actions': get_dashboard_owner_actions(dashboard_id)['Actions']
                }
            ]   
        )


def revoke_analysis_ownership(account_id, old_user_arn):
    if get_analysis_owner_actions(analysis_id):
        qs_client.update_analysis_permissions(
            AwsAccountId=account_id,
            AnalysisId=analysis_id,
            RevokePermissions=[
                {
                    'Principal': old_user_arn,
                    'Actions': get_analysis_owner_actions(analysis_id)['Actions']
                }
            ]   
        )


def revoke_theme_ownership(account_id, old_user_arn):
    if get_theme_owner_actions(theme_id):
        qs_client.update_theme_permissions(
            AwsAccountId=account_id,
            ThemeId=theme_id,
            RevokePermissions=[
                {
                    'Principal': old_user_arn,
                    'Actions': get_theme_owner_actions(theme_id)['Actions']
                }
            ]   
        )


def revoke_template_ownership(account_id, old_user_arn):
    if get_template_owner_actions(template_id):
        qs_client.update_template_permissions(
            AwsAccountId=account_id,
            TemplateId=template_id,
            RevokePermissions=[
                {
                    'Principal': old_user_arn,
                    'Actions': get_template_owner_actions(template_id)['Actions']
                }
            ]   
        )
    
    
def revoke_dataset_ownership(account_id, old_user_arn):
    if get_data_set_owner_actions(data_set_id):
        qs_client.update_data_set_permissions(
            AwsAccountId=account_id,
            DataSetId=data_set_id,
            RevokePermissions=[
                {
                    'Principal': old_user_arn,
                    'Actions': get_data_set_owner_actions(data_set_id)['Actions']
                }
            ]   
        )


def revoke_data_source_ownership(account_id, old_user_arn):
    if get_data_source_owner_actions(data_source_id):
        qs_client.update_data_source_permissions(
            AwsAccountId=account_id,
            DataSourceId=data_source_id,
            RevokePermissions=[
                {
                    'Principal': old_user_arn,
                    'Actions': get_data_source_owner_actions(data_source_id)['Actions']
                }
            ]   
        )        


def revoke_folder_ownership(account_id, old_user_arn):
    if get_folder_owner_actions(folder_id):
        qs_client.update_folder_permissions(
            AwsAccountId=account_id,
            FolderId=folder_id,
            RevokePermissions=[
                {
                    'Principal': old_user_arn,
                    'Actions': get_folder_owner_actions(folder_id)['Actions']
                }
            ]   
        )


# function calls to revoke ownership of assets
revoke_dashboard_ownership(account_id, old_user_arn)
revoke_analysis_ownership(account_id, old_user_arn)
revoke_dataset_ownership(account_id, old_user_arn)
revoke_theme_ownership(account_id, old_user_arn)
revoke_template_ownership(account_id, old_user_arn)
revoke_data_source_ownership(account_id, old_user_arn)
revoke_folder_ownership(account_id, old_user_arn)