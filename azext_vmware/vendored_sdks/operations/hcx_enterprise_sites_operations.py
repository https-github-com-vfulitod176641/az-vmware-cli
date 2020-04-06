# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

import uuid
from msrest.pipeline import ClientRawResponse
from msrest.polling import LROPoller, NoPolling
from msrestazure.polling.arm_polling import ARMPolling

from .. import models


class HcxEnterpriseSitesOperations(object):
    """HcxEnterpriseSitesOperations operations.

    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    :ivar api_version: Version of Azure VMware Solution by Virtustream API to be used with the client request. Constant value: "2020-03-20-preview".
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self.api_version = "2020-03-20-preview"

        self.config = config

    def list(
            self, resource_group_name, private_cloud_name, custom_headers=None, raw=False, **operation_config):
        """List HCX Enterprise Sites in a private cloud.

        :param resource_group_name: Name of the resource group within the
         Azure subscription
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud
        :type private_cloud_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: An iterator like instance of HcxEnterpriseSite
        :rtype:
         ~vendored_sdks.models.HcxEnterpriseSitePaged[~vendored_sdks.models.HcxEnterpriseSite]
        :raises:
         :class:`ApiErrorException<vendored_sdks.models.ApiErrorException>`
        """
        def internal_paging(next_link=None, raw=False):

            if not next_link:
                # Construct URL
                url = self.list.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                    'privateCloudName': self._serialize.url("private_cloud_name", private_cloud_name, 'str')
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
            response = self._client.send(request, stream=False, **operation_config)

            if response.status_code not in [200]:
                raise models.ApiErrorException(self._deserialize, response)

            return response

        # Deserialize response
        deserialized = models.HcxEnterpriseSitePaged(internal_paging, self._deserialize.dependencies)

        if raw:
            header_dict = {}
            client_raw_response = models.HcxEnterpriseSitePaged(internal_paging, self._deserialize.dependencies, header_dict)
            return client_raw_response

        return deserialized
    list.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareVirtustream/privateClouds/{privateCloudName}/hcxEnterpriseSites'}

    def get(
            self, resource_group_name, private_cloud_name, hcx_enterprise_site_name, custom_headers=None, raw=False, **operation_config):
        """Get an HCX Enterprise Site by name in a private cloud.

        :param resource_group_name: Name of the resource group within the
         Azure subscription
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in
         the private cloud
        :type hcx_enterprise_site_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: HcxEnterpriseSite or ClientRawResponse if raw=true
        :rtype: ~vendored_sdks.models.HcxEnterpriseSite or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`ApiErrorException<vendored_sdks.models.ApiErrorException>`
        """
        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'privateCloudName': self._serialize.url("private_cloud_name", private_cloud_name, 'str'),
            'hcxEnterpriseSiteName': self._serialize.url("hcx_enterprise_site_name", hcx_enterprise_site_name, 'str')
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
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('HcxEnterpriseSite', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized
    get.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareVirtustream/privateClouds/{privateCloudName}/hcxEnterpriseSites/{hcxEnterpriseSiteName}'}


    def _create_or_update_initial(
            self, resource_group_name, private_cloud_name, hcx_enterprise_site_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'privateCloudName': self._serialize.url("private_cloud_name", private_cloud_name, 'str'),
            'hcxEnterpriseSiteName': self._serialize.url("hcx_enterprise_site_name", hcx_enterprise_site_name, 'str')
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
        request = self._client.put(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 201]:
            raise models.ApiErrorException(self._deserialize, response)

        deserialized = None

        if response.status_code == 200:
            deserialized = self._deserialize('HcxEnterpriseSite', response)
        if response.status_code == 201:
            deserialized = self._deserialize('HcxEnterpriseSite', response)

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            return client_raw_response

        return deserialized

    def create_or_update(
            self, resource_group_name, private_cloud_name, hcx_enterprise_site_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Create or update an HCX Enterprise Site in a private cloud.

        :param resource_group_name: Name of the resource group within the
         Azure subscription
        :type resource_group_name: str
        :param private_cloud_name: The name of the private cloud.
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in
         the private cloud
        :type hcx_enterprise_site_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns HcxEnterpriseSite or
         ClientRawResponse<HcxEnterpriseSite> if raw==True
        :rtype:
         ~msrestazure.azure_operation.AzureOperationPoller[~vendored_sdks.models.HcxEnterpriseSite]
         or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[~vendored_sdks.models.HcxEnterpriseSite]]
        :raises:
         :class:`ApiErrorException<vendored_sdks.models.ApiErrorException>`
        """
        raw_result = self._create_or_update_initial(
            resource_group_name=resource_group_name,
            private_cloud_name=private_cloud_name,
            hcx_enterprise_site_name=hcx_enterprise_site_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            deserialized = self._deserialize('HcxEnterpriseSite', response)

            if raw:
                client_raw_response = ClientRawResponse(deserialized, response)
                return client_raw_response

            return deserialized

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    create_or_update.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareVirtustream/privateClouds/{privateCloudName}/hcxEnterpriseSites/{hcxEnterpriseSiteName}'}


    def _delete_initial(
            self, resource_group_name, private_cloud_name, hcx_enterprise_site_name, custom_headers=None, raw=False, **operation_config):
        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self.config.subscription_id", self.config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'privateCloudName': self._serialize.url("private_cloud_name", private_cloud_name, 'str'),
            'hcxEnterpriseSiteName': self._serialize.url("hcx_enterprise_site_name", hcx_enterprise_site_name, 'str')
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query("self.api_version", self.api_version, 'str')

        # Construct headers
        header_parameters = {}
        if self.config.generate_client_request_id:
            header_parameters['x-ms-client-request-id'] = str(uuid.uuid1())
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.accept_language is not None:
            header_parameters['accept-language'] = self._serialize.header("self.config.accept_language", self.config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        response = self._client.send(request, stream=False, **operation_config)

        if response.status_code not in [200, 202, 204]:
            raise models.ApiErrorException(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            return client_raw_response

    def delete(
            self, resource_group_name, private_cloud_name, hcx_enterprise_site_name, custom_headers=None, raw=False, polling=True, **operation_config):
        """Delete an HCX Enterprise Site in a private cloud.

        :param resource_group_name: Name of the resource group within the
         Azure subscription
        :type resource_group_name: str
        :param private_cloud_name: Name of the private cloud
        :type private_cloud_name: str
        :param hcx_enterprise_site_name: Name of the HCX Enterprise Site in
         the private cloud
        :type hcx_enterprise_site_name: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: The poller return type is ClientRawResponse, the
         direct response alongside the deserialized response
        :param polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :return: An instance of LROPoller that returns None or
         ClientRawResponse<None> if raw==True
        :rtype: ~msrestazure.azure_operation.AzureOperationPoller[None] or
         ~msrestazure.azure_operation.AzureOperationPoller[~msrest.pipeline.ClientRawResponse[None]]
        :raises:
         :class:`ApiErrorException<vendored_sdks.models.ApiErrorException>`
        """
        raw_result = self._delete_initial(
            resource_group_name=resource_group_name,
            private_cloud_name=private_cloud_name,
            hcx_enterprise_site_name=hcx_enterprise_site_name,
            custom_headers=custom_headers,
            raw=True,
            **operation_config
        )

        def get_long_running_output(response):
            if raw:
                client_raw_response = ClientRawResponse(None, response)
                return client_raw_response

        lro_delay = operation_config.get(
            'long_running_operation_timeout',
            self.config.long_running_operation_timeout)
        if polling is True: polling_method = ARMPolling(lro_delay, **operation_config)
        elif polling is False: polling_method = NoPolling()
        else: polling_method = polling
        return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    delete.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.VMwareVirtustream/privateClouds/{privateCloudName}/hcxEnterpriseSites/{hcxEnterpriseSiteName}'}
