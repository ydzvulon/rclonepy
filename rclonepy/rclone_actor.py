
import os
import re
import shlex
from functools import lru_cache

import spur

from rclonepy.cmds.rclone_tree import tree
from rclonepy.ifaces.shell_actor_iface import ShellActorIface

class RcloneActor(ShellActorIface):
    def __init__(self) -> None:
        pass
        
    @lru_cache(maxsize=1)
    def shell(self):
        return spur.LocalShell()

    def runcmd(self, cmd, **kw):
        shell = self.shell()
        cmd_tokens=shlex.split(cmd)
        if os.environ.get('RCLONE_CONFIG_FILE__HOST_EXT'):
            update_env = {
                'RCLONE_CONFIG': os.environ.get('RCLONE_CONFIG_FILE__HOST_EXT'),
            }
        else:
            update_env = {}
        res_raw = shell.run(cmd_tokens, update_env=update_env)
        res =  res_raw.output.decode()
        return res
