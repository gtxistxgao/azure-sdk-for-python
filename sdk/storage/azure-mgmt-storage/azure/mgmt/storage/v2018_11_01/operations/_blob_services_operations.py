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

import uuid
from azure.core.exceptions import map_error
from azure.mgmt.core.exceptions import ARMError

from .. import models


class BlobServicesOperations(object):
    """BlobServicesOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: The API version to use for this operation. Constant value: "2018-11-01".
    :ivar blob_services_name: The name of the blob Service within the specified storage account. Blob Service Name must be 'default'. Constant value: "default".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2018-11-01"
        self.blob_services_name = "default"

        self._config = config

    def set_service_properties(self, resource_group_name, account_name, parameters, cls=None, **kwargs):
        """Sets the properties of a storage account’s Blob service, including
        properties for Storage Analytics and CORS (Cross-Origin Resource
        Sharing) rules. .

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param parameters: The properties of a storage account’s Blob service,
         including properties for Storage Analytics and CORS (Cross-Origin
         Resource Sharing) rules.
        :type parameters:
         ~azure.mgmt.storage.v2018_11_01.models.BlobServiceProperties
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: BlobServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2018_11_01.models.BlobServiceProperties
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.set_service_properties.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'BlobServicesName': self._serialize.url("self.blob_services_name", self.blob_services_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

        # Construct body
        body_content = self._serialize.body(parameters, 'BlobServiceProperties')

        # Construct and send request
        request = self._client.put(url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BlobServiceProperties', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    set_service_properties.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName}'}

    def get_service_properties(self, resource_group_name, account_name, cls=None, **kwargs):
        """Gets the properties of a storage account’s Blob service, including
        properties for Storage Analytics and CORS (Cross-Origin Resource
        Sharing) rules.

        :param resource_group_name: The name of the resource group within the
         user's subscription. The name is case insensitive.
        :type resource_group_name: str
        :param account_name: The name of the storage account within the
         specified resource group. Storage account names must be between 3 and
         24 characters in length and use numbers and lower-case letters only.
        :type account_name: str
        :param callable cls: A custom type or function that will be passed the
         direct response
        :return: BlobServiceProperties or the result of cls(response)
        :rtype: ~azure.mgmt.storage.v2018_11_01.models.BlobServiceProperties
        :raises: :class:`ARMError<azure.mgmt.core.ARMError>`
        """
        error_map = kwargs.pop('error_map', None)
        # Construct URL
        url = self.get_service_properties.metadata['url']
        path_format_arguments = {
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str', max_length=90, min_length=1, pattern=r'^[-\w\._\(\)]+$'),
            'accountName': self._serialize.url("account_name", account_name, 'str', max_length=24, min_length=3),
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'BlobServicesName': self._serialize.url("self.blob_services_name", self.blob_services_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str', min_length=1)

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self._config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise ARMError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('BlobServiceProperties', response)

        if cls:
            return cls(response, deserialized, None)

        return deserialized
    get_service_properties.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Storage/storageAccounts/{accountName}/blobServices/{BlobServicesName}'}
