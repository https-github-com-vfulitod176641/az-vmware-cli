# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .tracked_resource_py3 import TrackedResource


class PrivateCloud(TrackedResource):
    """A private cloud resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :param location: Resource location
    :type location: str
    :param tags: Resource tags
    :type tags: dict[str, str]
    :param sku: The private cloud SKU
    :type sku: ~vendored_sdks.models.Sku
    :ivar provisioning_state: The provisioning state. Possible values include:
     'Succeeded', 'Failed', 'Cancelled', 'Pending', 'Building', 'Deleting',
     'Updating'
    :vartype provisioning_state: str or
     ~vendored_sdks.models.PrivateCloudProvisioningState
    :param circuit: An ExpressRoute Circuit
    :type circuit: ~vendored_sdks.models.Circuit
    :param management_cluster: The default cluster used for management
    :type management_cluster: ~vendored_sdks.models.DefaultClusterProperties
    :ivar endpoints: The endpoints
    :vartype endpoints: ~vendored_sdks.models.Endpoints
    :param internet: Connectivity to internet is enabled or disabled. Possible
     values include: 'Enabled', 'Disabled'
    :type internet: str or ~vendored_sdks.models.InternetEnum
    :param identity_sources: vCenter Single Sign On Identity Sources
    :type identity_sources: list[~vendored_sdks.models.IdentitySource]
    :param network_block: The block of addresses should be unique across VNet
     in your subscription as well as on-premise. Make sure the CIDR format is
     conformed to (A.B.C.D/X) where A,B,C,D are between 0 and 255, and X is
     between 0 and 22
    :type network_block: str
    :ivar management_network: Network used to access vCenter Server and NSX-T
     Manager
    :vartype management_network: str
    :ivar provisioning_network: Used for virtual machine cold migration,
     cloning, and snapshot migration
    :vartype provisioning_network: str
    :ivar vmotion_network: Used for live migration of virtual machines
    :vartype vmotion_network: str
    :param vcenter_password: Optionally, set the vCenter admin password when
     the private cloud is created
    :type vcenter_password: str
    :param nsxt_password: Optionally, set the NSX-T Manager password when the
     private cloud is created
    :type nsxt_password: str
    :ivar vcenter_certificate_thumbprint: Thumbprint of the vCenter Server SSL
     certificate
    :vartype vcenter_certificate_thumbprint: str
    :ivar nsxt_certificate_thumbprint: Thumbprint of the NSX-T Manager SSL
     certificate
    :vartype nsxt_certificate_thumbprint: str
    :ivar hcx_cloud_manager_ip: The IP address of the HCX Cloud Manager
    :vartype hcx_cloud_manager_ip: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'provisioning_state': {'readonly': True},
        'endpoints': {'readonly': True},
        'management_network': {'readonly': True},
        'provisioning_network': {'readonly': True},
        'vmotion_network': {'readonly': True},
        'vcenter_certificate_thumbprint': {'readonly': True},
        'nsxt_certificate_thumbprint': {'readonly': True},
        'hcx_cloud_manager_ip': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'sku': {'key': 'sku', 'type': 'Sku'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'circuit': {'key': 'properties.circuit', 'type': 'Circuit'},
        'management_cluster': {'key': 'properties.managementCluster', 'type': 'DefaultClusterProperties'},
        'endpoints': {'key': 'properties.endpoints', 'type': 'Endpoints'},
        'internet': {'key': 'properties.internet', 'type': 'str'},
        'identity_sources': {'key': 'properties.identitySources', 'type': '[IdentitySource]'},
        'network_block': {'key': 'properties.networkBlock', 'type': 'str'},
        'management_network': {'key': 'properties.managementNetwork', 'type': 'str'},
        'provisioning_network': {'key': 'properties.provisioningNetwork', 'type': 'str'},
        'vmotion_network': {'key': 'properties.vmotionNetwork', 'type': 'str'},
        'vcenter_password': {'key': 'properties.vcenterPassword', 'type': 'str'},
        'nsxt_password': {'key': 'properties.nsxtPassword', 'type': 'str'},
        'vcenter_certificate_thumbprint': {'key': 'properties.vcenterCertificateThumbprint', 'type': 'str'},
        'nsxt_certificate_thumbprint': {'key': 'properties.nsxtCertificateThumbprint', 'type': 'str'},
        'hcx_cloud_manager_ip': {'key': 'properties.hcxCloudManagerIP', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, sku=None, circuit=None, management_cluster=None, internet=None, identity_sources=None, network_block: str=None, vcenter_password: str=None, nsxt_password: str=None, **kwargs) -> None:
        super(PrivateCloud, self).__init__(location=location, tags=tags, **kwargs)
        self.sku = sku
        self.provisioning_state = None
        self.circuit = circuit
        self.management_cluster = management_cluster
        self.endpoints = None
        self.internet = internet
        self.identity_sources = identity_sources
        self.network_block = network_block
        self.management_network = None
        self.provisioning_network = None
        self.vmotion_network = None
        self.vcenter_password = vcenter_password
        self.nsxt_password = nsxt_password
        self.vcenter_certificate_thumbprint = None
        self.nsxt_certificate_thumbprint = None
        self.hcx_cloud_manager_ip = None
