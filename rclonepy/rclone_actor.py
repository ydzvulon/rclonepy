
import os
from rclonepy.cmds.rclone_cmds import RcloneCmdsMixin
import re
import shlex
from functools import lru_cache

import spur

from rclonepy.cmds.rclone_tree import tree
from rclonepy.ifaces.shell_actor_iface import ProcIface, ShellActorIface

class RcloneActor(ShellActorIface, RcloneCmdsMixin):
    def __init__(self) -> None:
        pass
        
    @lru_cache(maxsize=1)
    def shell(self):
        return spur.LocalShell()

    def runcmd(self, cmd, **kw):
        shell = self.shell()
        if isinstance(cmd, str):
            cmd_tokens=shlex.split(cmd)
        elif isinstance(cmd, list):
            cmd_tokens=cmd
        else:
            cmd_tokens = cmd.get_cmd_args()
        if os.environ.get('RCLONE_CONFIG_FILE__HOST_EXT'):
            update_env = {
                'RCLONE_CONFIG': os.environ.get('RCLONE_CONFIG_FILE__HOST_EXT'),
            }
        else:
            update_env = {}
        res_raw = shell.run(cmd_tokens, update_env=update_env)
        res =  res_raw.output.decode()
        return res


class ProcessHolder:
    def __init__(self, seed, process: ProcIface) -> None:
        self.seed = seed
        self.proceess = process
    
    def get_result(self):
        return self.proceess.wait_for_result()

class RcloneAsync(ShellActorIface, RcloneCmdsMixin):

    @lru_cache(maxsize=1)
    def shell(self):
        return spur.LocalShell()

    def runcmd(self, cmd, **kw) -> ProcessHolder:
        shell = self.shell()
        if isinstance(cmd, str):
            cmd_tokens=shlex.split(cmd)
        elif isinstance(cmd, list):
            cmd_tokens=cmd
        else:
            cmd_tokens = cmd.get_cmd_args()

        proc = shell.spawn(cmd_tokens)

        return ProcessHolder(cmd, proc)