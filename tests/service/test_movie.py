from unittest.mock import MagicMock

import pytest

from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(
        id=1,
        title="Movie_1",
        description="Description_1",
        trailer='Trailer_1',
        year=2000,
        rating=8.0,
        genre_id=1,
        director_id=1
    )

    movie_2 = Movie(
        id=2,
        title="Movie_2",
        description="Description_2",
        trailer="Trailer_2",
        year=2010,
        rating=10.0,
        genre_id=2,
        director_id=2
    )

    movie_3 = Movie(
        id=3,
        title="Movie_3",
        description="Description_3",
        trailer="Trailer_3",
        year=2020,
        rating=15.0,
        genre_id=3,
        director_id=3
    )

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()

    return movie_dao


class TestService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()

        assert len(movies) > 0

    def test_create_movie(self):
        create_movie = {
            "id": 4,
            "title": "Movie_4",
            "description": "Description_4",
            "trailer": "Trailer_4",
            "year": 2020,
            "rating": 100.0,
            "genre_id": 4,
            "director_id": 4
        }
        movie = self.movie_service.create(create_movie)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_update = {
            "id": 1,
            "title": "Movie_1_1",
            "description": "Description_1_1",
            "trailer": "Trailer_1",
            "year": 2000,
            "rating": 8.0,
            "genre_id": 1,
            "director_id": 1
        }
        self.movie_service.update(movie_update)
