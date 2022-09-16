class HatchRegexCommitException(Exception):
    pass


class GitNotAvailableException(HatchRegexCommitException):
    def __init__(self) -> None:
        self.message = "Git is not available on this system"


class WorkingDirectoryIsDirtyException(HatchRegexCommitException):
    def __init__(self, message):
        self.message = message
