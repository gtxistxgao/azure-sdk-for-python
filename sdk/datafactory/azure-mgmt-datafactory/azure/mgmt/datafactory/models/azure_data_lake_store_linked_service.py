# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .linked_service import LinkedService


class AzureDataLakeStoreLinkedService(LinkedService):
    """Azure Data Lake Store linked service.

    All required parameters must be populated in order to send to Azure.

    :param additional_properties: Unmatched properties from the message are
     deserialized this collection
    :type additional_properties: dict[str, object]
    :param connect_via: The integration runtime reference.
    :type connect_via:
     ~azure.mgmt.datafactory.models.IntegrationRuntimeReference
    :param description: Linked service description.
    :type description: str
    :param parameters: Parameters for linked service.
    :type parameters: dict[str,
     ~azure.mgmt.datafactory.models.ParameterSpecification]
    :param annotations: List of tags that can be used for describing the
     linked service.
    :type annotations: list[object]
    :param type: Required. Constant filled by server.
    :type type: str
    :param data_lake_store_uri: Required. Data Lake Store service URI. Type:
     string (or Expression with resultType string).
    :type data_lake_store_uri: object
    :param service_principal_id: The ID of the application used to
     authenticate against the Azure Data Lake Store account. Type: string (or
     Expression with resultType string).
    :type service_principal_id: object
    :param service_principal_key: The Key of the application used to
     authenticate against the Azure Data Lake Store account.
    :type service_principal_key: ~azure.mgmt.datafactory.models.SecretBase
    :param tenant: The name or ID of the tenant to which the service principal
     belongs. Type: string (or Expression with resultType string).
    :type tenant: object
    :param account_name: Data Lake Store account name. Type: string (or
     Expression with resultType string).
    :type account_name: object
    :param subscription_id: Data Lake Store account subscription ID (if
     different from Data Factory account). Type: string (or Expression with
     resultType string).
    :type subscription_id: object
    :param resource_group_name: Data Lake Store account resource group name
     (if different from Data Factory account). Type: string (or Expression with
     resultType string).
    :type resource_group_name: object
    :param encrypted_credential: The encrypted credential used for
     authentication. Credentials are encrypted using the integration runtime
     credential manager. Type: string (or Expression with resultType string).
    :type encrypted_credential: object
    """

    _validation = {
        'type': {'required': True},
        'data_lake_store_uri': {'required': True},
    }

    _attribute_map = {
        'additional_properties': {'key': '', 'type': '{object}'},
        'connect_via': {'key': 'connectVia', 'type': 'IntegrationRuntimeReference'},
        'description': {'key': 'description', 'type': 'str'},
        'parameters': {'key': 'parameters', 'type': '{ParameterSpecification}'},
        'annotations': {'key': 'annotations', 'type': '[object]'},
        'type': {'key': 'type', 'type': 'str'},
        'data_lake_store_uri': {'key': 'typeProperties.dataLakeStoreUri', 'type': 'object'},
        'service_principal_id': {'key': 'typeProperties.servicePrincipalId', 'type': 'object'},
        'service_principal_key': {'key': 'typeProperties.servicePrincipalKey', 'type': 'SecretBase'},
        'tenant': {'key': 'typeProperties.tenant', 'type': 'object'},
        'account_name': {'key': 'typeProperties.accountName', 'type': 'object'},
        'subscription_id': {'key': 'typeProperties.subscriptionId', 'type': 'object'},
        'resource_group_name': {'key': 'typeProperties.resourceGroupName', 'type': 'object'},
        'encrypted_credential': {'key': 'typeProperties.encryptedCredential', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(AzureDataLakeStoreLinkedService, self).__init__(**kwargs)
        self.data_lake_store_uri = kwargs.get('data_lake_store_uri', None)
        self.service_principal_id = kwargs.get('service_principal_id', None)
        self.service_principal_key = kwargs.get('service_principal_key', None)
        self.tenant = kwargs.get('tenant', None)
        self.account_name = kwargs.get('account_name', None)
        self.subscription_id = kwargs.get('subscription_id', None)
        self.resource_group_name = kwargs.get('resource_group_name', None)
        self.encrypted_credential = kwargs.get('encrypted_credential', None)
        self.type = 'AzureDataLakeStore'
