from tkinter.messagebox import NO
from typing_extensions import Literal

from rclonepy.ifaces.cmds_iface import RcloneCmd
from pydantic import BaseModel
from rclonepy.ifaces.shell_actor_iface import ShellActorIface

def size(actor: ShellActorIface, source: str, flags=None, **kw) -> str:
    """
    Prints the total size and number of objects in remote:path.

    Flags:
    -h, --help   help for size
        --json   format output as JSON
    """
    ucmd = RcloneSizeCmd(source=source, flags=flags)
    res = ShellActorIface.runcmd_safe(actor, ucmd, **kw)
    return res

class RcloneSizeCmd(RcloneCmd):
    __doc__ = size.__doc__

    cmdname: Literal['size'] = 'size'
    class Config:
        method = size

