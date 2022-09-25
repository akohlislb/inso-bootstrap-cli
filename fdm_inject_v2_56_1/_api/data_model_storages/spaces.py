from typing import *

from cognite.client import utils
from cognite.client._api_client import APIClient
from fdm_inject_v2_56_1.data_classes.data_model_storages.spaces import (
# from cognite.client.data_classes.data_model_storages.spaces import (
    DataModelStorageSpace,
    DataModelStorageSpaceList,
)

class DataModelStorageSpacesAPI(APIClient):
    _RESOURCE_PATH = "/datamodelstorage/spaces"
    _LIST_CLASS = DataModelStorageSpaceList

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._CREATE_LIMIT = 100

    def __call__(
        self,
        chunk_size: int = None,
        limit: int = None,
    ) -> Generator[Union[DataModelStorageSpace, DataModelStorageSpaceList], None, None]:
        """Iterate over spaces

        Fetches spaces as they are iterated over, so you keep a limited number of spaces in memory.

        Args:
            chunk_size (int, optional): Number of spaces to return in each chunk. Defaults to yielding one data set a time.
            limit (int, optional): Maximum number of spaces to return. Defaults to return all items.

        Yields:
            Union[DataModelStorageSpace, DataModelStorageSpaceList]: yields DataModelStorageSpace one by one if chunk is not specified, else DataModelStorageSpaceList objects.
        """
        filter = None
        # filter = DataModelStorageSpaceFilter(
        #     metadata=metadata,
        #     created_time=created_time,
        #     last_updated_time=last_updated_time,
        #     external_id_prefix=external_id_prefix,
        #     write_protected=write_protected,
        # ).dump(camel_case=True)
        return self._list_generator(method="POST", chunk_size=chunk_size, filter=filter, limit=limit)

    def __iter__(self) -> Generator[DataModelStorageSpace, None, None]:
        """Iterate over spaces

        Fetches spaces as they are iterated over, so you keep a limited number of spaces in memory.

        Yields:
            Event: yields DataModelStorageSpace one by one.
        """
        return self.__call__()

    def create(self, space: Union[DataModelStorageSpace, List[DataModelStorageSpace]]) -> Union[DataModelStorageSpace, DataModelStorageSpaceList]:
        """`Create one or more spaces. <https://docs.cognite.com/api/v1/#operation/createDataModelStorageSpaces>`_

        Args:
            space: Union[DataModelStorageSpace, List[DataModelStorageSpace]]: Data set or list of spaces to create.

        Returns:
            Union[DataModelStorageSpace, DataModelStorageSpaceList]: Created data set(s)

        Examples:

            Create new spaces::

                >>> from cognite.client import CogniteClient
                >>> from cognite.client.data_model_storage import DataModelStorageSpace
                >>> c = CogniteClient()
                >>> space = [DataModelStorageSpace(external_id="1st level"), DataModelStorageSpace(external_id="2nd level")]
                >>> res = c.data_model_storages.spaces.create(space)
        """
        return self._create_multiple(items=space)

    def retrieve(self, external_id: Optional[str] = None) -> Optional[DataModelStorageSpace]:
        """`Retrieve a single data set by id. <https://docs.cognite.com/api/v1/#operation/getDataModelStorageSpaces>`_

        Args:
            id (int, optional): ID
            external_id (str, optional): External ID

        Returns:
            Optional[DataModelStorageSpace]: Requested data set or None if it does not exist.

        Examples:

            Get space by external id::

                >>> from cognite.client import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.spaces.retrieve(external_id="1")
        """
        # utils._auxiliary.assert_exactly_one_of_id_or_external_id(id, external_id)
        return self._retrieve_multiple(external_ids=external_id, wrap_ids=False)

    def retrieve_multiple(self, external_ids: Optional[List[str]] = None) -> DataModelStorageSpaceList:
        """`Retrieve multiple spaces by id. <https://docs.cognite.com/api/v1/#operation/getDataModelStorageSpaces>`_

        Args:
            external_ids (List[str], optional): External IDs

        Returns:
            DataModelStorageSpaceList: The requested spaces.

        Examples:

            Get spaces by external id::

                >>> from cognite.client import CogniteClient
                >>> c = CogniteClient()
                >>> res = c.spaces.retrieve_multiple(external_ids=["abc", "def"])
        """
        utils._auxiliary.assert_type(external_ids, "external_id", [List], allow_none=True)
        return self._retrieve_multiple(
            ids=ids, external_ids=external_ids, ignore_unknown_ids=ignore_unknown_ids, wrap_ids=True
        )

    def list(
        self,
        limit: int = 25,
    ) -> DataModelStorageSpaceList:
        """`List spaces <https://docs.cognite.com/api/v1/#operation/listDataModelStorageSpaces>`_

        Args:
            limit (int, optional): Maximum number of spaces to return. Defaults to 25. Set to -1, float("inf") or None
                to return all items.

        Returns:
            DataModelStorageSpaceList: List of requested spaces

        Examples:

            List spaces (no filters supported yet):

                >>> from cognite.client import CogniteClient
                >>> c = CogniteClient()
                >>> space_list = c.spaces.list(limit=5)

            Iterate over spaces:

                >>> from cognite.client import CogniteClient
                >>> c = CogniteClient()
                >>> for space in c.spaces:
                ...     space # do something with the spaces

            Iterate over chunks of spaces to reduce memory load::

                >>> from cognite.client import CogniteClient
                >>> c = CogniteClient()
                >>> for space_list in c.spaces(chunk_size=2500):
                ...     space_list # do something with the list
        """
        filter = None
        # filter = DataModelStorageSpaceFilter(
        #     metadata=metadata,
        #     created_time=created_time,
        #     last_updated_time=last_updated_time,
        #     external_id_prefix=external_id_prefix,
        #     write_protected=write_protected,
        # ).dump(camel_case=True)
        return self._list(method="POST", limit=limit, filter=filter, headers={"cdf-version": "alpha"})

    def delete(
        self,
        external_id: Union[str, List[str]] = None,
    ) -> None:
        """`Delete one or more assets <https://doc.cognitedata.com/api/v1/#operation/deleteAssets>`_

        Args:
            external_id (Union[str, List[str]]): External ID or list of exgernal ids

        Returns:
            None

        Examples:

            Delete spaces by external id::

                >>> from cognite.client import CogniteClient
                >>> c = CogniteClient()
                >>> c.data_model_storages.spaces.delete(external_id="3")
        """
        self._delete_multiple(
            external_ids=external_id,
            wrap_ids=False,
            # extra_body_fields={},
        )
