"""
tmdb_client_py.discover
~~~~~~~~~~~~~~~~~~~
This module implements the Discover functionality of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class Discover(TMDB):
    """
    Discover functionality.

    See: https://developers.themoviedb.org/3/discover
    """

    BASE_PATH = "discover"
    URLS = {
        "movie": "/movie",
        "tv": "/tv",
    }

    def movie(
        self,
        language: str | None = None,
        region: str | None = None,
        sort_by: str | None = None,
        certification_country: str | None = None,
        certification: str | None = None,
        certification_lte: str | None = None,
        certification_gte: str | None = None,
        include_adult: bool | None = None,
        include_video: bool | None = None,
        page: int | None = None,
        primary_release_year: int | None = None,
        primary_release_date_gte: str | None = None,
        primary_release_date_lte: str | None = None,
        release_date_gte: str | None = None,
        release_date_lte: str | None = None,
        year: int | None = None,
        vote_count_gte: int | None = None,
        vote_count_lte: int | None = None,
        vote_average_gte: float | None = None,
        vote_average_lte: float | None = None,
        with_cast: str | None = None,
        with_crew: str | None = None,
        with_people: str | None = None,
        with_companies: str | None = None,
        with_genres: str | None = None,
        without_genres: str | None = None,
        with_keywords: str | None = None,
        without_keywords: str | None = None,
        with_runtime_gte: int | None = None,
        with_runtime_lte: int | None = None,
        with_original_language: str | None = None,
        **kwargs,
    ):
        """
        Discover movies by different types of data like average rating, number
        of votes, genres and certifications. You can get a valid list of
        certifications from the certifications list method.

        Discover also supports a nice list of sort options. See below for all
        of the available options.

        Please note, when using certification / certification.lte you must also
        specify certification_country. These two parameters work together in
        order to filter the results. You can only filter results with the
        countries we have added to our certifications list.

        If you specify the region parameter, the regional release date will be
        used instead of the primary release date. The date returned will be the
        first date based on your query (ie. if a with_release_type is
        specified). It's important to note the order of the release types that
        are used. Specifying "2|3" would return the limited theatrical release
        date as opposed to "3|2" which would return the theatrical date.

        Also note that a number of filters support being comma (,) or pipe (|)
        separated. Comma's are treated like an AND and query while pipe's are
        an OR.

        Some examples of what can be done with discover can be found at
        https://www.themoviedb.org/documentation/api/discover.

        Args:
            language: (optional) ISO 639-1 code.
            region: (optional) Specify a ISO 3166-1 code.
            sort_by: (optional) Allowed values: popularity.asc,
                popularity.desc, release_date.asc, release_date.desc,
                revenue.asc, revenue.desc, primary_release_date.asc,
                primary_release_date.desc, original_title.asc,
                original_title.desc, vote_average.asc, vote_average.desc,
                vote_count.asc, vote_count.desc
                Default: popularity.desc
            certification_country: (optional) Used in conjunction with the
                certification filter, use this to specify a country with a
                valid certification.
            certification: Filter results with a valid certification from the
                'certification_country' field.
            certification.gte: Filter and only include movies that have a
                certification that is greater than or equal to the specified
                value.
            certification.lte: Filter and only include movies that have a
                certification that is less than or equal to the specified
                value.
            include_adult: (optional) A filter and include or exclude adult
                movies.
            include_video: (optional) A filter to include or exclude videos.
            page: (optional) Minimum 1, maximum 1000, default 1.
            primary_release_year: (optional) A filter to limit the results to a
                specific primary release year.
            primary_release_date.gte: (optional) Filter and only include movies
                that have a primary release date that is greater or equal to
                the specified value.
            primary_release_date.lte: (optional) Filter and only include movies
                that have a primary release date that is less than or equal to
                the specified value.
            release_date.gte: (optional) Filter and only include movies that
                have a primary release date that is greater or equal to the
                specified value.
            releaste_date.lte: (optional) Filter and only include movies that
                have a primary release date that is less than or equal to the
                specified value.
            with_release_type: (optional) Specify a comma (AND) or pipe (OR)
                separated value to filter release types by. These release types
                map to the same values found on the movie release date method.
                Minimum 1, maximum 6.
            year: (optional) A filter to limit the results to a specific year
                (looking at all release dates).
            vote_count.gte: (optional) Filter and only include movies that have
                a vote count that is greater or equal to the specified value.
                Minimum 0.
            vote_count.lte: (optional) Filter and only include movies that have
                a vote count that is less than or equal to the specified value.
                Minimum 1.
            vote_average.gte: (optional) Filter and only include movies that
                have a rating that is greater or equal to the specified value.
                Minimum 0.
            vote_average.lte: (optional) Filter and only include movies that
                have a rating that is less than or equal to the specified value.
                Minimum 0.
            with_cast: (optional) A comma separated list of person ID's. Only
                include movies that have one of the ID's added as an actor.
            with_crew: (optional) A comma separated list of person ID's. Only
                include movies that have one of the ID's added as a crew member.
            with_people: (optional) A comma separated list of person ID's. Only
                include movies that have one of the ID's added as a either a
                actor or a crew member.
            with_companies: (optional) A comma separated list of production
                company ID's. Only include movies that have one of the ID's
                added as a production company.
            with_genres: (optional) Comma separated value of genre ids that you
                want to include in the results.
            without_genres: (optional) Comma separated value of genre ids that
                you want to exclude from the results.
            with_keywords: (optional) A comma separated list of keyword ID's.
                Only includes movies that have one of the ID's added as a
                keyword.
            without_keywords: (optional) Exclude items with certain keywords.
                You can comma and pipe separate these values to create an 'AND' or 'OR' logic.
            with_runtime.gte: (optional) Filter and only include movies that
                have a runtime that is greater or equal to a value.
            with_runtime.lte: (optional) Filter and only include movies that
                have a runtime that is less than or equal to a value.
            with_original_language: (optional) Specify an ISO 639-1 string to
                filter results by their original language value.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        # Convert the direct parameters to the kwargs dict
        if language is not None:
            kwargs["language"] = language
        if region is not None:
            kwargs["region"] = region
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if certification_country is not None:
            kwargs["certification_country"] = certification_country
        if certification is not None:
            kwargs["certification"] = certification
        if certification_lte is not None:
            kwargs["certification.lte"] = certification_lte
        if certification_gte is not None:
            kwargs["certification.gte"] = certification_gte
        if include_adult is not None:
            kwargs["include_adult"] = include_adult
        if include_video is not None:
            kwargs["include_video"] = include_video
        if page is not None:
            kwargs["page"] = page
        if primary_release_year is not None:
            kwargs["primary_release_year"] = primary_release_year
        if primary_release_date_gte is not None:
            kwargs["primary_release_date.gte"] = primary_release_date_gte
        if primary_release_date_lte is not None:
            kwargs["primary_release_date.lte"] = primary_release_date_lte
        if release_date_gte is not None:
            kwargs["release_date.gte"] = release_date_gte
        if release_date_lte is not None:
            kwargs["release_date.lte"] = release_date_lte
        if year is not None:
            kwargs["year"] = year
        if vote_count_gte is not None:
            kwargs["vote_count.gte"] = vote_count_gte
        if vote_count_lte is not None:
            kwargs["vote_count.lte"] = vote_count_lte
        if vote_average_gte is not None:
            kwargs["vote_average.gte"] = vote_average_gte
        if vote_average_lte is not None:
            kwargs["vote_average.lte"] = vote_average_lte
        if with_cast is not None:
            kwargs["with_cast"] = with_cast
        if with_crew is not None:
            kwargs["with_crew"] = with_crew
        if with_people is not None:
            kwargs["with_people"] = with_people
        if with_companies is not None:
            kwargs["with_companies"] = with_companies
        if with_genres is not None:
            kwargs["with_genres"] = with_genres
        if without_genres is not None:
            kwargs["without_genres"] = without_genres
        if with_keywords is not None:
            kwargs["with_keywords"] = with_keywords
        if without_keywords is not None:
            kwargs["without_keywords"] = without_keywords
        if with_runtime_gte is not None:
            kwargs["with_runtime.gte"] = with_runtime_gte
        if with_runtime_lte is not None:
            kwargs["with_runtime.lte"] = with_runtime_lte
        if with_original_language is not None:
            kwargs["with_original_language"] = with_original_language

        # Periods are not allowed in keyword arguments but several API
        # arguments contain periods. See both usages in tests/test_discover.py.
        for param in dict(kwargs):
            if "_lte" in param:
                kwargs[param.replace("_lte", ".lte")] = kwargs.pop(param)
            if "_gte" in param:
                kwargs[param.replace("_gte", ".gte")] = kwargs.pop(param)

        path = self._get_path("movie")

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def tv(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        air_date_gte: str | None = None,
        air_date_lte: str | None = None,
        first_air_date_gte: str | None = None,
        first_air_date_lte: str | None = None,
        first_air_date_year: int | None = None,
        page: int | None = None,
        timezone: str | None = None,
        vote_average_gte: float | None = None,
        vote_count_gte: int | None = None,
        with_genres: str | None = None,
        with_networks: str | None = None,
        without_genres: str | None = None,
        with_runtime_gte: int | None = None,
        with_runtime_lte: int | None = None,
        include_null_first_air_dates: bool | None = None,
        with_original_language: str | None = None,
        without_keywords: str | None = None,
        screened_theatrically: bool | None = None,
        with_companies: str | None = None,
        with_keywords: str | None = None,
        **kwargs,
    ):
        """
        Discover TV shows by different types of data like average rating,
        number of votes, genres, the network they aired on and air dates.

        Discover also supports a nice list of sort options. See below for all
        of the available options.

        Also note that a number of filters support being comma (,) or pipe (|)
        separated. Comma's are treated like an AND and query while pipe's are
        an OR.

        Some examples of what can be done with discover can be found at
        https://www.themoviedb.org/documentation/api/discover.

        Args:
            language: (optional) ISO 639-1 code.
            sort_by: (optional) Available options are 'vote_average.desc',
                     'vote_average.asc', 'first_air_date.desc',
                     'first_air_date.asc', 'popularity.desc', 'popularity.asc'
            sort_by: (optional) Allowed values: vote_average.desc,
                vote_average.asc, first_air_date.desc, first_air_date.asc,
                popularity.desc, popularity.asc
                Default: popularity.desc
            air_date.gte: (optional) Filter and only include TV shows that have
                a air date (by looking at all episodes) that is greater or
                equal to the specified value.
            air_date.lte: (optional) Filter and only include TV shows that have
                a air date (by looking at all episodes) that is less than or
                equal to the specified value.
            first_air_date.gte: (optional) Filter and only include TV shows
                that have a original air date that is greater or equal to the
                specified value. Can be used in conjunction with the
                "include_null_first_air_dates" filter if you want to include
                items with no air date.
            first_air_date.lte: (optional) Filter and only include TV shows
                that have a original air date that is less than or equal to the
                specified value. Can be used in conjunction with the
                "include_null_first_air_dates" filter if you want to include
                items with no air date.
            first_air_date_year: (optional) Filter and only include TV shows
                that have a original air date year that equal to the specified
                value. Can be used in conjunction with the
                "include_null_first_air_dates" filter if you want to include
                items with no air date.
            page: (optional) Specify the page of results to query. Default 1.
            timezone: (optional) Used in conjunction with the air_date.gte/lte
                filter to calculate the proper UTC offset. Default
                America/New_York.
            vote_average.gte: (optional) Filter and only include movies that
                have a rating that is greater or equal to the specified value.
                Minimum 0.
            vote_count.gte: (optional) Filter and only include movies that have
                a rating that is less than or equal to the specified value.
                Minimum 0.
            with_genres: (optional) Comma separated value of genre ids that you
                want to include in the results.
            with_networks: (optional) Comma separated value of network ids that
                you want to include in the results.
            without_genres: (optional) Comma separated value of genre ids that
                you want to exclude from the results.
            with_runtime.gte: (optional) Filter and only include TV shows with
                an episode runtime that is greater than or equal to a value.
            with_runtime.lte: (optional) Filter and only include TV shows with
                an episode runtime that is less than or equal to a value.
            include_null_first_air_dates: (optional) Use this filter to include
                TV shows that don't have an air date while using any of the
                "first_air_date" filters.
            with_original_language: (optional) Specify an ISO 639-1 string to
                filter results by their original language value.
            without_keywords: (optional) Exclude items with certain keywords.
                You can comma and pipe separate these values to create an 'AND'
                or 'OR' logic.
            screened_theatrically: (optional) Filter results to include items
                that have been screened theatrically.
            with_companies: (optional) A comma separated list of production
                company ID's. Only include movies that have one of the ID's
                added as a production company.
            with_keywords: (optional) A comma separated list of keyword ID's.
                Only includes TV shows that have one of the ID's added as a
                keyword.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        # Convert the direct parameters to the kwargs dict
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if air_date_gte is not None:
            kwargs["air_date.gte"] = air_date_gte
        if air_date_lte is not None:
            kwargs["air_date.lte"] = air_date_lte
        if first_air_date_gte is not None:
            kwargs["first_air_date.gte"] = first_air_date_gte
        if first_air_date_lte is not None:
            kwargs["first_air_date.lte"] = first_air_date_lte
        if first_air_date_year is not None:
            kwargs["first_air_date_year"] = first_air_date_year
        if page is not None:
            kwargs["page"] = page
        if timezone is not None:
            kwargs["timezone"] = timezone
        if vote_average_gte is not None:
            kwargs["vote_average.gte"] = vote_average_gte
        if vote_count_gte is not None:
            kwargs["vote_count.gte"] = vote_count_gte
        if with_genres is not None:
            kwargs["with_genres"] = with_genres
        if with_networks is not None:
            kwargs["with_networks"] = with_networks
        if without_genres is not None:
            kwargs["without_genres"] = without_genres
        if with_runtime_gte is not None:
            kwargs["with_runtime.gte"] = with_runtime_gte
        if with_runtime_lte is not None:
            kwargs["with_runtime.lte"] = with_runtime_lte
        if include_null_first_air_dates is not None:
            kwargs["include_null_first_air_dates"] = include_null_first_air_dates
        if with_original_language is not None:
            kwargs["with_original_language"] = with_original_language
        if without_keywords is not None:
            kwargs["without_keywords"] = without_keywords
        if screened_theatrically is not None:
            kwargs["screened_theatrically"] = screened_theatrically
        if with_companies is not None:
            kwargs["with_companies"] = with_companies
        if with_keywords is not None:
            kwargs["with_keywords"] = with_keywords

        # Periods are not allowed in keyword arguments but several API
        # arguments contain periods. See both usages in tests/test_discover.py.
        for param in dict(kwargs):
            if "_lte" in param:
                kwargs[param.replace("_lte", ".lte")] = kwargs.pop(param)
            if "_gte" in param:
                kwargs[param.replace("_gte", ".gte")] = kwargs.pop(param)

        path = self._get_path("tv")

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response
