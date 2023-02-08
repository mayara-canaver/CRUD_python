import logging

class Logging:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._file_handler = logging.FileHandler(filename='app.log')
            cls._formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            cls._file_handler.setFormatter(cls._formatter)
        return cls._instance

    def set_log_level(self, logger_name, level):
        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(self._file_handler)

        if not self._file_handler in logger.handlers:
            logger.addHandler(self._file_handler)

    def get_logger(self, logger_name):
        logger = logging.getLogger(logger_name)
        
        if not self._file_handler in logger.handlers:
            logger.addHandler(self._file_handler)
        return logger
        