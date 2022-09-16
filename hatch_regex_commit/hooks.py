from hatchling.plugin import hookimpl

from hatch_regex_commit.version_source import RegexCommitSource


@hookimpl
def hatch_register_version_source():
    return RegexCommitSource
