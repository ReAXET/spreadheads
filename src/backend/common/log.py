from __future__ import annotations

from typing import Optional, TYPE_CHECKING


import os

from loguru import logger
from rich.logging import RichHandler
from backend.core.path_config import LOGPATH
from backend.core.config import settings


if TYPE_CHECKING:
    from typing import Literal, Union
    from pydantic_settings import BaseSettings, SettingsConfigDict
    import loguru



class SpreadHeadLogger:
    def __init__(self):
        self.log_path = LOGPATH


    def log(self) -> loguru.Logger:
        if not os.path.exists(self.log_path):
            os.makedirs(self.log_path)

        log_stdout_file = os.path.join(self.log_path, settings.LOG_STDOUT_FILENAME)
        log_stderr_file = os.path.join(self.log_path, settings.LOG_STDERR_FILENAME)

        log_config = dict(rotation='10 MB', retention='10 days', compression='zip', enqueue=True, backtrace=True, diagnose=True, diagnose_depth=5, colorize=True, format=settings.LOG_FORMAT, level=settings.LOG_LEVEL, filter=lambda record: record["level"].name != "INFO")

        logger.add(log_stdout_file, **log_config, level=settings.LOG_LEVEL, filter=lambda record: record["level"].name == "INFO") # type: ignore


        logger.add(log_stderr_file, **log_config, level='ERROR', filter=lambda record: record['level'].name == 'ERROR' or record['level'].no >= 30) # type: ignore

        return logger
    


log = SpreadHeadLogger().log()







