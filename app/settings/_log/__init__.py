from ._logger import LoggerSetup

logger = LoggerSetup(name="giters").get_logger()

__all__ = ["logger"]
