from typing import *

from cognite.client.data_classes._base import *


class DataModelStorageSpace(CogniteResource):
    """No description.

    Args:
        external_id (str): The external ID provided by the client. Must be unique for the resource type.
        cognite_client (CogniteClient): The client to associate with this object.
    """

    def __init__(
        self,
        external_id: str = None,
        cognite_client=None,
    ):
        self.external_id = external_id
        self._cognite_client = cognite_client


class DataModelStorageSpaceList(CogniteResourceList):
    _RESOURCE = DataModelStorageSpace
    _UPDATE = None
    _ASSERT_CLASSES = False
