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
from msrest.pipeline import ClientRawResponse

from .. import models


class ProblemClassificationsOperations(object):
    """ProblemClassificationsOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Api version. Constant value: "2019-05-01-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2019-05-01-preview"

        self.config = config

    def list(
            self, service_name, custom_headers=None, raw=False, **operation_config):
        """Lists all the problem classifications (categories) available for a
        specific Azure service.<br/><br/> Always use the service and problem
        classifications obtained programmatically. This practice ensures that
        you always have the most recent set of service and problem
        classification Ids.

        :param service_name: Name of Azure service for which the problem
         classifications need to be retrieved.
        :type service_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of ProblemClassification
        :rtype:
         ~azure.mgmt.support.models.ProblemClassificationPaged[~azure.mgmt.support.models.ProblemClassification]
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.support.models.ExceptionResponseException>`
        """
        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'serviceName': self._serialize.url("service_name", service_name, 'str')
                }
                url = self._client.format_url(url, **path_format_arguments)

                # Construct parameters
                query_parameters = {}
                query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

            else:
                url = next_link
                query_parameters = {}

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'
            if self.config.generate_client_request_id:
                header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
            if custom_headers:
                header_parameters.update(custom_headers)
            if self.config.accept_language is not None:
                header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

            # Construct and send request
            request = self._client.get(url, query_parameters, header_parameters)
            return request

        def internal_paging(next_link=None):
            request = prepare_request(next_link)

            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ExceptionResponseException(self._deserialize, response)

            return response

        # Deserialize response
        header_dict = None
        if raw:
            header_dict = {}
        deserialized = models.ProblemClassificationPaged(internal_paging, self._deserialize.dependencies, header_dict)

        return deserialized
    list.metadata = {'url': '/providers/Microsoft.Support/services/{serviceName}/problemClassifications'}

    def get(
            self, service_name, problem_classification_name, custom_headers=None, raw=False, **operation_config):
        """Gets the details of a specific problem classification for a specific
        Azure service.

        :param service_name: Name of Azure service available for support.
        :type service_name: str
        :param problem_classification_name: Name of problem classification.
        :type problem_classification_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ProblemClassification or ClientRawResponse if raw=true
        :rtype: ~azure.mgmt.support.models.ProblemClassification or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ExceptionResponseException<azure.mgmt.support.models.ExceptionResponseException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'serviceName': self._serialize.url("service_name", service_name, 'str'),
            'problemClassificationName': self._serialize.url("problem_classification_name", problem_classification_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200]:
            raise models.ExceptionResponseException(self._deserialize, response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('ProblemClassification', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/providers/Microsoft.Support/services/{serviceName}/problemClassifications/{problemClassificationName}'}
