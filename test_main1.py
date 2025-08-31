import pytest
from main1 import userManager

# Fixtures can prepare something before a test and clean up after the test finishes.
@pytest.fixture
def user_manager():
    return userManager()

def test_add_user(user_manager):
    assert user_manager.add_users("John","abc@gmail.com")==True
    assert user_manager.get_user("John")=="abc@gmail.com"

def test_add_duplicate_user(user_manager):
    user_manager.add_users("John","abc@gmail.com")
    # used to test that a ValueError exception is raised when attempting to add a duplicate user.


    with pytest.raises(ValueError):
        user_manager.add_users("John","abc@gmail.com")