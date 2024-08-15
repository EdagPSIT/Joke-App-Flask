# tests/test_app.py
import pytest
from src.app import app
from typing import Any


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_homepage(client: Any):
    """Test the homepage response and content."""

    response = client.get('/')
    assert response.status_code == 200
    assert b"LaughLab" in response.data


def test_joke_language_selection(client: Any):
    """Test joke generation for different languages."""

    languages = ['en', 'de', 'es']
    for lang in languages:
        response = client.get(f'/?lang={lang}')
        assert response.status_code == 200
        assert b"&#x1F602;" in response.data  # checking for the emoji in the joke
