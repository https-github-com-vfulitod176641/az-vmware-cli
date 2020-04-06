# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .resource import Resource


class Cluster(Resource):
    """A cluster resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource ID.
    :vartype id: str
    :ivar name: Resource name.
    :vartype name: str
    :ivar type: Resource type.
    :vartype type: str
    :ivar cluster_id: The identity
    :vartype cluster_id: int
    :param cluster_size: The cluster size
    :type cluster_size: int
    :ivar hosts: The hosts
    :vartype hosts: list[str]
    :ivar provisioning_state: The state of the cluster provisioning. Possible
     values include: 'Succeeded', 'Failed', 'Cancelled', 'Deleting', 'Updating'
    :vartype provisioning_state: str or
     ~vendored_sdks.models.ClusterProvisioningState
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'cluster_id': {'readonly': True},
        'hosts': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'cluster_id': {'key': 'properties.clusterId', 'type': 'int'},
        'cluster_size': {'key': 'properties.clusterSize', 'type': 'int'},
        'hosts': {'key': 'properties.hosts', 'type': '[str]'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(Cluster, self).__init__(**kwargs)
        self.cluster_id = None
        self.cluster_size = kwargs.get('cluster_size', None)
        self.hosts = None
        self.provisioning_state = None
