"""Base model with common functionality."""

from typing import Any, Dict, List, Optional

from src.database.connection import DatabaseConnection


class BaseModel:
    """Base model class with common CRUD operations."""
    
    table_name: str = ''
    
    def __init__(self) -> None:
        """Initialize the base model."""
        self.db = DatabaseConnection()
    
    def create(self, data: Dict[str, Any]) -> Optional[int]:
        """Create a new record.
        
        Args:
            data: Dictionary of column names and values.
            
        Returns:
            Optional[int]: The ID of the created record if successful, None otherwise.
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['%s'] * len(data))
        query = f'INSERT INTO {self.table_name} ({columns}) VALUES ({placeholders})'
        
        try:
            self.db.connect()
            result = self.db.execute_query(query, tuple(data.values()))
            return result[0]['LAST_INSERT_ID()'] if result else None
        finally:
            self.db.disconnect()
    
    def get_by_id(self, id: int) -> Optional[Dict[str, Any]]:
        """Get a record by ID.
        
        Args:
            id: The ID of the record to retrieve.
            
        Returns:
            Optional[Dict[str, Any]]: The record if found, None otherwise.
        """
        query = f'SELECT * FROM {self.table_name} WHERE id = %s'
        
        try:
            self.db.connect()
            result = self.db.execute_query(query, (id,))
            return result[0] if result else None
        finally:
            self.db.disconnect()
    
    def get_all(self) -> List[Dict[str, Any]]:
        """Get all records.
        
        Returns:
            List[Dict[str, Any]]: List of all records.
        """
        query = f'SELECT * FROM {self.table_name}'
        
        try:
            self.db.connect()
            return self.db.execute_query(query)
        finally:
            self.db.disconnect()
    
    def update(self, id: int, data: Dict[str, Any]) -> bool:
        """Update a record.
        
        Args:
            id: The ID of the record to update.
            data: Dictionary of column names and values to update.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        set_clause = ', '.join([f'{k} = %s' for k in data.keys()])
        query = f'UPDATE {self.table_name} SET {set_clause} WHERE id = %s'
        
        try:
            self.db.connect()
            self.db.execute_query(query, (*data.values(), id))
            return True
        except Exception:
            return False
        finally:
            self.db.disconnect()
    
    def delete(self, id: int) -> bool:
        """Delete a record.
        
        Args:
            id: The ID of the record to delete.
            
        Returns:
            bool: True if successful, False otherwise.
        """
        query = f'DELETE FROM {self.table_name} WHERE id = %s'
        
        try:
            self.db.connect()
            self.db.execute_query(query, (id,))
            return True
        except Exception:
            return False
        finally:
            self.db.disconnect() 