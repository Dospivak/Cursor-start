import os
from typing import Any, Dict

import mysql.connector
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DatabaseConnection:
    def __init__(self) -> None:
        self.connection = None
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load database configuration from environment variables."""
        return {
            'host': os.getenv('DB_HOST', 'localhost'),
            'port': int(os.getenv('DB_PORT', '3306')),
            'database': os.getenv('DB_NAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD')
        }

    def connect(self) -> None:
        """Establish database connection."""
        try:
            if not self.connection or not self.connection.is_connected():
                self.connection = mysql.connector.connect(**self.config)
                print("Successfully connected to the database")
        except mysql.connector.Error as err:
            print(f"Error connecting to the database: {err}")
            raise

    def disconnect(self) -> None:
        """Close database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")

    def execute_query(self, query: str, params: tuple = None) -> Any:
        """Execute a database query."""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            self.connection.commit()
            return result
        except mysql.connector.Error as err:
            print(f"Error executing query: {err}")
            self.connection.rollback()
            raise
        finally:
            cursor.close() 