import logging
import os

# debug, info, warning, error, critical

LOGGING_LEVEL = int(os.environ.get(
    "LOGGING_LEVEL", 
    default=0
))

logging.basicConfig(level=LOGGING_LEVEL)
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")
# logging.critical("This is a critical log")

# 1. Create logger
logger = logging.getLogger(name=__name__)  # __main__ or log

# 2. Create handler
all_handler = logging.FileHandler(filename="all.log")

# 2.1 Create a formatter
# datetime - filename - level - message
formatter = logging.Formatter(
    fmt="%(asctime)s - %(filename)s - %(levelname)s - %(message)s"
)

# 2.2 Subscribe formatter
all_handler.setFormatter(formatter)

# 3. Subscribe handler
logger.addHandler(all_handler)

# 4. Create a error logger
error_handler = logging.FileHandler(filename="error.log")

# 4.1 Subscribe formatter
error_handler.setFormatter(formatter)

# 4.2 Change level to errors and criticals
error_handler.setLevel(40)

# 5. Subscribe handler
logger.addHandler(error_handler)

logger.debug("This is a debug log from logger")
logger.info("This is a info log from logger")
logger.warning("This is a warning log from logger")
logger.error("This is a error log from logger")
logger.critical("This is a critical log from logger")