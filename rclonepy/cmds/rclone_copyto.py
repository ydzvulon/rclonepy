from typing_extensions import Literal
from rclonepy.ifaces.cmds_iface import RcloneCmd
from rclonepy.ifaces.shell_actor_iface import ShellActorIface


def copyto(actor: ShellActorIface, source: str, dest: str, flags=None, **kw)  -> str:
    """
    If source:path is a file or directory then it copies it to a file or
    directory named dest:path.

    This can be used to upload single files to other than their current
    name.  If the source is a directory then it acts exactly like the copy
    command.

    So
        rclone copyto src dst

    where src and dst are rclone paths, either remote:path or
    /path/to/local or C:\windows\path\if\on\windows.

    This will:

        if src is file
            copy it to dst, overwriting an existing file if it exists
        if src is directory
            copy it to dst, overwriting existing files if they exist
            see copy command for full details

    This doesn't transfer unchanged files, testing by size and
    modification time or MD5SUM.  It doesn't delete files from the
    destination.

    **Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics

    Usage:
    rclone copyto source:path dest:path [flags]

    Flags:
    -h, --help   help for copyto
    """
    ucmd = RcloneCmdItem(source=source, dest=dest, flags=flags)
    res = ShellActorIface.runcmd_safe(actor, ucmd, **kw)
    return res

impl_method = copyto

class RcloneCmdItem(RcloneCmd):
    __doc__ = impl_method.__doc__

    cmdname: Literal['copyto'] = 'copyto'
    class Config:
        method = impl_method
