from typing_extensions import Literal
from rclonepy.ifaces.cmds_iface import RcloneCmd
from pydantic import BaseModel
from rclonepy.ifaces.shell_actor_iface import ShellActorIface

def tree(actor: ShellActorIface, source: str, flags: dict = None) -> str:
    """
    rclone tree lists the contents of a remote in a similar way to the
    unix tree command.

    For example

        $ rclone tree remote:path
        /
        ├── file1
        ├── file2
        ├── file3
        └── subdir
            ├── file4
            └── file5
        
        1 directories, 5 files

    You can use any of the filtering options with the tree command (e.g.
    --include and --exclude).  You can also use --fast-list.

    The tree command has many options for controlling the listing which
    are compatible with the tree command.  Note that not all of them have
    short options as they conflict with rclone's short options.
    """
    ucmd = RcloneCmdItem(source=source, flags=flags)
    res = ShellActorIface.runcmd_safe(actor, ucmd)
    return res

class RcloneCmdItem(RcloneCmd):
    __doc__ = tree.__doc__
    cmdname: Literal['tree'] = 'tree'
    class Config:
        method = tree
