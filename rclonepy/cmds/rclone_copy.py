from typing_extensions import Literal
from rclonepy.ifaces.cmds_iface import RcloneCmd
from rclonepy.ifaces.shell_actor_iface import ShellActorIface


def copy(actor: ShellActorIface, source: str, dest: str, flags=None, **kw) -> str:
    """
    Copy the source to the destination.  Doesn't transfer
    unchanged files, testing by size and modification time or
    MD5SUM.  Doesn't delete files from the destination.

    Note that it is always the contents of the directory that is synced,
    not the directory so when source:path is a directory, it's the
    contents of source:path that are copied, not the directory name and
    contents.

    If dest:path doesn't exist, it is created and the source:path contents
    go there.

    For example

        rclone copy source:sourcepath dest:destpath

    Let's say there are two files in sourcepath

        sourcepath/one.txt
        sourcepath/two.txt

    This copies them to

        destpath/one.txt
        destpath/two.txt

    Not to

        destpath/sourcepath/one.txt
        destpath/sourcepath/two.txt

    If you are familiar with `rsync`, rclone always works as if you had
    written a trailing `/` - meaning "copy the contents of this directory".
    This applies to all commands and whether you are talking about the
    source or destination.

    See the [--no-traverse](/docs/#no-traverse) option for controlling
    whether rclone lists the destination directory or not.  Supplying this
    option when copying a small number of files into a large destination
    can speed transfers up greatly.

    For example, if you have many files in /path/to/src but only a few of
    them change every day, you can copy all the files which have changed
    recently very efficiently like this:

        rclone copy --max-age 24h --no-traverse /path/to/src remote:

    **Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics.

    **Note**: Use the `--dry-run` or the `--interactive`/`-i` flag to test without copying anything.

    Usage:
    rclone copy source:path dest:path [flags]

    Flags:
        --create-empty-src-dirs   Create empty source dirs on destination after copy
    -h, --help                    help for copy
    """
    ucmd = RcloneCmdItem(source=source, dest=dest, flags=flags)
    res = ShellActorIface.runcmd_safe(actor, ucmd, **kw)
    return res

impl_method = copy

class RcloneCmdItem(RcloneCmd):
    __doc__ = impl_method.__doc__

    cmdname: Literal['copy'] = 'copy'
    class Config:
        method = impl_method