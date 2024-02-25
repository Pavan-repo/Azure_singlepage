from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

organization_url = "https://dev.azure.com/NRG-Acceleration/"
project = 'NRG-Acceleration'
personal_access_token = "nmrww4zqxhkal32gbhuq2eo3zljxcz4l4fs37zvvjsswalcr6c4q"
# Connect to Azure DevOps
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Access work item tracking client
wit_client = connection.clients.get_work_item_tracking_client()

epic_id = 1060 
area_path = 'NRG_Agile_Enablement'

def create_azure_issue(title,description,anforderer, story_points,type_picker):
    
    new_work_item = [
            {
               "op": "add",
                "path": "/fields/System.Title",
                "from": None,
               "value": title
            },
            {
               "op": "add",
                "path": "/fields/Microsoft.VSTS.CodeReview.ContextOwner",
                "from": None,
                "value": anforderer
            },
            {
                "op": "add",
                "path": "/fields/System.Description",
                "from": None,
                "value": f"{description}"
            },
            {
                "op": "add",
                "path": "/fields/System.WorkItemType",
                "from": None,
                "value": {'name': type_picker}
            },
            {
                "op": "add",
                "path": "/fields/System.Parent",
                "from": None,
                "value": epic_id
            },
            {
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": f"{organization_url}/{project}/_apis/wit/workItems/{epic_id}",
                    "attributes": {
                        "comment": "Parent link to Epic"
                    }
                }
            },
            {
                "op": "add",
                "path": "/fields/Microsoft.VSTS.Scheduling.StoryPoints",
                "from": None,
                "value": story_points
            },
            
            {
                "op": "add",
                "path": "/fields/System.AreaPath",
                "from": None,
                "value":f"{project}\\{area_path}" 
            }
        ]
    created_work_item = wit_client.create_work_item(project=project,document=new_work_item, type=type_picker)
    return (f"Created {type_picker} with ID:{created_work_item.id} ")
    