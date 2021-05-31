
class ShellActorIface:
    def runcmd(self, cmd, **kw):
        return NotImplementedError

class ProcResult:
    return_code: int
    output: str
    stderr_output: str

class ProcIface:

    def is_running(self) -> bool:
        return NotImplementedError

    def stdin_write(self, value):
        return NotImplementedError

    def send_signal(self, signal):
        return NotImplementedError

    def wait_for_result(self) -> ProcResult:
        return NotImplementedError
