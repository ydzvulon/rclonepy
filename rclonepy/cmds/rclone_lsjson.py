from pydantic import BaseModel
from typing_extensions import Literal
from rclonepy.ifaces.cmds_iface import RcloneCmd
from rclonepy.ifaces.shell_actor_iface import ShellActorIface


def lsjson(actor: ShellActorIface, source: str, flags=None, **kw) -> str:
    """rclone cat sends any files to standard output.
    List directories and objects in the path in JSON format.
    The output is an array of Items, where each Item looks like this
    There are several related list commands

    * `ls` to list size and path of objects only
    * `lsl` to list modification time, size and path of objects only
    * `lsd` to list directories only
    * `lsf` to list objects and directories in easy to parse format
    * `lsjson` to list objects and directories in JSON format

    `ls`,`lsl`,`lsd` are designed to be human readable.
    `lsf` is designed to be human and machine readable.
    `lsjson` is designed to be machine readable.

    Note that `ls` and `lsl` recurse by default - use `--max-depth 1` to stop the recursion.

    The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default - use `-R` to make them recurse.

    Listing a non existent directory will produce an error except for
    remotes which can't have empty directories (e.g. s3, swift, or gcs -
    the bucket based remotes).

    Usage:
    rclone lsjson remote:path [flags]

    Flags:
        --dirs-only               Show only directories in the listing.
    -M, --encrypted               Show the encrypted names.
        --files-only              Show only files in the listing.
        --hash                    Include hashes in the output (may take longer).
        --hash-type stringArray   Show only this hash type (may be repeated).
    -h, --help                    help for lsjson
        --no-mimetype             Don't read the mime type (can speed things up).
        --no-modtime              Don't read the modification time (can speed things up).
        --original                Show the ID of the underlying Object.
    -R, --recursive               Recurse into the listing.
    """
    ucmd = RcloneCmdItem(source=source, flags=flags)
    res = ShellActorIface.runcmd_safe(actor, ucmd, **kw)
    return res

impl_method = lsjson

class RcloneCmdItem(RcloneCmd):
    __doc__ = impl_method.__doc__

    cmdname: Literal['lsjson'] = 'lsjson'
    class Config:
        method = impl_method
