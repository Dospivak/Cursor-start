"""Logging configuration and utilities."""

import sys
from pathlib import Path
from typing import Union

from loguru import logger

from src.config.settings import BASE_DIR


def setup_logger(log_file: Union[str, Path] = None) -> None:
    """Configure the application logger.
    
    Args:
        log_file: Optional path to the log file. If not provided,
                 logs will be written to BASE_DIR/logs/app.log
    """
    # Remove default handler
    logger.remove()
    
    # Create logs directory if it doesn't exist
    log_dir = BASE_DIR / 'logs'
    log_dir.mkdir(exist_ok=True)
    
    # Set default log file if not provided
    if log_file is None:
        log_file = log_dir / 'app.log'
    
    # Add handlers
    logger.add(
        sys.stderr,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="INFO"
    )
    
    logger.add(
        log_file,
        rotation="500 MB",
        retention="10 days",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
        level="DEBUG"
    )


# Initialize logger
setup_logger() 