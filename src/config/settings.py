"""Application settings and configuration."""

import os
from pathlib import Path
from typing import Dict, Any

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Debug mode
DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'

# Secret key
SECRET_KEY = os.getenv('APP_SECRET_KEY', 'your-secret-key-here')

# Database settings
DATABASE: Dict[str, Any] = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', '3306')),
    'database': os.getenv('DB_NAME', 'your_database_name'),
    'user': os.getenv('DB_USER', 'your_username'),
    'password': os.getenv('DB_PASSWORD', 'your_password'),
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

# Template directory
TEMPLATE_DIR = BASE_DIR / 'src' / 'templates' 