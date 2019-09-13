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

from msrest.serialization import Model
from msrest.exceptions import HttpOperationError


class Resource(Model):
    """Resource information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
    }

    def __init__(self, **kwargs):
        super(Resource, self).__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.location = kwargs.get('location', None)
        self.tags = kwargs.get('tags', None)


class GenericResource(Resource):
    """Resource information.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
    }

    def __init__(self, **kwargs):
        super(GenericResource, self).__init__(**kwargs)
        self.managed_by = kwargs.get('managed_by', None)
        self.sku = kwargs.get('sku', None)
        self.identity = kwargs.get('identity', None)


class Application(GenericResource):
    """Information about managed application.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    :param managed_resource_group_id: Required. The managed resource group Id.
    :type managed_resource_group_id: str
    :param application_definition_id: The fully qualified path of managed
     application definition Id.
    :type application_definition_id: str
    :param parameters: Name and value pairs that define the managed
     application parameters. It can be a JObject or a well formed JSON string.
    :type parameters: object
    :ivar outputs: Name and value pairs that define the managed application
     outputs.
    :vartype outputs: object
    :ivar provisioning_state: The managed application provisioning state.
     Possible values include: 'Accepted', 'Running', 'Ready', 'Creating',
     'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded',
     'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.managedapplications.models.ProvisioningState
    :param plan: The plan information.
    :type plan: ~azure.mgmt.resource.managedapplications.models.Plan
    :param kind: Required. The kind of the managed application. Allowed values
     are MarketPlace and ServiceCatalog.
    :type kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'managed_resource_group_id': {'required': True},
        'outputs': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'kind': {'required': True, 'pattern': r'^[-\w\._,\(\)]+$'},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'application_definition_id': {'key': 'properties.applicationDefinitionId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'outputs': {'key': 'properties.outputs', 'type': 'object'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'plan': {'key': 'plan', 'type': 'Plan'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Application, self).__init__(**kwargs)
        self.managed_resource_group_id = kwargs.get('managed_resource_group_id', None)
        self.application_definition_id = kwargs.get('application_definition_id', None)
        self.parameters = kwargs.get('parameters', None)
        self.outputs = None
        self.provisioning_state = None
        self.plan = kwargs.get('plan', None)
        self.kind = kwargs.get('kind', None)


class ApplicationArtifact(Model):
    """Managed application artifact.

    :param name: The managed application artifact name.
    :type name: str
    :param uri: The managed application artifact blob uri.
    :type uri: str
    :param type: The managed application artifact type. Possible values
     include: 'Template', 'Custom'
    :type type: str or
     ~azure.mgmt.resource.managedapplications.models.ApplicationArtifactType
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'uri': {'key': 'uri', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ApplicationArtifactType'},
    }

    def __init__(self, **kwargs):
        super(ApplicationArtifact, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.uri = kwargs.get('uri', None)
        self.type = kwargs.get('type', None)


class ApplicationDefinition(GenericResource):
    """Information about managed application definition.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    :param lock_level: Required. The managed application lock level. Possible
     values include: 'CanNotDelete', 'ReadOnly', 'None'
    :type lock_level: str or
     ~azure.mgmt.resource.managedapplications.models.ApplicationLockLevel
    :param display_name: The managed application definition display name.
    :type display_name: str
    :param is_enabled: A value indicating whether the package is enabled or
     not.
    :type is_enabled: str
    :param authorizations: Required. The managed application provider
     authorizations.
    :type authorizations:
     list[~azure.mgmt.resource.managedapplications.models.ApplicationProviderAuthorization]
    :param artifacts: The collection of managed application artifacts. The
     portal will use the files specified as artifacts to construct the user
     experience of creating a managed application from a managed application
     definition.
    :type artifacts:
     list[~azure.mgmt.resource.managedapplications.models.ApplicationArtifact]
    :param description: The managed application definition description.
    :type description: str
    :param package_file_uri: The managed application definition package file
     Uri. Use this element
    :type package_file_uri: str
    :param main_template: The inline main template json which has resources to
     be provisioned. It can be a JObject or well-formed JSON string.
    :type main_template: object
    :param create_ui_definition: The createUiDefinition json for the backing
     template with Microsoft.Solutions/applications resource. It can be a
     JObject or well-formed JSON string.
    :type create_ui_definition: object
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'lock_level': {'required': True},
        'authorizations': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'lock_level': {'key': 'properties.lockLevel', 'type': 'ApplicationLockLevel'},
        'display_name': {'key': 'properties.displayName', 'type': 'str'},
        'is_enabled': {'key': 'properties.isEnabled', 'type': 'str'},
        'authorizations': {'key': 'properties.authorizations', 'type': '[ApplicationProviderAuthorization]'},
        'artifacts': {'key': 'properties.artifacts', 'type': '[ApplicationArtifact]'},
        'description': {'key': 'properties.description', 'type': 'str'},
        'package_file_uri': {'key': 'properties.packageFileUri', 'type': 'str'},
        'main_template': {'key': 'properties.mainTemplate', 'type': 'object'},
        'create_ui_definition': {'key': 'properties.createUiDefinition', 'type': 'object'},
    }

    def __init__(self, **kwargs):
        super(ApplicationDefinition, self).__init__(**kwargs)
        self.lock_level = kwargs.get('lock_level', None)
        self.display_name = kwargs.get('display_name', None)
        self.is_enabled = kwargs.get('is_enabled', None)
        self.authorizations = kwargs.get('authorizations', None)
        self.artifacts = kwargs.get('artifacts', None)
        self.description = kwargs.get('description', None)
        self.package_file_uri = kwargs.get('package_file_uri', None)
        self.main_template = kwargs.get('main_template', None)
        self.create_ui_definition = kwargs.get('create_ui_definition', None)


class ApplicationPatchable(GenericResource):
    """Information about managed application.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID
    :vartype id: str
    :ivar name: Resource name
    :vartype name: str
    :ivar type: Resource type
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param managed_by: ID of the resource that manages this resource.
    :type managed_by: str
    :param sku: The SKU of the resource.
    :type sku: ~azure.mgmt.resource.managedapplications.models.Sku
    :param identity: The identity of the resource.
    :type identity: ~azure.mgmt.resource.managedapplications.models.Identity
    :param managed_resource_group_id: The managed resource group Id.
    :type managed_resource_group_id: str
    :param application_definition_id: The fully qualified path of managed
     application definition Id.
    :type application_definition_id: str
    :param parameters: Name and value pairs that define the managed
     application parameters. It can be a JObject or a well formed JSON string.
    :type parameters: object
    :ivar outputs: Name and value pairs that define the managed application
     outputs.
    :vartype outputs: object
    :ivar provisioning_state: The managed application provisioning state.
     Possible values include: 'Accepted', 'Running', 'Ready', 'Creating',
     'Created', 'Deleting', 'Deleted', 'Canceled', 'Failed', 'Succeeded',
     'Updating'
    :vartype provisioning_state: str or
     ~azure.mgmt.resource.managedapplications.models.ProvisioningState
    :param plan: The plan information.
    :type plan: ~azure.mgmt.resource.managedapplications.models.PlanPatchable
    :param kind: The kind of the managed application. Allowed values are
     MarketPlace and ServiceCatalog.
    :type kind: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'outputs': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'kind': {'pattern': r'^[-\w\._,\(\)]+$'},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'managed_by': {'key': 'managedBy', 'type': 'str'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'identity': {'key': 'identity', 'type': 'Identity'},
        'managed_resource_group_id': {'key': 'properties.managedResourceGroupId', 'type': 'str'},
        'application_definition_id': {'key': 'properties.applicationDefinitionId', 'type': 'str'},
        'parameters': {'key': 'properties.parameters', 'type': 'object'},
        'outputs': {'key': 'properties.outputs', 'type': 'object'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'plan': {'key': 'plan', 'type': 'PlanPatchable'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationPatchable, self).__init__(**kwargs)
        self.managed_resource_group_id = kwargs.get('managed_resource_group_id', None)
        self.application_definition_id = kwargs.get('application_definition_id', None)
        self.parameters = kwargs.get('parameters', None)
        self.outputs = None
        self.provisioning_state = None
        self.plan = kwargs.get('plan', None)
        self.kind = kwargs.get('kind', None)


class ApplicationProviderAuthorization(Model):
    """The managed application provider authorization.

    All required parameters must be populated in order to send to Azure.

    :param principal_id: Required. The provider's principal identifier. This
     is the identity that the provider will use to call ARM to manage the
     managed application resources.
    :type principal_id: str
    :param role_definition_id: Required. The provider's role definition
     identifier. This role will define all the permissions that the provider
     must have on the managed application's container resource group. This role
     definition cannot have permission to delete the resource group.
    :type role_definition_id: str
    """

    _validation = {
        'principal_id': {'required': True},
        'role_definition_id': {'required': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'role_definition_id': {'key': 'roleDefinitionId', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ApplicationProviderAuthorization, self).__init__(**kwargs)
        self.principal_id = kwargs.get('principal_id', None)
        self.role_definition_id = kwargs.get('role_definition_id', None)


class CloudError(Model):
    """CloudError.
    """

    _attribute_map = {
    }


class ErrorResponse(Model):
    """Error response indicates managed application is not able to process the
    incoming request. The reason is provided in the error message.

    :param http_status: Http status code.
    :type http_status: str
    :param error_code: Error code.
    :type error_code: str
    :param error_message: Error message indicating why the operation failed.
    :type error_message: str
    """

    _attribute_map = {
        'http_status': {'key': 'httpStatus', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'str'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ErrorResponse, self).__init__(**kwargs)
        self.http_status = kwargs.get('http_status', None)
        self.error_code = kwargs.get('error_code', None)
        self.error_message = kwargs.get('error_message', None)


class ErrorResponseException(HttpOperationError):
    """Server responsed with exception of type: 'ErrorResponse'.

    :param deserialize: A deserializer
    :param response: Server response to be deserialized.
    """

    def __init__(self, deserialize, response, *args):

        super(ErrorResponseException, self).__init__(deserialize, response, 'ErrorResponse', *args)


class Identity(Model):
    """Identity for the resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar principal_id: The principal ID of resource identity.
    :vartype principal_id: str
    :ivar tenant_id: The tenant ID of resource.
    :vartype tenant_id: str
    :param type: The identity type. Possible values include: 'SystemAssigned'
    :type type: str or
     ~azure.mgmt.resource.managedapplications.models.ResourceIdentityType
    """

    _validation = {
        'principal_id': {'readonly': True},
        'tenant_id': {'readonly': True},
    }

    _attribute_map = {
        'principal_id': {'key': 'principalId', 'type': 'str'},
        'tenant_id': {'key': 'tenantId', 'type': 'str'},
        'type': {'key': 'type', 'type': 'ResourceIdentityType'},
    }

    def __init__(self, **kwargs):
        super(Identity, self).__init__(**kwargs)
        self.principal_id = None
        self.tenant_id = None
        self.type = kwargs.get('type', None)


class Plan(Model):
    """Plan for the managed application.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The plan name.
    :type name: str
    :param publisher: Required. The publisher ID.
    :type publisher: str
    :param product: Required. The product code.
    :type product: str
    :param promotion_code: The promotion code.
    :type promotion_code: str
    :param version: Required. The plan's version.
    :type version: str
    """

    _validation = {
        'name': {'required': True},
        'publisher': {'required': True},
        'product': {'required': True},
        'version': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Plan, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.publisher = kwargs.get('publisher', None)
        self.product = kwargs.get('product', None)
        self.promotion_code = kwargs.get('promotion_code', None)
        self.version = kwargs.get('version', None)


class PlanPatchable(Model):
    """Plan for the managed application.

    :param name: The plan name.
    :type name: str
    :param publisher: The publisher ID.
    :type publisher: str
    :param product: The product code.
    :type product: str
    :param promotion_code: The promotion code.
    :type promotion_code: str
    :param version: The plan's version.
    :type version: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'publisher': {'key': 'publisher', 'type': 'str'},
        'product': {'key': 'product', 'type': 'str'},
        'promotion_code': {'key': 'promotionCode', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PlanPatchable, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.publisher = kwargs.get('publisher', None)
        self.product = kwargs.get('product', None)
        self.promotion_code = kwargs.get('promotion_code', None)
        self.version = kwargs.get('version', None)


class Sku(Model):
    """SKU for the resource.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The SKU name.
    :type name: str
    :param tier: The SKU tier.
    :type tier: str
    :param size: The SKU size.
    :type size: str
    :param family: The SKU family.
    :type family: str
    :param model: The SKU model.
    :type model: str
    :param capacity: The SKU capacity.
    :type capacity: int
    """

    _validation = {
        'name': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'tier': {'key': 'tier', 'type': 'str'},
        'size': {'key': 'size', 'type': 'str'},
        'family': {'key': 'family', 'type': 'str'},
        'model': {'key': 'model', 'type': 'str'},
        'capacity': {'key': 'capacity', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(Sku, self).__init__(**kwargs)
        self.name = kwargs.get('name', None)
        self.tier = kwargs.get('tier', None)
        self.size = kwargs.get('size', None)
        self.family = kwargs.get('family', None)
        self.model = kwargs.get('model', None)
        self.capacity = kwargs.get('capacity', None)
