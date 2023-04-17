import json
import boto3

account_id = '733585711144'
region_id = 'us-east-1'

session = boto3.Session(region_name=region_id)
qs_client = session.client('quicksight')

data_source_id = '61976948-be7b-432b-97ba-1d696a8232a0'
data_set_id = 'bfd27db6-28de-426d-97e3-3e5b35ba29f1'
dashboard_id = '6029d740-2bf3-4a5b-bde6-4691eedbabbc'
analysis_id = 'ab1cb626-d7ac-4539-9894-62428acc91bf'
theme_id = '5c6bf0df-ac73-452e-86b3-e7dfdda811e1'
template_id = 'Test1'
folder_id = '1d461ea8-728b-4250-8167-c4fb8b8df368'

print(f"\nPermissions for Data Source: {data_source_id}")
parsed_data_source_permissions = json.dumps(qs_client.describe_data_source_permissions(
    AwsAccountId=account_id,
    DataSourceId=data_source_id
    )['Permissions'], indent=4, default=str)
print(parsed_data_source_permissions)

print(f"\nPermissions for DataSet: {data_set_id}")
parsed_data_set_permissions = json.dumps(qs_client.describe_data_set_permissions(
    AwsAccountId=account_id,
    DataSetId=data_set_id
    )['Permissions'], indent=4, default=str)
print(parsed_data_set_permissions)

print(f"\nPermissions for Dashboard: {dashboard_id}")
parsed_dashboard_permissions = json.dumps(qs_client.describe_dashboard_permissions(
    AwsAccountId=account_id,
    DashboardId=dashboard_id
    )['Permissions'], indent=4, default=str)
print(parsed_dashboard_permissions)

print(f"\nPermissions for Template: {template_id}")
parsed_template_permissions = json.dumps(qs_client.describe_template_permissions(
    AwsAccountId=account_id,
    TemplateId=template_id
    )['Permissions'], indent=4, default=str)
print(parsed_template_permissions)

print(f"\nPermissions for Theme: {theme_id}")
parsed_theme_permissions = json.dumps(qs_client.describe_theme_permissions(
    AwsAccountId=account_id,
    ThemeId=theme_id
    )['Permissions'], indent=4, default=str)
print(parsed_theme_permissions)

print(f"\nPermissions for Analysis: {analysis_id}")
parsed_analysis_permissions = json.dumps(qs_client.describe_analysis_permissions(
    AwsAccountId=account_id,
    AnalysisId=analysis_id
    )['Permissions'], indent=4, default=str)
print(parsed_analysis_permissions)

print(f"\nPermissions for Folder: {folder_id}")
parsed_folder_permissions = json.dumps(qs_client.describe_folder_permissions(
    AwsAccountId=account_id,
    FolderId=folder_id
    )['Permissions'], indent=4, default=str)
print(parsed_folder_permissions)