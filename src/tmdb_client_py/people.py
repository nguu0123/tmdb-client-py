"""
tmdb_client_py.people
~~~~~~~~~~~~~~~~~
This module implements the People and Credits functionality of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class People(TMDB):
    """
    People functionality.

    See: https://developers.themoviedb.org/3/people
    """

    BASE_PATH = "person"
    URLS = {
        "info": "/{id}",
        "changes": "/{id}/changes",
        "movie_credits": "/{id}/movie_credits",
        "tv_credits": "/{id}/tv_credits",
        "combined_credits": "/{id}/combined_credits",
        "external_ids": "/{id}/external_ids",
        "images": "/{id}/images",
        "tagged_images": "/{id}/tagged_images",
        "translations": "/{id}/translations",
        "latest": "/latest",
        "popular": "/popular",
    }

    def __init__(self, id=0):
        super().__init__()
        self.id = id

    def info(self, language: str | None = None, append_to_response: str | None = None):
        """
        Get the primary person details by id.

        Supports append_to_response. Read more about this at
        https://developers.themoviedb.org/3/getting-started/append-to-response.

        Args:
            language: (optional) ISO 639-1 code.
            append_to_response: (optional) Append requests within the same
                namespace to the response.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("info")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if append_to_response is not None:
            kwargs["append_to_response"] = append_to_response

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def changes(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int | None = None,
    ):
        """
        Get the changes for a person. By default only the last 24 hours are returned.

        You can query up to 14 days in a single query by using the start_date
        and end_date query parameters.

        Args:
            start_date: (optional) Filter the results with a start date.
                Expected format is 'YYYY-MM-DD'.
            end_date: (optional) Filter the results with a end date.
                Expected format is 'YYYY-MM-DD'.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("changes")
        kwargs = {}
        if start_date is not None:
            kwargs["start_date"] = start_date
        if end_date is not None:
            kwargs["end_date"] = end_date
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movie_credits(self, language: str | None = None):
        """
        Get the movie credits for a person.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("movie_credits")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv_credits(self, language: str | None = None):
        """
        Get the TV show credits for a person.

        You can query for some extra details about the credit with the credit
        method.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("tv_credits")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def combined_credits(self, language: str | None = None):
        """
        Get the movie and TV credits together in a single response.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("combined_credits")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, language: str | None = None):
        """
        Get the external ids for a person. We currently support the following external sources.

        External Sources
            - IMDB ID
            - Facebook
            - Freebase MID
            - Freebase ID
            - Instagram
            - TVRage ID
            - Twitter

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("external_ids")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self):
        """
        Get the images for a person.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("images")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def translations(self, language: str | None = None):
        """
        Get a list of translations that have been created for a person.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("translations")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def latest(self, language: str | None = None):
        """
        Get the most newly created person. This is a live response and will
        continuously change.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("latest")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, language: str | None = None, page: int | None = None):
        """
        Get the list of popular people on TMDb. This list updates daily.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("popular")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Credits(TMDB):
    """
    Credits functionality.

    See: https://developers.themoviedb.org/3/credits
    """

    BASE_PATH = "credit"
    URLS = {
        "info": "/{credit_id}",
    }

    def __init__(self, credit_id):
        super().__init__()
        self.credit_id = credit_id

    def info(self):
        """
        Get a movie or TV credit details by id.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_credit_id_path("info")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def _get_credit_id_path(self, key):
        return self._get_path(key).format(credit_id=self.credit_id)
