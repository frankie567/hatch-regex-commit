# hatch-regex-commit

[![PyPI - Version](https://img.shields.io/pypi/v/hatch-regex-commit.svg)](https://pypi.org/project/hatch-regex-commit)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hatch-regex-commit.svg)](https://pypi.org/project/hatch-regex-commit)

-----

This provides a plugin for [Hatch](https://github.com/pypa/hatch) that automatically creates a Git **commit** and **tag** after version bumping.

## Global dependency

Ensure `hatch-regex-commit` is defined within the `build-system.requires` field in your `pyproject.toml` file.

```toml
[build-system]
requires = ["hatchling", "hatch-regex-commit"]
build-backend = "hatchling.build"
```

## Version source

The [version source plugin](https://hatch.pypa.io/latest/plugins/version-source/) name is `regex_commit`.

- ***pyproject.toml***

    ```toml
    [tool.hatch.version]
    source = "regex_commit"
    path = "my_library/___about___.py"
    ```

- ***hatch.toml***

    ```toml
    [version]
    source = "regex_commit"
    path = "my_library/___about___.py"
    ```

### Version source options

This plugin inherits from the Hatch builtin [Regex version source](https://hatch.pypa.io/latest/plugins/version-source/regex/). It inherits from all its [options](https://hatch.pypa.io/latest/plugins/version-source/regex/#options) and add the following ones:

| Option              | Type        | Default                                          | Description                                                                                                           |
| ------------------- | ----------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------- |
| `check_dirty`       | `bool`      | true                                             | Check if the Git repository is dirty, e.g., you have uncommited changes. If you have, the version bumping will abort. |
| `commit`            | `bool`      | true                                             | Whether to create a Git commit.                                                                                       |
| `commit_message`    | `str`       | `Bump version {current_version} → {new_version}` | Template of the Git commit message.                                                                                   |
| `commit_extra_args` | `list[str]` | []                                               | List of [extra arguments](https://git-scm.com/docs/git-commit#_options) for Git commit command.                       |
| `tag`               | `bool`      | true                                             | Whether to create a Git tag.                                                                                          |
| `tag_name`          | `str`       | `v{new_version}`                                 | Template for the Git tag name.                                                                                        |
| `tag_message`       | `str`       | `Bump version {current_version} → {new_version}` | Template of the Git tag message.                                                                                      |
| `tag_sign`          | `bool`      | true                                             | Whether to sign the Git tag.                                                                                          |

## Examples

### Basic

```toml
  [tool.hatch.version]
  source = "regex_commit"
  path = "my_library/___about___.py"
```

### Custom commit message

```toml
  [tool.hatch.version]
  source = "regex_commit"
  path = "my_library/___about___.py"
  commit_message = "🚀 Version {new_version}"
```

### Edit commit message in the editor before proceeding

```toml
  [tool.hatch.version]
  source = "regex_commit"
  path = "my_library/___about___.py"
  commit_extra_args = ["-e"]
```

### Disable Git tag

```toml
  [tool.hatch.version]
  source = "regex_commit"
  path = "my_library/___about___.py"
  tag = false
```

## License

`hatch-regex-commit` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
