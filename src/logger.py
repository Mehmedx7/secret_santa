import logging
import os
from pathlib import Path
from logging.handlers import RotatingFileHandler

LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "secret_santa.log"
LOG_SIZE = 5 * 1024 * 1024  # 5MB max size before rotation
LOG_BACKUP_COUNT = 3  # Keep last 3 log files

def get_logger(name: str) -> logging.Logger:
    """
    Configures and returns a logger with both file and console output.
    Uses rotating file handler to prevent excessive log size.
    """
    if not LOG_DIR.exists():
        LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    if logger.hasHandlers():  # Prevent adding multiple handlers
        return logger

    logger.setLevel(logging.DEBUG)

    # File handler with rotation
    file_handler = RotatingFileHandler(LOG_FILE, maxBytes=LOG_SIZE, backupCount=LOG_BACKUP_COUNT)
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(file_formatter)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter("%(levelname)s - %(message)s")
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
