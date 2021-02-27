"""
Name : LoggingUtility.py
Author : Jaga
Date : 20-02-2021
"""

import logging
from utilities.FileReadUtility import ReadConfig


class GenerateLogs:

    @staticmethod
    def log_gen(__name__):
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler(filename=ReadConfig.get_test_data('LOG_FILE'), mode='a')
        formatter = logging.Formatter('%(asctime)-12s - %(name)s - %(levelname)s - %(message)s',
                                      datefmt="%d-%m-%Y %H:%M:%S")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.INFO)
        return logger
