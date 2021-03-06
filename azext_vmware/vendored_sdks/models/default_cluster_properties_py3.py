# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DefaultClusterProperties(Model):
    """The properties of a default cluster.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar cluster_id: The identity
    :vartype cluster_id: int
    :param cluster_size: The cluster size
    :type cluster_size: int
    :ivar hosts: The hosts
    :vartype hosts: list[str]
    """

    _validation = {
        'cluster_id': {'readonly': True},
        'hosts': {'readonly': True},
    }

    _attribute_map = {
        'cluster_id': {'key': 'clusterId', 'type': 'int'},
        'cluster_size': {'key': 'clusterSize', 'type': 'int'},
        'hosts': {'key': 'hosts', 'type': '[str]'},
    }

    def __init__(self, *, cluster_size: int=None, **kwargs) -> None:
        super(DefaultClusterProperties, self).__init__(**kwargs)
        self.cluster_id = None
        self.cluster_size = cluster_size
        self.hosts = None
