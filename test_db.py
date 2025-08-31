import pytest
from db import Database

@pytest.fixture
def db():
    database=Database()
    yield database #provide the fixture instance
    database.data.clear() #cleanup step (needed real DBs)

def test_add_user(db):
    db.add_user("id1","John")
    assert db.get_user("id1")=="John"


def test_add_duplicate_user(db):
    db.add_user("id1","John")

    with pytest.raises(ValueError):
        db.add_user("id1","John")

def test_get_user(db):
    db.add_user("id1","John")
    assert db.get_user("id1")=="John"

def test_delete_user(db):
    db.add_user("id1","John")
    db.delete_user("id1")
    assert db.get_user("id1") is None

