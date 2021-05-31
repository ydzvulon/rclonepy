from sys import flags
from typing import Optional
import pydantic
from typing_extensions import Literal


def flags_to_cli(flags: dict):
    if not flags:
        return flags
    res = []
    for k, v in flags.items():
        if v is True:
            res.append(f'--{k}')
        elif v is False:
            res.append(f'--{k}=0')
        elif v is None:
            pass
        else:
            res.append(f"--{k} {str(v)}")
    return " ".join(res)

class CmdBody(pydantic.BaseModel):
    source: Optional[str]
    dest: Optional[str]
    flags: Optional[dict]

    def render_bag(self):
        res = dict(
            source=self.source or "",
            dest=self.dest or "",
            flags=flags_to_cli(self.flags) or ""
        )
        return res

class RcloneCmd(CmdBody):
    # RcloneCmdLine = namedtuple('RcloneCmdLine', ['cmdname', 'source', 'dest', 'flags'])
    actor: Literal['rclone'] = 'rclone'
    cmdname: str
    args_fmt_list = 'rclone {cmdname} {source} {dest} {flags}'
    cmd_line_ready: Optional[str]
    
    def get_cmd_args(self):
        cmd_line = self.args_fmt_list.format(
            **self.render_bag(), 
            cmdname=self.cmdname)
        import shlex
        self.cmd_line_ready = shlex.split(cmd_line)
        return self.cmd_line_ready
