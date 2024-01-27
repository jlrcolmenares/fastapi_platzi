import pytest
from pydantic import ValidationError

from ..models import Movie


class TestModels:
    def test_movie_with_valid_data(self):
        movie = Movie(
            id=1,
            title="Inception",
            overview="A thief who steals corporate secrets...",
            year=2010,
            rating=8.8,
            category="Sci-Fi",
        )
        assert movie.id == 1
        # ... (assert other fields)

    def test_movie_with_missing_required_fields(self):
        with pytest.raises(ValidationError):
            Movie(
                title="Inception",
                # Missing 'overview', 'year', 'rating', 'category'
            )

    def test_movie_with_wrong_data_types(self):
        with pytest.raises(ValidationError):
            Movie(
                id="not an integer",
                title=123,  # Should be a string
                overview="A thief who steals corporate secrets...",
                year="not an integer",
                rating="not a float",
                category=1234,  # Should be a string
            )
