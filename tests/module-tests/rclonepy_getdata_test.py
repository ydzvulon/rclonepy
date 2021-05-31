from pathlib import Path

from rclonepy.rclone_actor import ProcessHolder, RcloneAsync, RcloneActor


def _get_rclone_async() ->RcloneAsync:
    return RcloneAsync()

def _get_rclone_sync() ->RcloneActor:
    return RcloneActor()

def _get_my_p():
    return Path(__file__)

def test_rclone_cat_first():
    pp = _get_my_p().absolute()
    rclone = _get_rclone_sync()
    res = rclone.cat(str(pp))
    assert 'test_rclone_cat' in  res