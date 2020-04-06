# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.operations import Operations
from .operations.private_clouds_operations import PrivateCloudsOperations
from .operations.clusters_operations import ClustersOperations
from .operations.identity_sources_operations import IdentitySourcesOperations
from .operations.hcx_enterprise_sites_operations import HcxEnterpriseSitesOperations
from . import models


class VirtustreamClientConfiguration(AzureConfiguration):
    """Configuration for VirtustreamClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Unique identifier for the Azure subscription
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if subscription_id is None:
            raise ValueError("Parameter 'subscription_id' must not be None.")
        if not base_url:
            base_url = 'https://management.azure.com'

        super(VirtustreamClientConfiguration, self).__init__(base_url)

        self.add_user_agent('virtustreamclient/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials
        self.subscription_id = subscription_id


class VirtustreamClient(SDKClient):
    """Azure VMware Solution by Virtustream API

    :ivar config: Configuration for client.
    :vartype config: VirtustreamClientConfiguration

    :ivar operations: Operations operations
    :vartype operations: vendored_sdks.operations.Operations
    :ivar private_clouds: PrivateClouds operations
    :vartype private_clouds: vendored_sdks.operations.PrivateCloudsOperations
    :ivar clusters: Clusters operations
    :vartype clusters: vendored_sdks.operations.ClustersOperations
    :ivar identity_sources: IdentitySources operations
    :vartype identity_sources: vendored_sdks.operations.IdentitySourcesOperations
    :ivar hcx_enterprise_sites: HcxEnterpriseSites operations
    :vartype hcx_enterprise_sites: vendored_sdks.operations.HcxEnterpriseSitesOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Unique identifier for the Azure subscription
    :type subscription_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, base_url=None):

        self.config = VirtustreamClientConfiguration(credentials, subscription_id, base_url)
        super(VirtustreamClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2020-03-20-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
        self.private_clouds = PrivateCloudsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.clusters = ClustersOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.identity_sources = IdentitySourcesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.hcx_enterprise_sites = HcxEnterpriseSitesOperations(
            self._client, self.config, self._serialize, self._deserialize)
