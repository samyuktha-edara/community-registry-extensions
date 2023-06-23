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
class AwsIotfleetwiseModelmanifest(BaseModel):
    Arn: Optional[str]
    CreationTime: Optional[str]
    Description: Optional[str]
    LastModificationTime: Optional[str]
    Name: Optional[str]
    Nodes: Optional[AbstractSet[str]]
    SignalCatalogArn: Optional[str]
    Status: Optional[str]
    Tags: Optional[Any]

    @classmethod
    def _deserialize(
        cls: Type["_AwsIotfleetwiseModelmanifest"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_AwsIotfleetwiseModelmanifest"]:
        if not json_data:
            return None
        dataclasses = {n: o for n, o in getmembers(sys.modules[__name__]) if isclass(o)}
        recast_object(cls, json_data, dataclasses)
        return cls(
            Arn=json_data.get("Arn"),
            CreationTime=json_data.get("CreationTime"),
            Description=json_data.get("Description"),
            LastModificationTime=json_data.get("LastModificationTime"),
            Name=json_data.get("Name"),
            Nodes=set_or_none(json_data.get("Nodes")),
            SignalCatalogArn=json_data.get("SignalCatalogArn"),
            Status=json_data.get("Status"),
            Tags=json_data.get("Tags"),
        )


# work around possible type aliasing issues when variable has same name as a model
_AwsIotfleetwiseModelmanifest = AwsIotfleetwiseModelmanifest


@dataclass
class Tag(BaseModel):
    Key: Optional[str]
    Value: Optional[str]

    @classmethod
    def _deserialize(
        cls: Type["_Tag"],
        json_data: Optional[Mapping[str, Any]],
    ) -> Optional["_Tag"]:
        if not json_data:
            return None
        return cls(
            Key=json_data.get("Key"),
            Value=json_data.get("Value"),
        )


# work around possible type aliasing issues when variable has same name as a model
_Tag = Tag

