"""
tmdb_client_py.account
~~~~~~~~~~~~~~~~~~
This module implements the Account, Authentication, and Lists functionality
of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class Account(TMDB):
    """
    Account functionality.

    See: https://developers.themoviedb.org/3/account
         https://www.themoviedb.org/documentation/api/sessions
    """

    BASE_PATH = "account"
    URLS = {
        "info": "",
        "lists": "/{id}/lists",
        "favorite_movies": "/{id}/favorite/movies",
        "favorite_tv": "/{id}/favorite/tv",
        "favorite": "/{id}/favorite",
        "rated_movies": "/{id}/rated/movies",
        "rated_tv": "/{id}/rated/tv",
        "rated_tv_episodes": "/{id}/rated/tv/episodes",
        "watchlist_movies": "/{id}/watchlist/movies",
        "watchlist_tv": "/{id}/watchlist/tv",
        "watchlist": "/{id}/watchlist",
    }

    def __init__(self, session_id):
        super().__init__()
        self.session_id = session_id

    def info(self):
        """
        Get your account details.

        Args:

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("info")

        response = self._GET(path)
        self.id = response["id"]
        self._set_attrs_to_values(response)
        return response

    def lists(self, language: str | None = None, page: int | None = None):
        """
        Get all of the lists created by an account. Will include private lists
        if you are the owner.

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

    def favorite_movies(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
    ):
        """
        Get the list of your favorite movies.

        Args:
            language: (optional) ISO 639-1 code.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("favorite_movies")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def favorite_tv(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
    ):
        """
        Get the list of your favorite TV shows.

        Args:
            language: (optional) ISO 639-1 code.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("favorite_tv")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def favorite(self, media_type: str, media_id: int, favorite: bool):
        """
        This method allows you to mark a movie or TV show as a favorite item.

        Args:
            media_type: 'movie' | 'tv'
            media_id: The id of the media.
            favorite: True (to add) | False (to remove).

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("favorite")

        payload = {
            "media_type": media_type,
            "media_id": media_id,
            "favorite": favorite,
        }

        response = self._POST(path, {}, payload)
        self._set_attrs_to_values(response)
        return response

    def rated_movies(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
    ):
        """
        Get a list of all the movies you have rated.

        Args:
            language: (optional) ISO 639-1 value.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("rated_movies")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def rated_tv(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
    ):
        """
        Get a list of all the TV shows you have rated.

        Args:
            language: (optional) ISO 639-1 value.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("rated_tv")
        kwargs = {"session_id": self.session_id}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def rated_tv_episodes(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
    ):
        """
        Get a list of all the TV episodes you have rated.

        Args:
            language: (optional) ISO 639-1 value.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("rated_tv_episodes")
        kwargs = {"session_id": self.session_id}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watchlist_movies(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
    ):
        """
        Get a list of all the movies you have added to your watchlist.

        Args:
            language: (optional) ISO 639-1 value.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("watchlist_movies")
        kwargs = {"session_id": self.session_id}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watchlist_tv(
        self,
        language: str | None = None,
        sort_by: str | None = None,
        page: int | None = None,
    ):
        """
        Get a list of all the TV shows you have added to your watchlist.

        Args:
            language: (optional) ISO 639-1 value.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("watchlist_tv")
        kwargs = {"session_id": self.session_id}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def watchlist(self, media_type: str, media_id: int, watchlist: bool):
        """
        Add a movie or TV show to your watchlist.

        Args:
            media_type: 'movie' | 'tv'
            media_id: The id of the media.
            watchlist: True (to add) | False (to remove).

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("watchlist")
        kwargs = {"session_id": self.session_id}

        payload = {
            "media_type": media_type,
            "media_id": media_id,
            "watchlist": watchlist,
        }

        response = self._POST(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response


class Authentication(TMDB):
    """
    Authentication functionality.

    See: https://developers.themoviedb.org/3/authentication
         https://www.themoviedb.org/documentation/api/sessions
    """

    BASE_PATH = "authentication"
    URLS = {
        "guest_session_new": "/guest_session/new",
        "token_new": "/token/new",
        "session_new": "/session/new",
        "token_validate_with_login": "/token/validate_with_login",
        "session_delete": "/session",
    }

    def guest_session_new(self):
        """
        This method will let you create a new guest session. Guest sessions
        are a type of session that will let a user rate movies and TV shows
        but not require them to have a TMDb user account. More
        information about user authentication can be found here
        (https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id).

        Please note, you should only generate a single guest session per
        user (or device) as you will be able to attach the ratings to a
        TMDb user account in the future. There is also IP limits in place
        so you should always make sure it's the end user doing the guest
        session actions.

        If a guest session is not used for the first time within 24 hours,
        it will be automatically deleted.

        Args:

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("guest_session_new")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def token_new(self):
        """
        Create a temporary request token that can be used to validate a TMDb
        user login. More details about how this works can be found here
        (https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id).

        Args:

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("token_new")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def session_new(self, request_token: str | None = None):
        """
        You can use this method to create a fully valid session ID once a user
        has validated the request token. More information about how this works
        can be found here
        (https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id).

        Args:
            request_token: The token you generated for the user to approve.
                           The token needs to be approved before being
                           used here.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("session_new")
        kwargs = {}
        if request_token is not None:
            kwargs["request_token"] = request_token

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def token_validate_with_login(
        self, username: str, password: str, request_token: str
    ):
        """
        This method allows an application to validate a request token by entering
        a username and password.

        Not all applications have access to a web view so this can be used as a
        substitute.

        Please note, the preferred method of validating a request token is to
        have a user authenticate the request via the TMDb website. You can read
        about that method here
        (https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id).

        If you decide to use this method please use HTTPS.

        Args:
            username: The user's username on TMDb.
            password: The user's password on TMDb.
            request_token: The token you generated for the user to approve.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("token_validate_with_login")
        kwargs = {
            "username": username,
            "password": password,
            "request_token": request_token,
        }

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def session_delete(self, session_id: str):
        """
        If you would like to delete (or "logout") from a session, call this
        method with a valid session ID.

        Args:

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("session_delete")

        payload = {
            "session_id": session_id,
        }

        response = self._DELETE(path, {}, payload)
        self._set_attrs_to_values(response)
        return response


class GuestSessions(TMDB):
    """
    Guest Sessions functionality.

    See: https://developers.themoviedb.org/3/guest-sessions
    """

    BASE_PATH = "guest_session"
    URLS = {
        "rated_movies": "/{guest_session_id}/rated/movies",
        "rated_tv": "/{guest_session_id}/rated/tv",
        "rated_tv_episodes": "/{guest_session_id}/rated/tv/episodes",
    }

    def __init__(self, guest_session_id=0):
        super().__init__()
        self.guest_session_id = guest_session_id

    def _get_guest_session_id_path(self, key):
        return self._get_path(key).format(guest_session_id=self.guest_session_id)

    def rated_movies(self, language: str | None = None, sort_by: str | None = None):
        """
        Get the rated movies for a guest session.

        Args:
            language: (optional) ISO 639-1 code.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_guest_session_id_path("rated_movies")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def rated_tv(self, language: str | None = None, sort_by: str | None = None):
        """
        Get the rated TV shows for a guest session.

        Args:
            language: (optional) ISO 639-1 code.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_guest_session_id_path("rated_tv")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def rated_tv_episodes(
        self, language: str | None = None, sort_by: str | None = None
    ):
        """
        Get the rated TV episodes for a guest session.

        Args:
            language: (optional) ISO 639-1 code.
            sort_by: (optional) Allowed Values: created_at.asc, created_at.desc

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_guest_session_id_path("rated_tv_episodes")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if sort_by is not None:
            kwargs["sort_by"] = sort_by

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class Lists(TMDB):
    """
    Lists functionality.

    See: https://developers.themoviedb.org/3/lists
    """

    BASE_PATH = "list"
    URLS = {
        "info": "/{id}",
        "item_status": "/{id}/item_status",
        "list_create": "",
        "add_item": "/{id}/add_item",
        "remove_item": "/{id}/remove_item",
        "list_clear": "/{id}/clear",
        "list_delete": "/{id}",
    }

    def __init__(self, id=0, session_id=0):
        super().__init__()
        self.id = id
        self.session_id = session_id
        self.list_id: int | None = None

    def info(self, language: str | None = None):
        """
        Get the details of a list.

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

    def item_status(self, movie_id: int):
        """
        You can use this method to check if a movie has already been added to
        the list.

        Args:
            movie_id: The id of the movie.  Minimum 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("item_status")
        kwargs = {"movie_id": movie_id}

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def list_create(self, name: str, description: str, language: str | None = None):
        """
        Create a list.

        Args:
            name: Name of the list.
            description: Description of the list.
            language: (optional) ISO 639-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("list_create")
        kwargs = {"session_id": self.session_id}

        payload = {
            "name": name,
            "description": description,
            "language": language,
        }

        response = self._POST(path, kwargs, payload)
        self._set_attrs_to_values(response)
        self.id = self.list_id
        return response

    def add_item(self, media_id: int):
        """
        Add a movie to a list.

        Args:
            media_id: A movie id.  Minimum 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("add_item")
        kwargs = {"session_id": self.session_id}

        payload = {
            "media_id": media_id,
        }

        response = self._POST(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def remove_item(self, media_id: int):
        """
        Remove a movie from a list.

        Args:
            media_id: A movie id.  Minimum 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("remove_item")
        kwargs = {"session_id": self.session_id}

        payload = {
            "media_id": media_id,
        }

        response = self._POST(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def list_clear(self, confirm: bool):
        """
        Clear all of the items from a list.

        Args:
            confirm: True (do it) | False (don't do it)

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("list_clear")
        kwargs = {"session_id": self.session_id, "confirm": str(confirm).lower()}

        payload = {}

        response = self._POST(path, kwargs, payload)
        self._set_attrs_to_values(response)
        return response

    def list_delete(self):
        """
        Delete a list.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("list_delete")
        kwargs = {"session_id": self.session_id}

        response = self._DELETE(path, kwargs)
        self._set_attrs_to_values(response)
        return response
