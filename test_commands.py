# how would I test Barky?
# First, I wouldn't test barky, I would test the reusable modules barky relies on:
# commands.py and database.py

# we will use pytest: https://docs.pytest.org/en/stable/index.html

# should we test quit? No, its behavior is self-evident and not logic dependent
def test_quit_command():
    pass

# okay, should I test the other commands?
# not really, they are tighly coupled with sqlite3 and its use in the database.py module


from database import DatabaseManager
import sqlite3
import pytest
from datetime import datetime
db = DatabaseManager("bookmarks.db")

def test_add_bookmark_command():
    # Create a test bookmark
    url = "https://www.example.com"
    title = "Example Website"
    desc = "A website for examples"
    pass
    
def execute(self, data, timestamp=None):
        data["date_added"] = datetime.utcnow().isoformat()
        db.add("bookmarks", data)
        return "Bookmark added!"


def test_list_bookmarks_command():
    # Create some test bookmarks
    bookmarks = [
        {"url": "https://www.example1.com", "title": "Example 1", "description": "A website for examples"},
        {"url": "https://www.example2.com", "title": "Example 2", "description": "Another website for examples"},
        {"url": "https://www.example3.com", "title": "Example 3", "description": "Yet another website for examples"}
    ]

