import boto3

aws_account_id = ''
region_id = ''

session = boto3.Session(region_name='')
qs_client = session.client('quicksight')

data_source_id = ''
data_set_id = ''
dashboard_id = ''
analysis_id = ''
theme_id = ''
template_id = ''
folder_id = ''

print(qs_client.describe_data_source_permissions(
    AwsAccountId=aws_account_id,
    DataSourceId=data_source_id
)['Permissions'])

print(qs_client.describe_data_set_permissions(
    AwsAccountId=aws_account_id,
    DataSetId=data_set_id
)['Permissions'])

print(qs_client.describe_theme_permissions(
    AwsAccountId=aws_account_id,
    ThemeId=theme_id
)['Permissions'])

print(qs_client.describe_template_permissions(
    AwsAccountId=aws_account_id,
    TemplateId=template_id
)['Permissions'])

print(qs_client.describe_dashboard_permissions(
    AwsAccountId=aws_account_id,
    DashboardId=dashboard_id
)['Permissions'])

print(qs_client.describe_analysis_permissions(
    AwsAccountId=aws_account_id,
    AnalysisId=analysis_id
)['Permissions'])

print(qs_client.describe_folder_permissions(
    AwsAccountId=aws_account_id,
    FolderId=folder_id
)['Permissions'])