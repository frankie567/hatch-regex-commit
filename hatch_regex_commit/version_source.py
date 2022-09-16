from typing import List, Type

from hatchling.version.source.regex import RegexSource

from hatch_regex_commit.exceptions import GitNotAvailableException
from hatch_regex_commit.git import Git


class RegexCommitSource(RegexSource):
    PLUGIN_NAME = "regex_commit"

    @property
    def git(self) -> Type[Git]:
        if not Git.is_usable():
            raise GitNotAvailableException()
        return Git

    @property
    def config_check_dirty(self) -> bool:
        return self._get_bool_config("check_dirty", True)

    @property
    def config_commit(self) -> bool:
        return self._get_bool_config("commit", True)

    @property
    def config_commit_message(self) -> str:
        return self._get_str_config(
            "commit_message", "Bump version {current_version} → {new_version}"
        )

    @property
    def config_commit_extra_args(self) -> List[str]:
        extra_args = self.config.get("commit_extra_args", [])
        if not isinstance(extra_args, list):
            raise TypeError(f"option `{extra_args}` must be a list")
        return extra_args

    @property
    def config_tag(self) -> bool:
        return self._get_bool_config("tag", True)

    @property
    def config_tag_name(self) -> str:
        return self._get_str_config("tag_name", "v{new_version}")

    @property
    def config_tag_message(self) -> str:
        return self._get_str_config(
            "tag_message", "Bump version {current_version} → {new_version}"
        )

    @property
    def config_tag_sign(self) -> bool:
        return self._get_bool_config("tag_sign", True)

    def set_version(self, version, version_data):
        if self.config_check_dirty:
            self.git.assert_nondirty()

        super().set_version(version, version_data)

        context = {"current_version": version_data["version"], "new_version": version}

        if self.config_commit:
            file = self.config.get("path", "")
            self.git.add_path(file)
            commit_message = self.config_commit_message.format(**context)
            self.git.commit(commit_message, self.config_commit_extra_args)

        if self.config_tag:
            tag_name = self.config_tag_name.format(**context)
            tag_message = self.config_tag_message.format(**context)
            self.git.tag(self.config_tag_sign, tag_name, tag_message)

    def _get_bool_config(self, name: str, default: bool) -> bool:
        value = self.config.get(name, default)
        if not isinstance(value, bool):
            raise TypeError(f"option `{name}` must be a boolean")
        return value

    def _get_str_config(self, name: str, default: str) -> str:
        value = self.config.get(name, default)
        if not isinstance(value, str):
            raise TypeError(f"option `{name}` must be a string")
        return value
