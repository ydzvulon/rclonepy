import json
from pathlib import Path
from typing import List
from rclonepy.schemas.rclone_path_item import RclonePathItem

from rclonepy.rclone_actor import ProcessHolder, RcloneActor


def _get_rclone_sync() ->RcloneActor:
    return RcloneActor()

def _get_my_p():
    return Path(__file__)

def test__rclone_size1_async():
    rclone = _get_rclone_sync()
    upath = str(_get_my_p())
    promise: ProcessHolder = rclone.size(upath, _async=True)
    the_size = promise.get_result()
    print(the_size)
    pass

def test__rclone_size2():
    from pathlib import Path
    rclone = _get_rclone_sync()
    pp = str(Path(__file__).absolute())
    the_size = rclone.size(source=pp)
    print(the_size)

def test__rclone_tree_again():
    from pathlib import Path
    
    rclone = _get_rclone_sync()
    pp = _get_my_p().parent.absolute()
    the_tree = rclone.tree(source=str(pp))
    assert len(the_tree.splitlines()) > 3
    assert _get_my_p().name in the_tree
    print(the_tree)


def test__rclone_lsjson_basic():
    from pathlib import Path
    
    rclone = _get_rclone_sync()
    pp = _get_my_p().parent.absolute()
    
    jsono = rclone.lsjson(source=str(pp), _asjsono=True)
    assert isinstance(jsono, list)
    assert any(it["Name"] == _get_my_p().name for it in jsono)
    # print(jsono)

    text = rclone.lsjson(source=str(pp), _asjsono=False)
    assert isinstance(text, str)
    assert _get_my_p().name in text

    items:List[RclonePathItem] = rclone.lsjson(source=str(pp), _toschema=RclonePathItem)

    assert isinstance(items[0], RclonePathItem)
    assert isinstance(items[0].Size, int)
    item = items[0]
    item.Name == jsono[0]["Name"]

