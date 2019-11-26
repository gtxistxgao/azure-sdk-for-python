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

from azure.core import PipelineClient
from msrest import Serializer, Deserializer

from ._configuration import StorageManagementClientConfiguration
from .operations import Operations
from .operations import SkusOperations
from .operations import StorageAccountsOperations
from .operations import UsagesOperations
from .operations import ManagementPoliciesOperations
from .operations import PrivateEndpointConnectionsOperations
from .operations import PrivateLinkResourcesOperations
from .operations import BlobServicesOperations
from .operations import BlobContainersOperations
from .operations import FileServicesOperations
from .operations import FileSharesOperations
from . import models


class StorageManagementClient(object):
    """The Azure Storage Management API.


    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.storage.v2019_06_01.operations.Operations
    :ivar skus: Skus operations
    :vartype skus: azure.mgmt.storage.v2019_06_01.operations.SkusOperations
    :ivar storage_accounts: StorageAccounts operations
    :vartype storage_accounts: azure.mgmt.storage.v2019_06_01.operations.StorageAccountsOperations
    :ivar usages: Usages operations
    :vartype usages: azure.mgmt.storage.v2019_06_01.operations.UsagesOperations
    :ivar management_policies: ManagementPolicies operations
    :vartype management_policies: azure.mgmt.storage.v2019_06_01.operations.ManagementPoliciesOperations
    :ivar private_endpoint_connections: PrivateEndpointConnections operations
    :vartype private_endpoint_connections: azure.mgmt.storage.v2019_06_01.operations.PrivateEndpointConnectionsOperations
    :ivar private_link_resources: PrivateLinkResources operations
    :vartype private_link_resources: azure.mgmt.storage.v2019_06_01.operations.PrivateLinkResourcesOperations
    :ivar blob_services: BlobServices operations
    :vartype blob_services: azure.mgmt.storage.v2019_06_01.operations.BlobServicesOperations
    :ivar blob_containers: BlobContainers operations
    :vartype blob_containers: azure.mgmt.storage.v2019_06_01.operations.BlobContainersOperations
    :ivar file_services: FileServices operations
    :vartype file_services: azure.mgmt.storage.v2019_06_01.operations.FileServicesOperations
    :ivar file_shares: FileShares operations
    :vartype file_shares: azure.mgmt.storage.v2019_06_01.operations.FileSharesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: The ID of the target subscription.
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None, **kwargs):

        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = StorageManagementClientConfiguration(credentials, subscription_id, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2019-06-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.skus = SkusOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.storage_accounts = StorageAccountsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.usages = UsagesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.management_policies = ManagementPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_endpoint_connections = PrivateEndpointConnectionsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.private_link_resources = PrivateLinkResourcesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_services = BlobServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.blob_containers = BlobContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_services = FileServicesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.file_shares = FileSharesOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def close(self):
        self._client.close()
    def __enter__(self):
        self._client.__enter__()
        return self
    def __exit__(self, *exc_details):
        self._client.__exit__(*exc_details)
