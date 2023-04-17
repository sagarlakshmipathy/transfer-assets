# TransferAssets.py
This Python program uses boto3 library to transfer ownership of QuickSight dashboards, data sets, data sources, analyses, themes, folders and templates to another owner. It also optionally deletes the original owner.
## Installation
To run this program, you need to install the required packages listed in the `requirements.txt` file. You can install the required packages using pip:
`
pip3 install -r requirements.txt
`
## Usage
The program can be run using the following command:
`
python3 TransferAssets.py --old_owner_user_name <OLD_OWNER_USER_NAME> --old_owner_namespace <OLD_OWNER_NAMESPACE> --new_owner_user_name <NEW_OWNER_USER_NAME> --new_owner_namespace <NEW_OWNER_NAMESPACE> --assets_region <ASSETS_REGION> --account_id <ACCOUNT_ID> [--delete_user_from_quicksight]
`
Here are the details of the command line arguments:

`--old_owner_user_name`: Specify the user name of the owner to be deleted.

`--old_owner_namespace`: Specify the namespace of the owner to be deleted.

`--new_owner_user_name`: Specify the user name to transfer the assets to.

`--new_owner_namespace`: Specify the namespace of the user to transfer the assets to.

`--assets_region`: Specify the region where the assets are located.

`--account_id`: Specify the account ID where the assets are located.

`--delete_user_from_quicksight`: Specify this flag if you want to delete the original owner.

Note that the `--delete_user_from_quicksight` flag is optional.

## Example
Here is an example command to transfer assets and delete the original owner:

`
python3 TransferAssets.py --old_owner_user_name john_doe --old_owner_namespace default --new_owner_user_name jane_doe --new_owner_namespace default --assets_region us-east-1 --account_id 123456789 --delete_user_from_quicksight
`

## License
This project is licensed under the MIT License - see the [LICENSE] file for details.
