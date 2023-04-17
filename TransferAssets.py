# imports
import boto3
import argparse

# initilization
parser = argparse.ArgumentParser(description='Transfer assets and delete user')
parser.add_argument('--old_owner_user_name', type=str, required=True, help='Specify the user name to be deleted')
parser.add_argument('--old_owner_namespace', type=str, required=True, help='Specify the namespace of the to be deleted user')
parser.add_argument('--new_owner_user_name', type=str, required=True, help='Specify the user name to transfer the assets to')
parser.add_argument('--new_owner_namespace', type=str, required=True, help='Specify the namespace of the to be deleted user')
parser.add_argument('--assets_region', type=str, required=True, help='Specify the region where the assets are located')
parser.add_argument('--account_id', type=str, required=True, help='Specify the account id where the assets are located')
parser.add_argument('--delete_user_from_quicksight', action='store_true', help='Specify if you want to delete the user')

args = parser.parse_args()

assets_region = args.assets_region
session = boto3.Session(region_name=assets_region)
account_id = args.account_id

qs_client = session.client('quicksight')

# Specify the user you want to delete
old_owner_user_name = args.old_owner_user_name
old_owner_namespace = args.old_owner_namespace

# specify the user you want to transfer the assets to
new_owner_user_name = args.new_owner_user_name
new_owner_namespace = args.new_owner_namespace

old_user_arn = f"arn:aws:quicksight:us-east-1:{account_id}:user/{old_owner_namespace}/{old_owner_user_name}"

def get_permissions(id, asset_type):
    if asset_type == 'theme':
        permissions_response = qs_client.describe_theme_permissions(
            AwsAccountId=account_id,
            ThemeId=id
        )
        # if there is a DeleteTheme action, then the user is an owner
        if 'quicksight:DeleteTheme' in permissions_response['Permissions'][0]['Actions']:
            return permissions_response['Permissions'][0]['Actions']
        
    elif asset_type == 'template':
        permissions_response = qs_client.describe_template_permissions(
            AwsAccountId=account_id,
            TemplateId=id
        )
        # if there is a DeleteTemplate action, then the user is an owner
        if 'quicksight:DeleteTemplate' in permissions_response['Permissions'][0]['Actions']:
            return permissions_response['Permissions'][0]['Actions']
    

def add_new_dashboard_ownership(account_id, new_owner_namespace, new_owner_user_name):
    # Retrieve a list of all dashboards in your QuickSight account
    search_dashboards_response = qs_client.search_dashboards(
        AwsAccountId=account_id,
        Filters=[
            {
                'Name': 'QUICKSIGHT_OWNER',
                'Operator': 'StringEquals',
                'Value': old_user_arn
                }
            ]
        )
    
    # Loop through each dashboard
    for dashboard in search_dashboards_response['DashboardSummaryList']:
        dashboard_id = dashboard['DashboardId']
        
        # Retrieve a list of permissions for the dashboard
        describe_permissions_response = qs_client.describe_dashboard_permissions(
            DashboardId=dashboard_id,
            AwsAccountId=account_id
        )
        permissions = describe_permissions_response['Permissions']
        
        if len(permissions) == 1:
            # check if the user to be deleted is the only owner of the dashboard
            if permissions[0]['Principal'] == old_user_arn:
                dashboard_owner_actions = permissions[0]['Actions']
                qs_client.update_dashboard_permissions(
                    AwsAccountId=account_id,
                    DashboardId=dashboard_id,
                    GrantPermissions=[
                        {
                            "Principal": f"arn:aws:quicksight:us-east-1:{account_id}:user/{new_owner_namespace}/{new_owner_user_name}",
                            "Actions": dashboard_owner_actions
                        }
                    ]
                )
                
                print(f"Transferring ownership of dashboard {dashboard_id} to user {new_owner_user_name}")


def add_new_analysis_ownership(account_id, new_owner_namespace, new_owner_user_name):
    
    search_analyses_response = qs_client.search_analyses(
        AwsAccountId=account_id,
        Filters=[
            {
                'Name': 'QUICKSIGHT_OWNER',
                'Operator': 'StringEquals',
                'Value': f"arn:aws:quicksight:us-east-1:{account_id}:user/{old_owner_namespace}/{old_owner_user_name}"
                }
            ]
        )

    # loop through each analysis
    for analysis in search_analyses_response['AnalysisSummaryList']:
        analysis_id = analysis['AnalysisId']
        
        # Retrieve a list of permissions for the analysis
        describe_permissions_response = qs_client.describe_analysis_permissions(
            AnalysisId=analysis_id,
            AwsAccountId=account_id
        )
        permissions = describe_permissions_response['Permissions']
        
        if len(permissions) == 1:
            # check if the user to be deleted is the only owner of the analysis
            if permissions[0]['Principal'] == old_user_arn:
                analysis_owner_actions = permissions[0]['Actions']
                qs_client.update_analysis_permissions(
                    AwsAccountId=account_id,
                    AnalysisId=analysis_id,
                    GrantPermissions=[
                        {
                            "Principal": f"arn:aws:quicksight:us-east-1:{account_id}:user/{new_owner_namespace}/{new_owner_user_name}",
                            "Actions": analysis_owner_actions
                        }
                    ]
                )
                
                print(f"Transferring ownership of analysis {analysis_id} to user {new_owner_user_name}")


