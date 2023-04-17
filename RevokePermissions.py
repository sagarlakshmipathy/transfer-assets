# imports
import boto3

assets_region = ''
session = boto3.Session(region_name=assets_region)

qs_client = session.client('quicksight')

# Specify the user you want to delete
user_name_for_revoke = ''

dashboard_id = ''
analysis_id = ''
theme_id = ''
template_id = ''
data_set_id = ''
data_source_id = ''
folder_id = ''

account_id = ''

def get_dashboard_owner_actions(dashboard_id):
    permissions_response = qs_client.describe_dashboard_permissions(
        AwsAccountId=account_id,
        DashboardId=dashboard_id
    )
    
    print(permissions_response)
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}":
            print(permission)
            return permission

def get_analysis_owner_actions(analysis_id):
    permissions_response = qs_client.describe_analysis_permissions(
        AwsAccountId=account_id,
        AnalysisId=analysis_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}":
            return permission

def get_theme_owner_actions(theme_id):
    permissions_response = qs_client.describe_theme_permissions(
        AwsAccountId=account_id,
        ThemeId=theme_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}":
            return permission

def get_template_owner_actions(template_id):
    permissions_response = qs_client.describe_template_permissions(
        AwsAccountId=account_id,
        TemplateId=template_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}":
            return permission

def get_data_source_owner_actions(data_source_id):
    permissions_response = qs_client.describe_data_source_permissions(
        AwsAccountId=account_id,
        DataSourceId=data_source_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}":
            return permission

def get_data_set_owner_actions(data_set_id):
    permissions_response = qs_client.describe_data_set_permissions(
        AwsAccountId=account_id,
        DataSetId=data_set_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}":
            return permission

def get_folder_owner_actions(folder_id):
    permissions_response = qs_client.describe_folder_permissions(
        AwsAccountId=account_id,
        FolderId=folder_id
    )
    
    for permission in permissions_response['Permissions']:
        if permission['Principal'] == f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}":
            return permission

def revoke_dashboard_ownership(account_id, user_name_for_revoke):
    if get_dashboard_owner_actions(dashboard_id):
        qs_client.update_dashboard_permissions(
            AwsAccountId=account_id,
            DashboardId=dashboard_id,
            RevokePermissions=[
                {
                    'Principal': f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}",
                    'Actions': get_dashboard_owner_actions(dashboard_id)['Actions']
                }
            ]   
        )
        
        return get_dashboard_owner_actions(dashboard_id)['Principal']
    
def revoke_analysis_ownership(account_id, user_name_for_revoke):
    if get_analysis_owner_actions(analysis_id):
        qs_client.update_analysis_permissions(
            AwsAccountId=account_id,
            AnalysisId=analysis_id,
            RevokePermissions=[
                {
                    'Principal': f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}",
                    'Actions': get_analysis_owner_actions(analysis_id)['Actions']
                }
            ]   
        )
        
        return get_analysis_owner_actions(analysis_id)['Principal']
    
def revoke_theme_ownership(account_id, user_name_for_revoke):
    if get_theme_owner_actions(theme_id):
        qs_client.update_theme_permissions(
            AwsAccountId=account_id,
            ThemeId=theme_id,
            RevokePermissions=[
                {
                    'Principal': f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}",
                    'Actions': get_theme_owner_actions(theme_id)['Actions']
                }
            ]   
        )
        
        return get_theme_owner_actions(theme_id)['Principal']
        
def revoke_template_ownership(account_id, user_name_for_revoke):
    if get_template_owner_actions(template_id):
        qs_client.update_template_permissions(
            AwsAccountId=account_id,
            TemplateId=template_id,
            RevokePermissions=[
                {
                    'Principal': f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}",
                    'Actions': get_template_owner_actions(template_id)['Actions']
                }
            ]   
        )
    
    return get_template_owner_actions(template_id)['Principal']
    
    
def revoke_data_source_ownership(account_id, user_name_for_revoke):
    if get_data_set_owner_actions(data_set_id):
        qs_client.update_data_source_permissions(
            AwsAccountId=account_id,
            DataSourceId=data_source_id,
            RevokePermissions=[
                {
                    'Principal': f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}",
                    'Actions': get_data_set_owner_actions(data_set_id)['Actions']
                }
            ]   
        )
    
    return get_data_set_owner_actions(data_set_id)['Principal']
    
def revoke_dataset_ownership(account_id, user_name_for_revoke):
    if get_data_source_owner_actions(data_source_id):
        qs_client.update_data_set_permissions(
            AwsAccountId=account_id,
            DataSetId=data_set_id,
            RevokePermissions=[
                {
                    'Principal': f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}",
                    'Actions': get_data_source_owner_actions(data_source_id)['Actions']
                }
            ]   
        )
        
        return get_data_source_owner_actions(data_source_id)['Principal']
    
def revoke_folder_ownership(account_id, user_name_for_revoke):
    if get_folder_owner_actions(folder_id):
        qs_client.update_folder_permissions(
            AwsAccountId=account_id,
            FolderId=folder_id,
            RevokePermissions=[
                {
                    'Principal': f"arn:aws:quicksight:us-east-1:{account_id}:user/default/{user_name_for_revoke}",
                    'Actions': get_folder_owner_actions(folder_id)['Actions']
                }
            ]   
        )
        
    return get_folder_owner_actions(folder_id)['Principal']


# function calls to revoke ownership of assets
revoke_dashboard_ownership(account_id, user_name_for_revoke)
revoke_analysis_ownership(account_id, user_name_for_revoke)
revoke_dataset_ownership(account_id, user_name_for_revoke)
revoke_theme_ownership(account_id, user_name_for_revoke)
revoke_template_ownership(account_id, user_name_for_revoke)
revoke_data_source_ownership(account_id, user_name_for_revoke)
revoke_folder_ownership(account_id, user_name_for_revoke)