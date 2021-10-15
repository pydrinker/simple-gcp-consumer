import logging
import logging.config

from .config import settings

# Complete log:
#
# DEFAULT_FORMAT = (
#     "%(asctime)s %(levelname)s %(pathname)s %(lineno)s %(process)s "
#     "%(processName)s %(thread)s %(threadName)s %(name)s %(message)s"
# )

DEFAULT_FORMAT = "%(asctime)s %(module)s %(message)s"

DEFAULT_LOGGING_CONF = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {"format": DEFAULT_FORMAT},
    },
    "handlers": {
        "default": {
            "level": settings.LOG_LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "null": {
            "class": "logging.NullHandler",
        },
    },
    "root": {
        "handlers": ["default"],
        "level": "DEBUG",
    },
    "loggers": {},
}

logging.config.dictConfig(DEFAULT_LOGGING_CONF)
