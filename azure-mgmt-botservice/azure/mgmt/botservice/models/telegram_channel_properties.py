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


class TelegramChannelProperties(Model):
    """The parameters to provide for the Telegram channel.

    :param access_token: The Telegram access token
    :type access_token: str
    :param is_validated: Whether this channel is validated for the bot
    :type is_validated: bool
    :param is_enabled: Whether this channel is enabled for the bot
    :type is_enabled: bool
    """

    _validation = {
        'access_token': {'required': True},
        'is_enabled': {'required': True},
    }

    _attribute_map = {
        'access_token': {'key': 'accessToken', 'type': 'str'},
        'is_validated': {'key': 'isValidated', 'type': 'bool'},
        'is_enabled': {'key': 'isEnabled', 'type': 'bool'},
    }

    def __init__(self, access_token, is_enabled, is_validated=None):
        self.access_token = access_token
        self.is_validated = is_validated
        self.is_enabled = is_enabled
