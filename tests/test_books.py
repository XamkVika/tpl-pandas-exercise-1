import pandas as pd
import pytest
from main import load_data

@pytest.fixture
def df():
    test_file = ("data/books.csv")
    return load_data(test_file)

def test_load_data(df):
    # Should have 71 rows
    assert len(df) == 71

def test_unique_genres(df):
    genres = df["genre"].unique()
    assert "Fiction" in genres
    assert "Classic" in genres

def test_author_books(df):
    orwell_books = df[df["author"] == "George Orwell"]
    assert not orwell_books.empty
    assert "1984" in orwell_books["title"].values

def test_highest_rating(df):
    max_rating = df["rating"].max()
    assert max_rating >= 4.5  # sanity check