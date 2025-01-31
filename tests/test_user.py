"""Tests for the User model."""

import pytest

from src.models.user import User


@pytest.fixture
def user_model():
    """Provide a User model instance for tests."""
    return User()

def test_create_user(user_model):
    """Test creating a new user."""
    # Create test user
    user_id = user_model.create_user('test_user', 'test@example.com')
    
    # Verify user was created
    assert user_id is not None
    
    # Get user by ID
    user = user_model.get_by_id(user_id)
    
    # Verify user data
    assert user is not None
    assert user['username'] == 'test_user'
    assert user['email'] == 'test@example.com'

def test_get_user_by_email(user_model):
    """Test retrieving a user by email."""
    # Create test user
    email = 'find_me@example.com'
    user_model.create_user('find_me', email)
    
    # Get user by email
    user = user_model.get_by_email(email)
    
    # Verify user was found
    assert user is not None
    assert user['email'] == email 