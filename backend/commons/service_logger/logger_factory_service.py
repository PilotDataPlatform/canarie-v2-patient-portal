import logging
import os, os.path
import sys
from models.service_meta_class import MetaService
from .formatter import formatter_factory
from logging.handlers import RotatingFileHandler
my_formatter = formatter_factory()

class SrvLoggerFactory(metaclass=MetaService):
    def __init__(self, name):
        if not os.path.exists("./logs/"):
            os.makedirs("./logs/")
        self.name = name
    def get_logger(self):
        logger = logging.getLogger(self.name)
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            # File Handler
            handler = RotatingFileHandler("logs/{}.log".format(self.name), maxBytes=50000, backupCount=2) 
            handler.setFormatter(my_formatter)
            handler.setLevel(logging.DEBUG)
            # Standard Out Handler
            stdout_handler = logging.StreamHandler(sys.stdout)
            stdout_handler.setFormatter(my_formatter)
            stdout_handler.setLevel(logging.DEBUG)
            # Standard Err Handler
            stderr_handler = logging.StreamHandler(sys.stderr)
            stderr_handler.setFormatter(my_formatter)
            stderr_handler.setLevel(logging.ERROR)
            # register handlers
            logger.addHandler(handler)
            logger.addHandler(stdout_handler)
            logger.addHandler(stderr_handler)
        return logger
