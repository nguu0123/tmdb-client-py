"""
tmdb_client_py.movies
~~~~~~~~~~~~~~~~~
This module implements the Movies, Collections, Companies, Keywords, and
Reviews functionality of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class Movies(TMDB):
    """
    Movies functionality.

    See: https://developers.themoviedb.org/3/movies
    """

    BASE_PATH = "movie"
    URLS = {
        "details": "/{id}",
        "account_states": "/{id}/account_states",
        "alternative_titles": "/{id}/alternative_titles",
        "changes": "/{id}/changes",
        "credits": "/{id}/credits",
        "external_ids": "/{id}/external_ids",
        "images": "/{id}/images",
        "keywords": "/{id}/keywords",
        "lists": "/{id}/lists",
        "recommendations": "/{id}/recommendations",
        "release_dates": "/{id}/release_dates",
        "reviews": "/{id}/reviews",
        "similar_movies": "/{id}/similar_movies",
        "translations": "/{id}/translations",
        "videos": "/{id}/videos",
        "watch_providers": "/{id}/watch/providers",
        "rating": "/{id}/rating",
        "rating_delete": "/{id}/rating",
        "latest": "/latest",
        "now_playing": "/now_playing",
        "popular": "/popular",
        "top_rated": "/top_rated",
        "upcoming": "/upcoming",
        "releases": "/{id}/releases",  # backward compatibility
    }

    def __init__(self, id=0):
        super().__init__()
        self.id = id

    def details(
        self, language: str | None = None, append_to_response: str | None = None
    ):
        """
        Get the primary information about a movie.

        Supports append_to_response. Read more about this at
        https://developers.themoviedb.org/3/getting-started/append-to-response.

        Args:
            language: (optional) ISO 639-1 code.
            append_to_response: (optional) Append requests within the same
                namespace to the response.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("details")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if append_to_response is not None:
            kwargs["append_to_response"] = append_to_response

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def account_states(self, session_id: str, guest_session_id: str | None = None):
        """
        Grab the following account states for a session:
            - Movie rating
            - If it belongs to your watchlist
            - If it belongs to your favourite list

        Args:
            session_id: (required) See Authentication.
            guest_session_id: (optional) See Authentication.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("account_states")
        kwargs = {"session_id": session_id}
        if guest_session_id is not None:
            kwargs["guest_session_id"] = guest_session_id

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def alternative_titles(self, country: str | None = None):
        """
        Get all of the alternative titles for a movie.

        Args:
            country: (optional) ISO 3166-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("alternative_titles")
        kwargs = {}
        if country is not None:
            kwargs["country"] = country

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
        Get the changes for a movie. By default only the last 24 hours are returned.

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

    def credits(self):
        """
        Get the cast and crew for a movie.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("credits")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self):
        """
        Get the external ids for a movie. We currently support the following
        external sources.

        Media Databases - IMDb
        Social IDs - Facebok, Instagram, Twitter

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("external_ids")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def images(
        self, language: str | None = None, include_image_language: str | None = None
    ):
        """
        Get the images that belong to a movie.

        Querying images with a language parameter will filter the results. If
        you want to include a fallback language (especially useful for
        backdrops) you can use the include_image_language parameter. This
        should be a comma separated value like so:
        include_image_language=en,null.

        Args:
            language: (optional) ISO 639-1 code.
            include_image_language: (optional) Comma separated, a valid
                                    ISO 69-1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("images")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if include_image_language is not None:
            kwargs["include_image_language"] = include_image_language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def keywords(self):
        """
        Get the keywords that have been added to a movie.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("keywords")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def lists(self, language: str | None = None, page: int | None = None):
        """
        Get a list of lists that this movie belongs to.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("lists")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def recommendations(self, language: str | None = None, page: int | None = None):
        """
        Get a list of recommended movies for a movie.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("recommendations")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def release_dates(self):
        """
        Get the release date along with the certification for a movie.

        Release dates support different types:

            1. Premiere
            2. Theatrical (limited)
            3. Theatrical
            4. Digital
            5. Physical
            6. TV

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("release_dates")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def reviews(self, language: str | None = None, page: int | None = None):
        """
        Get the user reviews for a movie.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("reviews")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def similar_movies(self, language: str | None = None, page: int | None = None):
        """
        Get a list of similar movies. This is not the same as the
        "Recommendation" system you see on the website.

        These items are assembled by looking at keywords and genres.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("similar_movies")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def translations(self):
        """
        Get a list of translations that have been created for a movie.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("translations")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def videos(self, language: str | None = None):
        """
        Get the videos that have been added to a movie.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("videos")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watch_providers(self):
        """
        Get a list of the availabilities per country by provider for movies.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("watch_providers")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def rating(
        self,
        value: float,
        session_id: str | None = None,
        guest_session_id: str | None = None,
    ):
        """
        Rate a movie.

        A valid session or guest session ID is required. You can read more
        about how this works at
        https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

        Args:
            session_id: (optional) See Authentication.
            guest_session_id: (optional) See Authentication.
            value: (required) This is the value of the rating you want to
                submit. The value is expected to be between 0.5 and 10.0.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("rating")
        kwargs = {}
        if session_id is not None:
            kwargs["session_id"] = session_id
        if guest_session_id is not None:
            kwargs["guest_session_id"] = guest_session_id

        payload = {
            "value": value,
        }

        response = self._POST(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def rating_delete(
        self, session_id: str | None = None, guest_session_id: str | None = None
    ):
        """
        Remove your rating for a movie.

        A valid session or guest session ID is required. You can read more
        about how this works at
        https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

        Args:
            session_id: (optional) See Authentication.
            guest_session_id: (optional) See Authentication.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("rating_delete")
        kwargs = {}
        if session_id is not None:
            kwargs["session_id"] = session_id
        if guest_session_id is not None:
            kwargs["guest_session_id"] = guest_session_id

        response = self._DELETE(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def latest(self, language: str | None = None):
        """
        Get the most newly created movie. This is a live response and will
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

    def now_playing(
        self,
        language: str | None = None,
        page: int | None = None,
        region: str | None = None,
    ):
        """
        Get a list of movies in theatres. This is a release type query that
        looks for all movies that have a release type of 2 or 3 within the
        specified date range.

        You can optionally specify a region parameter which will narrow the
        search to only look for theatrical release dates within the specified
        country.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("now_playing")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if region is not None:
            kwargs["region"] = region

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(
        self,
        language: str | None = None,
        page: int | None = None,
        region: str | None = None,
    ):
        """
        Get a list of the current popular movies on TMDb. This list updates
        daily.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("popular")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if region is not None:
            kwargs["region"] = region

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def top_rated(
        self,
        language: str | None = None,
        page: int | None = None,
        region: str | None = None,
    ):
        """
        Get the top rated movies on TMDb.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("top_rated")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if region is not None:
            kwargs["region"] = region

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def upcoming(
        self,
        language: str | None = None,
        page: int | None = None,
        region: str | None = None,
    ):
        """
        Get a list of upcoming movies in theatres. This is a release type query
        that looks for all movies that have a release type of 2 or 3 within the
        specified date range.

        You can optionally specify a region parameter which will narrow the
        search to only look for theatrical release dates within the specified
        country.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.
            region: (optional) Specify a ISO 3166-1 code to filter release
                dates. Must be uppercase.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("upcoming")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page
        if region is not None:
            kwargs["region"] = region

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    # backward compatibility
    def releases(self):
        """
        Get the release date and certification information by country for a
        specific movie id.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("releases")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response


class Collections(TMDB):
    """
    Collections functionality.

    See: https://developers.themoviedb.org/3/collections
    """

    BASE_PATH = "collection"
    URLS = {
        "info": "/{id}",
        "images": "/{id}/images",
        "translations": "/{id}/translations",
    }

    def __init__(self, id):
        super().__init__()
        self.id = id

    def info(self, language: str | None = None):
        """
        Get collection details by id.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("info")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(self, language: str | None = None):
        """
        Get the images for a collection by id.

        Args:
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("images")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def translations(self, language: str | None = None):
        """
        Get a list of the translations for a collection by id.

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


class Companies(TMDB):
    """
    Companies functionality.

    See: https://developers.themoviedb.org/3/companies
    """

    BASE_PATH = "company"
    URLS = {
        "info": "/{id}",
        "alternative_names": "/{id}/alternative_names",
        "images": "/{id}/images",
        "movies": "/{id}/movies",  # backward compatibility
    }

    def __init__(self, id=0):
        super().__init__()
        self.id = id

    def info(self):
        """
        Get a companies details by id.

        Args:

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("info")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def alternative_names(self):
        """
        Get the alternative names of a company.

        Args:

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("alternative_names")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def images(self):
        """
        Get a company's logos by id.

        There are two image formats that are supported for companies, PNG's and
        SVG's. You can see which type the original file is by looking at the
        file_type field. We prefer SVG's as they are resolution independent and
        as such, the width and height are only there to reflect the original
        asset that was uploaded.  An SVG can be scaled properly beyond those
        dimensions if you call them as a PNG.

        For more information about how SVG's and PNG's can be used, take a read
        through https://developers.themoviedb.org/3/getting-started/images.

        Args:

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("images")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    # backward compatibility
    def movies(self, language: str | None = None, page: int | None = None):
        """
        Get the list of movies associated with a particular company.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum value of 1.  Expected value is an integer.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("movies")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Keywords(TMDB):
    """
    Keywords functionality.

    See: https://developers.themoviedb.org/3/keywords
    """

    BASE_PATH = "keyword"
    URLS = {
        "info": "/{id}",
        "movies": "/{id}/movies",
    }

    def __init__(self, id):
        super().__init__()
        self.id = id

    def info(self):
        """
        Get the details of a keyword.

        Args:
           None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("info")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def movies(self, language: str | None = None, include_adult: bool | None = None):
        """
        Get the movies that belong to a keyword.

        We highly recommend using movie discover instead of this method as it
        is much more flexible.

        Args:
            language: (optional) ISO 639-1 code.
            include_adult: Choose whether to include adult (pornography)
                content in the results.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("movies")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if include_adult is not None:
            kwargs["include_adult"] = include_adult

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Reviews(TMDB):
    """
    Reviews functionality.

    See: https://developers.themoviedb.org/3/reviews
    """

    BASE_PATH = "review"
    URLS = {
        "info": "/{id}",
    }

    def __init__(self, id):
        super().__init__()
        self.id = id

    def info(self):
        """
        Get the review details by id.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("info")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response
