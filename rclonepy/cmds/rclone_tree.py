from pydantic import BaseModel
from rclonepy.ifaces.shell_actor_iface import ShellActorIface


class RcloneCmdTree(BaseModel):
    nid = 'tree'
    cmd = "rclone {cid} {source} {dest}"
    source: str

def tree(actor: ShellActorIface, source: str) -> str:
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
    ucmd = RcloneCmdTree(source=source)
    if actor:
        res = actor.runcmd(ucmd)
    else:
        res = ucmd
    return res

