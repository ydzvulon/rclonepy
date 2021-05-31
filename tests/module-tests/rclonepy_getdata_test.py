from pathlib import Path

from rclonepy.rclone_actor import ProcessHolder, RcloneAsync, RcloneActor


def _get_rclone_async() ->RcloneAsync:
    return RcloneAsync()

def _get_rclone_sync() ->RcloneActor:
    return RcloneActor()

def _get_my_p():
    return Path(__file__)

def test__rclone_size1():
    rclone = _get_rclone_async()
    promise: ProcessHolder = rclone.size(str(_get_my_p()))
    the_size = promise.get_result()
    print(the_size.output.decode())
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
    tr = rclone.tree(source=str(pp))
    print(tr)