from typing_extensions import Literal
from rclonepy.ifaces.cmds_iface import RcloneCmd
from rclonepy.ifaces.shell_actor_iface import ShellActorIface


def cat(actor: ShellActorIface, source: str, flags=None) -> str:
    """rclone cat sends any files to standard output.
    You can use it like this to output a single file
        rclone cat remote:path/to/file

    Or like this to output any file in dir or its subdirectories.
        rclone cat remote:path/to/dir

    Or like this to output any .txt files in dir or its subdirectories.
        rclone --include "*.txt" cat remote:path/to/dir

    Flags:
        --count int    Only print N characters. (default -1)
        --discard      Discard the output instead of printing.
        --head int     Only print the first N characters.
    -h, --help         help for cat
        --offset int   Start printing at offset N (or from end if -ve).
        --tail int     Only print the last N characters.
    """
    ucmd = RcloneCmdItem(source=source, flags=flags)
    res = ShellActorIface.runcmd_safe(actor, ucmd)
    return res

impl_method = cat

class RcloneCmdItem(RcloneCmd):
    __doc__ = impl_method.__doc__

    cmdname: Literal['cat'] = 'cat'
    class Config:
        method = impl_method

