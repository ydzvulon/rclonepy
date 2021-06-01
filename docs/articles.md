# Artciles

## Reducing Complexity with Pydantic & Singledispatch

> https://www.gidware.com/reducing-complexity-with-pydantic-singledispatch/

### Base Settings with Literal

```python
from typing import Union

from pydantic import BaseSettings, parse_obj_as
from typing_extensions import Literal


class LocalContext(BaseSettings):
    env: Literal["local"]  # 1
    mongo_url: str


class ProdContext(BaseSettings):
    env: Literal["prod"]  # 1
    mongo_url: str
    mongo_replicaset: str  # 2


Context = Union[LocalContext, ProdContext]  # 3

context = parse_obj_as(Context, {})  # 4
```

### singledispatch

```python
from functools import singledispatch


@singledispatch  # 1
def to_json(inp):  # 1
    """implementations in dispatched functions"""


@to_json.register  # 2
def as_json_str(input_str: str) -> str:  # 2
    return f'"{input_str}"'  # 4


@to_json.register  # 3
def as_json_str(inputs: list) -> str:  # 3
    json_inputs = ", ".join(to_json(single_input) for single_input in inputs)  # 4
    return f"[{json_inputs}]"  # 4


def test_to_json():
    assert to_json("Hello world") == '"Hello world"'  # 5
    assert to_json(["a", "l", "i", "c", "e"]) == '["a", "l", "i", "c", "e"]'  # 6
```

### Magic

```python
import os
from typing import Union

from pymongo import MongoClient, ReadPreference
import pytest
from functools import singledispatch
from pydantic import BaseSettings, parse_obj_as
from typing_extensions import Literal


class LocalContext(BaseSettings):
    env: Literal["local"]  # 1
    mongo_url: str


class ProdContext(BaseSettings):
    env: Literal["prod"]  # 1
    mongo_url: str
    mongo_replicaset: str  # 1


Context = Union[LocalContext, ProdContext]


@singledispatch  # 2
def read_env(context: Context) -> MongoClient:
    """implementations in dispatched functions"""


@read_env.register  # 3
def create_local_mongo(context: LocalContext) -> MongoClient:
    print("Creating local MongoClient")
    return MongoClient(context.mongo_url)  # 4


@read_env.register  # 3
def create_prod_mongo(context: ProdContext) -> MongoClient:
    print("Creating production MongoClient")
    return MongoClient(
        context.mongo_url,
        replicaSet=context.mongo_replicaset,
        read_preference=ReadPreference.NEAREST,
    )  # 4


def test_reads_local_context():
    os.environ.clear()
    os.environ["ENV"] = "local"
    os.environ["MONGO_URL"] = "mongodb://madeup_name:madeup_pass@localhost:27017"

    context = parse_obj_as(Context, {})  # 5
    client = read_env(context)  # 5

    assert client.address == ("localhost", 27017)  # 6


def test_reads_prod_context():
    os.environ.clear()
    mongo_url = (
        "mongodb://madeup_name:madeup_pass@mongodb0.example.com:27017/?authSource=admin"
    )
    os.environ["ENV"] = "prod"
    os.environ["MONGO_URL"] = mongo_url
    os.environ["MONGO_REPLICASET"] = "put-your-real-replicaset-here"

    context = parse_obj_as(Context, {})  # 5
    client = read_env(context)  # 5

    assert client.address == ("mongodb0.example.com", 27017)  # 6
```