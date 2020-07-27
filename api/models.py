from typing import Generic, List, TypeVar

from pydantic.generics import GenericModel

DataT = TypeVar("DataT")


class ListResponse(GenericModel, Generic[DataT]):
    results: List[DataT]
