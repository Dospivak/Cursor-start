"""Pytest configuration and fixtures."""

import os
from typing import Generator

import pytest
from dotenv import load_dotenv

from src.database.connection import DatabaseConnection


@pytest.fixture(scope='session', autouse=True)
def load_env() -> None:
    """Load environment variables before running tests."""
    load_dotenv()
    # Set test database
    os.environ['DB_NAME'] = 'test_database'


@pytest.fixture
def db_connection() -> Generator[DatabaseConnection, None, None]:
    """Provide a database connection for tests.
    
    Yields:
        DatabaseConnection: A database connection instance.
    """
    connection = DatabaseConnection()
    connection.connect()
    yield connection
    connection.disconnect() 