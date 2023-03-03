# how would I test Barky?
# First, I wouldn't test barky, I would test the reusable modules barky relies on:
# commands.py and database.py

# we will use pytest: https://docs.pytest.org/en/stable/index.html

# should we test quit? No, its behavior is self-evident and not logic dependent
#def test_quit_command():
#    pass

# okay, should I test the other commands?
# not really, they are tighly coupled with sqlite3 and its use in the database.py module

from commands import AddBookmarkCommand, ListBookmarksCommand, EditBookmarkCommand, DeleteBookmarkCommand
from database import DatabaseManager
import sqlite3
import pytest


@pytest.fixture
def db_handler():
    # Set up a test database
    db_handler = DatabaseManager(":memory:")
    return db_handler


def test_add_bookmark_command(db_handler):
    # Create a test bookmark
    url = "https://www.example.com"
    title = "Example Website"
    desc = "A website for examples"
    
    # Create an AddBookmarkCommand object and execute it
    add_command = AddBookmarkCommand(url, title, desc)
    add_command.execute(db_handler)
    
    # Retrieve the bookmark from the database
    list_command = ListBookmarksCommand()
    list_command.execute(db_handler)
    bookmarks = list_command.bookmarks
    
    # Check that the bookmark was added to the database
    assert len(bookmarks) == 1
    assert bookmarks[0]["url"] == url
    assert bookmarks[0]["title"] == title
    assert bookmarks[0]["description"] == desc



def test_list_bookmarks_command(db_handler):
    # Create some test bookmarks
    bookmarks = [
        {"url": "https://www.example1.com", "title": "Example 1", "description": "A website for examples"},
        {"url": "https://www.example2.com", "title": "Example 2", "description": "Another website for examples"},
        {"url": "https://www.example3.com", "title": "Example 3", "description": "Yet another website for examples"}
    ]

