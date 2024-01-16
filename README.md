# Hatch plugin to customize build dependencies

Simple Hatch plugin to customize dependencies
whether the build is `editable` or `standard`.
This may be useful for example in monorepo projects
where sub-projects need to be installed manually,
from the local repo, and not the pypi index.
In this case you can add dependencies to the
`standard-dependencies` that will be used only
when building wheels.


## Usage

You can specify `editable-dependencies` for editable installs
and `standard-dependencies` for other builds in the
`[tool.hatch.build.hook.flex]` section of the `pyproject.toml`.
These dependencies, depending on the build type, will be added
to the dependencies already declared in the project section.


```
[build-system]
requires = ["hatchling", "hatch-flex"]
build-backend = "hatchling.build"

[tool.hatch.build.hooks.flex]
editable-dependencies = [...]
standard-dependencies = [...]
```

## Related Projects & Resources
- [hatch](https://hatch.pypa.io/latest/) Modern, extensible Python project management
- [issue 588](https://github.com/pypa/hatch/issues/588) Support for Editable Dependencies
