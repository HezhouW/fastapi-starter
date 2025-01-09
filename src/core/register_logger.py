import logging
import sys
from loguru import logger
from src.config.config import settings

def register_logger(app=None):
    level = settings.loguru.LOG_LEVEL
    path = settings.loguru.LOG_PATH
    retention = settings.loguru.LOG_RETENTION

    # intercept everything at the root logger
    logging.root.handlers = [InterceptHandler()]
    # logging.getLogger().handlers = [InterceptHandler()]
    logging.root.setLevel(level)

    # remove every other logger's handlers
    # and propagate to root logger
    for name in logging.root.manager.loggerDict.keys():
        # logging.getLogger(name).handlers = [InterceptHandler()]
        # logging.getLogger(name).propagate = False
        # logging.getLogger(name).setLevel(10)
        logging.getLogger(name).handlers = []
        if '.' not in name:
            logging.getLogger(name).addHandler(InterceptHandler())
            logging.getLogger(name).propagate = False
    # configure loguru
    logger.configure(handlers=[
        {"sink": sys.stdout},
        {"sink": path, "rotation": "00:00", "retention": retention},
    ])


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 0
        while frame and (depth == 0 or frame.f_code.co_filename == logging.__file__):
            frame = frame.f_back
            depth += 1

        ''' if python version <=3.11, PLEASE use this code instead!!!
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame =frame.f_back
            depth += 1
        '''

        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())
