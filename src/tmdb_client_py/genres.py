"""
tmdb_client_py.genres
~~~~~~~~~~~~~~~~~
This module implements the Genres functionality of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class Genres(TMDB):
    """
    Genres functionality.

    See: https://developers.themoviedb.org/3/genres
    """

    BASE_PATH = "genre"
    URLS = {
        "movie_list": "/movie/list",
        "tv_list": "/tv/list",
        "movies": "/{id}/movies",  # backward compatibility
    }

    def __init__(self, id=0):
        super().__init__()
        self.id = id

    def movie_list(self, language: str | None = None):
        """
        Get the list of official genres for movies.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("movie_list")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv_list(self, language: str | None = None):
        """
        Get the list of official genres for TV shows.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("tv_list")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    # backward compatibility
    def movies(
        self,
        page: int | None = None,
        language: str | None = None,
        include_all_movies: bool | None = None,
        include_adult: bool | None = None,
    ):
        """
        Get the list of movies for a particular genre by id. By default, only
        movies with 10 or more votes are included.

        Args:
            page: (optional) Minimum 1, maximum 1000.
            language: (optional) ISO 639-1 code.
            include_all_movies: (optional) Toggle the inclusion of all movies
                                and not just those with 10 or more ratings.
                                Expected value is: True or False.
            include_adult: (optional) Toggle the inclusion of adult titles.
                           Expected value is: True or False.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("movies")
        kwargs = {}
        if page is not None:
            kwargs["page"] = page
        if language is not None:
            kwargs["language"] = language
        if include_all_movies is not None:
            kwargs["include_all_movies"] = include_all_movies
        if include_adult is not None:
            kwargs["include_adult"] = include_adult

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
