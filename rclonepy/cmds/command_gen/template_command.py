from typing_extensions import Literal
from rclonepy.ifaces.cmds_iface import RcloneCmd
from rclonepy.ifaces.shell_actor_iface import ShellActorIface


def _CMD_NAME_(actor: ShellActorIface, source: str, flags=None, **kw) -> str:
    """
    _DOCS_TEXT_
    """
    ucmd = RcloneCmdItem(source=source, flags=flags)
    res = ShellActorIface.runcmd_safe(actor, ucmd, **kw)
    return res

impl_method = _CMD_NAME_

class RcloneCmdItem(RcloneCmd):
    __doc__ = impl_method.__doc__

    cmdname: Literal['_CMD_NAME_'] = '_CMD_NAME_'
    class Config:
        method = impl_method
