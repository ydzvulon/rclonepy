# content of conftest.py
import os
import pytest


def pytest_collect_file(parent, path: 'LocalPath'):

    if path.basename.endswith("test.tasks.yml"):
        return YamlFile.from_parent(parent, fspath=path)


class YamlFile(pytest.File):
    def collect(self):
        # We need a yaml parser, e.g. PyYAML.
        import yaml

        raw = yaml.safe_load(self.fspath.open())
        for name, spec in sorted(raw['tasks'].items()):
            if name.startswith('test'):
                spec["_fspath"] = str(self.fspath)
                yield YamlItem.from_parent(self, name=name, spec=spec)


class YamlItem(pytest.Item):
    def __init__(self, name, parent, spec):
        super().__init__(name, parent)
        self.spec = spec

    def runtest(self):
        import pathlib
        _me = pathlib.Path(__file__).absolute()
        _rt = _me.parent.parent
        _cmd = f'task -t {self.spec["_fspath"]} {self.name} -o prefixed TDIR={_rt}'
        res = os.system(_cmd)
        if res != 0:
            raise YamlException(self, self.name, _cmd)
        # if self.spec.get('vars', None):
        #     raise YamlException(self, self.name, self.spec['_fspath'])
        # for name, value in self.spec['cmds']:
        #     # Some custom test execution (dumb example follows).
        #     _cmd = f'task -t {value["_fspath"]} name -o prefixed TDIR={_rt}'
        #     # res = os.system(_cmd)
        #     # if res != 0:
        #     #     raise YamlException(self, name, _cmd)

        #     if self.spec.get('vars', None):
        #         raise YamlException(self, name, _cmd)
    def repr_failure(self, excinfo):
        """Called when self.runtest() raises an exception."""
        if isinstance(excinfo.value, YamlException):
            return "\n".join(
                [
                    "usecase execution failed",
                    "   spec failed: {1!r}: {2!r}".format(*excinfo.value.args),
                    "   no further details known at this point.",
                ]
            )
        else:
            return f"{excinfo.value}"

    def reportinfo(self):
        return self.fspath, 0, f"usecase: {self.name}"


class YamlException(Exception):
    """Custom exception for error reporting."""