
from rclonepy.rclone_actor import ProcessHolder, RcloneAsync, RcloneActor


def _get_rclone_async() ->RcloneAsync:
    return RcloneAsync()

def _get_rclone_sync() ->RcloneActor:
    return RcloneActor()

def test__rclone_size1():
    from pathlib import Path
    
    me_parent_p = Path(__file__).parent
    name = Path(__file__).name

    rclone = _get_rclone_async()
    promise: ProcessHolder = rclone.size(str(Path(__file__)))
    the_size = promise.get_result()
    print(the_size.output.decode())
    pass

def test__rclone_size2():
    from pathlib import Path
    
    me_parent_p = Path(__file__).parent
    name = Path(__file__).name

    rclone = _get_rclone_sync()
    pp = str(Path(__file__).absolute())
    the_size = rclone.size(source=pp)
    print(the_size)
