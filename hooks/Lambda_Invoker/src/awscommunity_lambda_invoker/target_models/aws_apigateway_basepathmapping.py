# DO NOT modify this file by hand, changes will be overwritten
from dataclasses import dataclass

from cloudformation_cli_python_lib.interface import BaseModel
from cloudformation_cli_python_lib.recast import recast_object
from cloudformation_cli_python_lib.utils import deserialize_list

import sys
from inspect import getmembers, isclass
from typing import (
    AbstractSet,
    Any,
    Generic,
    Mapping,
    MutableMapping,
    Optional,
    Sequence,
    Type,
    TypeVar,
)

T = TypeVar("T")


def set_or_none(value: Optional[Sequence[T]]) -> Optional[AbstractSet[T]]:
    if value:
        return set(value)
    return None


@dataclass
class AwsApigatewayBasepathmapping(BaseModel):
    BasePath: Optional[str]
    DomainName: Optional[str]
    RestApiId: Optional[str]
    Stage: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_AwsApigatewayBasepathmapping"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsApigatewayBasepathmapping"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            BasePath=json_data.get("BasePath"),
            DomainName=json_data.get("DomainName"),
            RestApiId=json_data.get("RestApiId"),
            Stage=json_data.get("Stage"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsApigatewayBasepathmapping = AwsApigatewayBasepathmapping

