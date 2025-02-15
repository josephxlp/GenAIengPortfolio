import os
import logging
from datetime import datetime

def setup_daily_logger():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    log_dir = os.path.join(base_dir, 'logs')  
    os.makedirs(log_dir, exist_ok=True)


    current_time = datetime.now().strftime("%m_%d_%y_%I_%M_%p")
    log_file = os.path.join(log_dir, f"{current_time}.log")


    logging.basicConfig(
        filename=log_file,
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s', 
        filemode='w',
        encoding='utf-8' 
    )


    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s')  # Added line number
    console_handler.setFormatter(console_formatter)


    logging.getLogger().addHandler(console_handler)


    return logging.getLogger(__name__)

"""
source:https://www.freecodecamp.org/news/what-are-logs-in-programming/
example.py
from glogger import setup_daily_logger

logger = setup_daily_logger()


logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
"""
