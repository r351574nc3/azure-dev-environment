import os
from azure_dev_environment import virtual_machine

subscription_id = os.environ.get(
    'AZURE_SUBSCRIPTION_ID',
    '11111111-1111-1111-1111-111111111111') # your Azure Subscription Id
resource_group = os.environ.get(
    'AZURE_DEFAULT_RESOURCE_GROUP',
    'my-resource-group') # Resource group to deploy to
location = os.environ.get('LOCATION', 'centralus')

def vm_deployer():
    return virtual_machine.deployer.Deployer(subscription_id, resource_group)

def deploy():
    """

    """
    print("Deploying Virtual Machines to subscription {}...".format(subscription_id))
    vm_deployer().deploy(
        {
            "subscription_id": subscription_id,
            "resource_group": resource_group,
        }
    )
    print("Deployment complete.")