def add_new_data_set_ownership(account_id, new_owner_namespace, new_owner_user_name):
    # retrieve the list of datasets in your QuickSight account
    search_data_sets_response = qs_client.search_data_sets(
        AwsAccountId=account_id,
        Filters=[
            {
                'Name': 'QUICKSIGHT_OWNER',
                'Operator': 'StringEquals',
                'Value': f"arn:aws:quicksight:us-east-1:{account_id}:user/{old_owner_namespace}/{old_owner_user_name}"
                }
            ]
        )
    # loop through each dataset
    for data_set in search_data_sets_response['DataSetSummaries']:
        data_set_id = data_set['DataSetId']
        
        # Retrieve a list of permissions for the dataset
        describe_permissions_response = qs_client.describe_data_set_permissions(
            DataSetId=data_set_id,
            AwsAccountId=account_id
        )
        permissions = describe_permissions_response['Permissions']
        
        if len(permissions) == 1:
            # check if the user to be deleted is the only owner of the analysis
            if permissions[0]['Principal'] == old_user_arn:
                data_set_owner_actions = permissions[0]['Actions']
                qs_client.update_data_set_permissions(
                    AwsAccountId=account_id,
                    DataSetId=data_set_id,
                    GrantPermissions=[
                        {
                            "Principal": f"arn:aws:quicksight:us-east-1:{account_id}:user/{new_owner_namespace}/{new_owner_user_name}",
                            'Actions': data_set_owner_actions
                            }
                        ]
                    )
                    
                print(f"Transferring ownership of dataset {data_set_id} to user {new_owner_user_name}")


def add_new_theme_ownership(account_id, new_owner_namespace, new_owner_user_name):
    # retrieve the list of themes in your QuickSight account
    list_themes_response = qs_client.list_themes(
        AwsAccountId=account_id
        )

    # loop through each theme
    for theme in list_themes_response['ThemeSummaryList']:
        theme_id = theme['ThemeId']

        # Retrieve a list of permissions for the theme for all themese except default ones
        if theme_id not in ['CLASSIC', 'MIDNIGHT', 'SEASIDE', 'RAINIER']:
            describe_permissions_response = qs_client.describe_theme_permissions(
                ThemeId=theme_id,    
                AwsAccountId=account_id
                )

            permissions = describe_permissions_response['Permissions']

            if len(permissions) == 1:
                # check if the user to be deleted is the only owner of the analysis
                if permissions[0]['Principal'] == old_user_arn:
                    permissions_list = get_permissions(theme_id, 'theme')
                    if permissions_list:
                        qs_client.update_theme_permissions(
                            AwsAccountId=account_id,
                            ThemeId=theme_id,
                            GrantPermissions=[
                                {
                                    "Principal": f"arn:aws:quicksight:us-east-1:{account_id}:user/{new_owner_namespace}/{new_owner_user_name}",
                                    'Actions': permissions_list
                                    }
                                ]
                            )
                            
                        print(f"Transferring ownership of theme {theme_id} to user {new_owner_user_name}")


def add_new_template_ownership(account_id, new_owner_namespace, new_owner_user_name):
    # retrieve the list of templates in your QuickSight account
    list_templates_response = qs_client.list_templates(
        AwsAccountId=account_id
        )

    # loop through each template
    for template in list_templates_response['TemplateSummaryList']:
        template_id = template['TemplateId']
        
        # Retrieve a list of permissions for the template
        describe_permissions_response = qs_client.describe_template_permissions(
            TemplateId=template_id,   
            AwsAccountId=account_id
            )

        permissions = describe_permissions_response['Permissions']

        if len(permissions) == 1:
            # check if the user to be deleted is the only owner of the analysis
            if permissions[0]['Principal'] == old_user_arn:
                permissions_list = get_permissions(template_id, 'template')
                if permissions_list:
                    qs_client.update_template_permissions(
                        AwsAccountId=account_id,
                        TemplateId=template_id,
                        GrantPermissions=[
                            {
                                "Principal": f"arn:aws:quicksight:us-east-1:{account_id}:user/{new_owner_namespace}/{new_owner_user_name}",
                                'Actions': permissions_list
                                }
                            ]
                        )
                        
                    print(f"Transferring ownership of template {template_id} to user {new_owner_user_name}")


