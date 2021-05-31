import os
import json
from pathlib import Path
from setuptools import setup

def read_file(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class ProjectLayoutPy:
    project_name__txt = 'version/project_name.txt'
    project_props__json = 'version/project_props.json'
    version_prefix__txt = 'version/version_prefix.txt'
    run_reqs__txt = 'rclonepy/requirements.txt'


class _values_:
    name = read_file(ProjectLayoutPy.project_name__txt)
    packages=[name]
    version = read_file(ProjectLayoutPy.version_prefix__txt)
    long_description = read_file("README.md")
    install_requires= [
        l.strip() if l[0]!='"' else l[1:-1].strip()   
        for l in read_file(ProjectLayoutPy.run_reqs__txt).splitlines()]
    print(install_requires)

    props = json.loads(read_file(ProjectLayoutPy.project_props__json))

    @classmethod
    def get_rest(cls, fetch_fields: dict):
        rest = {}
        for k, v in fetch_fields.items():
            if v is True:
                rest[k] = cls.props[k]
            elif isinstance(v, str):
                rest[k] = cls.props[v]
            else:
                raise ValueError(f"not supported: {v}")
        return rest

setup(
    name=_values_.name,
    version=_values_.version,
    long_description=_values_.long_description,
    packages=_values_.packages,
    install_requires=_values_.install_requires,

    **_values_.get_rest(fetch_fields={
        # map by string
        "author": "author",
        # map by same
        "description": True,
        "author_email": True,
        "url": True,
        "keywords": True,
        "license": True,
        "classifiers": True
    })
)
