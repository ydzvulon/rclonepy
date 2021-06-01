from pathlib import Path

from rclonepy.rclone_actor import ProcessHolder, RcloneActor

def _get_rclone_sync() ->RcloneActor:
    return RcloneActor()

def _get_my_p():
    return Path(__file__)

def test_rclone_cat_first():
    pp = _get_my_p().absolute()
    rclone = _get_rclone_sync()
    res = rclone.cat(str(pp))
    assert 'test_rclone_cat' in  res


def test_rclone_copy_simple():
    pp = _get_my_p().absolute()
    
    dp = Path('/tmp/_testing') / pp.name

    rclone = _get_rclone_sync()
    res = rclone.copyto(source=str(pp), dest=str(dp))

    assert dp.exists()
    assert pp.stat().st_size == dp.stat().st_size

    assert rclone.size(str(pp)) == rclone.size(str(dp))