def add_new_data_source_ownership(account_id, new_owner_namespace, new_owner_user_name):
    # retrieve the list of data sources in your QuickSight account
    search_data_sources_response = qs_client.search_data_sources(
        AwsAccountId=account_id,
        Filters=[   
            {
                'Name': 'DIRECT_QUICKSIGHT_OWNER',
                'Operator': 'StringEquals',
                'Value': f"arn:aws:quicksight:us-east-1:{account_id}:user/{old_owner_namespace}/{old_owner_user_name}"
                }
            ]
        )

    # loop through each data source
    for data_source in search_data_sources_response['DataSourceSummaries']:
        data_source_id = data_source['DataSourceId']

        # Retrieve a list of permissions for the data source
        describe_permissions_response = qs_client.describe_data_source_permissions(
            DataSourceId=data_source_id,  
            AwsAccountId=account_id
            )

        permissions = describe_permissions_response['Permissions']

        if len(permissions) == 1:
            # check if the user to be deleted is the only owner of the analysis
            if permissions[0]['Principal'] == old_user_arn:
                data_source_owner_actions = permissions[0]['Actions']
                qs_client.update_data_source_permissions(
                    AwsAccountId=account_id,
                    DataSourceId=data_source_id,
                    GrantPermissions=[
                        {
                            "Principal": f"arn:aws:quicksight:us-east-1:{account_id}:user/{new_owner_namespace}/{new_owner_user_name}",
                            'Actions': data_source_owner_actions
                            }
                        ]
                    )
                    
                print(f"Transferring ownership of data source {data_source_id} to user {new_owner_user_name}")

              
def add_new_folder_ownership(account_id, new_owner_namespace, new_owner_user_name):
    # retrieve the list of folders in your QuickSight account
    search_folders_response = qs_client.search_folders(
        AwsAccountId=account_id,
        Filters=[
            {
                'Name': 'QUICKSIGHT_OWNER',
                'Operator': 'StringEquals',
                'Value': f"arn:aws:quicksight:us-east-1:{account_id}:user/{old_owner_namespace}/{old_owner_user_name}"
                }
            ]
        )
    

    # loop through each folder
    for folder in search_folders_response['FolderSummaryList']:
        folder_id = folder['FolderId']

        # Retrieve a list of permissions for the folder
        describe_permissions_response = qs_client.describe_folder_permissions(
            FolderId=folder_id,  
            AwsAccountId=account_id
            )

        permissions = describe_permissions_response['Permissions']

        if len(permissions) == 1:
            # check if the user to be deleted is the only owner of the analysis
            if permissions[0]['Principal'] == old_user_arn:
                folder_owner_actions = permissions[0]['Actions']
                qs_client.update_folder_permissions(
                    AwsAccountId=account_id,
                    FolderId=folder_id,
                    GrantPermissions=[
                        {
                            "Principal": f"arn:aws:quicksight:us-east-1:{account_id}:user/{new_owner_namespace}/{new_owner_user_name}",
                            'Actions': folder_owner_actions
                            }
                        ]
                    )

                print(f"Transferring ownership of folder {folder_id} to user {new_owner_user_name}")


def remove_user(account_id, old_owner_user_name, old_owner_user_namespace):
    # Delete the user from QuickSight
    boto3.client('quicksight').delete_user(
        AwsAccountId=account_id,
        UserName=old_owner_user_name,
        Namespace=old_owner_user_namespace
        )


# function calls to transfer ownership of assets
add_new_dashboard_ownership(account_id, new_owner_namespace, new_owner_user_name)
add_new_analysis_ownership(account_id, new_owner_namespace, new_owner_user_name)
add_new_data_set_ownership(account_id, new_owner_namespace, new_owner_user_name)
add_new_theme_ownership(account_id, new_owner_namespace, new_owner_user_name)
add_new_template_ownership(account_id, new_owner_namespace, new_owner_user_name)
add_new_data_source_ownership(account_id, new_owner_namespace, new_owner_user_name)
add_new_folder_ownership(account_id, new_owner_namespace, new_owner_user_name)

# check if the user needs to be deleted
if args.delete_user_from_quicksight:
    remove_user(account_id, old_owner_user_name, old_owner_namespace)
