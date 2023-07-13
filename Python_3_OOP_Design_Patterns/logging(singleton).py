import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Использование логгера в разных частях приложения
logger.debug("Debug message")
logger.info("Info message")
logger.error("Error message")