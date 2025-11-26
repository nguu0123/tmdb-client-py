"""
tmdb_client_py.search
~~~~~~~~~~~~~~~~~
This module implements the Search functionality of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class Search(TMDB):
    """
    Search functionality

    See: https://developers.themoviedb.org/3/search
    """

    BASE_PATH = "search"
    URLS = {
        "company": "/company",
        "collection": "/collection",
        "keyword": "/keyword",
        "movie": "/movie",
        "multi": "/multi",
        "person": "/person",
        "tv": "/tv",
    }

    def company(self, query: str, page: int | None = None):
        """
        Search for companies.

        Args:
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("company")
        kwargs = {"query": query}
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def collection(
        self, query: str, language: str | None = None, page: int | None = None
    ):
        """
        Search for collections.

        Args:
            language: (optional) (optional) ISO 639-1 code.
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("collection")
        kwargs = {"query": query}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def keyword(self, query: str, page: int | None = None):
        """
        Search for keywords.

        Args:
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("keyword")
        kwargs = {"query": query}
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def movie(
        self,
        query: str,
        language: str | None = None,
        page: int | None = None,
        include_adult: bool | None = None,
        region: str | None = None,
        year: int | None = None,
        primary_release_year: int | None = None,
    ):
        """
        Search for movies.

        Args:
            language: (optional) (optional) ISO 639-1 code.
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.
            include_adult: (optional) Choose whether to include adult
                (pornography) content in the results.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.
            year: (optional) A filter to limit the results to a specific year
                (looking at all release dates).
            primary_release_year: (optional) A filter to limit the results to a
                specific primary release year.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("movie")
        kwargs = {"query": query}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if include_adult is not None:
            kwargs["include_adult"] = include_adult
        if region is not None:
            kwargs["region"] = region
        if year is not None:
            kwargs["year"] = year
        if primary_release_year is not None:
            kwargs["primary_release_year"] = primary_release_year

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def multi(
        self,
        query: str,
        language: str | None = None,
        page: int | None = None,
        include_adult: bool | None = None,
        region: str | None = None,
    ):
        """
        Search multiple models in a single request. Multi search currently
        supports searching for movies, tv shows and people in a single request.

        Args:
            language: (optional) (optional) ISO 639-1 code.
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.
            include_adult: (optional) Choose whether to include adult
                (pornography) content in the results.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("multi")
        kwargs = {"query": query}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if include_adult is not None:
            kwargs["include_adult"] = include_adult
        if region is not None:
            kwargs["region"] = region

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def person(
        self,
        query: str,
        language: str | None = None,
        page: int | None = None,
        include_adult: bool | None = None,
        region: str | None = None,
    ):
        """
        Search for people.

        Args:
            language: (optional) (optional) ISO 639-1 code.
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.
            include_adult: (optional) Choose whether to include adult
                (pornography) content in the results.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("person")
        kwargs = {"query": query}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if include_adult is not None:
            kwargs["include_adult"] = include_adult
        if region is not None:
            kwargs["region"] = region

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv(
        self,
        query: str,
        language: str | None = None,
        page: int | None = None,
        include_adult: bool | None = None,
        first_air_date_year: int | None = None,
    ):
        """
        Search for a TV show.

        Args:
            language: (optional) (optional) ISO 639-1 code.
            query: (required) Pass a text query to search. This value should be
                URI encoded.
            page: (optional) Minimum 1, maximum 1000, default 1.
            include_adult: (optional) Choose whether to include adult
                (pornography) content in the results.
            first_air_date_year: (optional) Filter the results to only match
                shows that have an air date with with value.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("tv")
        kwargs = {"query": query}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if include_adult is not None:
            kwargs["include_adult"] = include_adult
        if first_air_date_year is not None:
            kwargs["first_air_date_year"] = first_air_date_year

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
