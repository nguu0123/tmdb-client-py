"""
tmdb_client_py.tv
~~~~~~~~~~~~~
This module implements the TV, TV Seasons, TV Episodes, and Networks
functionality of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

from .base import TMDB


class TV(TMDB):
    """
    TV functionality.

    See: https://developers.themoviedb.org/3/tv
    """

    BASE_PATH = "tv"
    URLS = {
        "info": "/{id}",
        "account_states": "/{id}/account_states",
        "alternative_titles": "/{id}/alternative_titles",
        "content_ratings": "/{id}/content_ratings",
        "credits": "/{id}/credits",
        "episode_groups": "/{id}/episode_groups",
        "external_ids": "/{id}/external_ids",
        "images": "/{id}/images",
        "keywords": "/{id}/keywords",
        "recommendations": "/{id}/recommendations",
        "reviews": "/{id}/reviews",
        "screened_theatrically": "/{id}/screened_theatrically",
        "similar": "/{id}/similar",
        "translations": "/{id}/translations",
        "videos": "/{id}/videos",
        "watch_providers": "/{id}/watch/providers",
        "rating": "/{id}/rating",
        "rating_delete": "/{id}/rating",
        "latest": "/latest",
        "airing_today": "/airing_today",
        "on_the_air": "/on_the_air",
        "popular": "/popular",
        "top_rated": "/top_rated",
    }

    def __init__(self, id=0):
        super().__init__()
        self.id = id

    def info(self, language: str | None = None, append_to_response: str | None = None):
        """
        Get the primary TV show details by id.

        Supports append_to_response. Read more about this at
        https://developers.themoviedb.org/3/getting-started/append-to-response.

        Args:
            language: (optional) ISO 639 code.
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

    def account_states(
        self,
        session_id: str,
        language: str | None = None,
        guest_session_id: str | None = None,
    ):
        """
        Grab the following account states for a session:
            - TV show rating
            - If it belongs to your watchlist
            - If it belongs to your favourite list

        Args:
            language: (optional) ISO 3166-1 code.
            session_id: (required) See Authentication.
            guest_session_id: (optional) See Authentication.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("account_states")
        kwargs = {"session_id": session_id}
        if language is not None:
            kwargs["language"] = language
        if guest_session_id is not None:
            kwargs["guest_session_id"] = guest_session_id

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def alternative_titles(self, language: str | None = None):
        """
        Returns all of the alternative titles for a TV show.

        Args:
            language: (optional) ISO 3166-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("alternative_titles")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def content_ratings(self, language: str | None = None):
        """
        Get the list of content ratings (certifications) that have been added
        to a TV show.

        Args:
            language: (optional) ISO 3166-1 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("content_ratings")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, language: str | None = None):
        """
        Get the credits (cast and crew) that have been added to a TV show.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("credits")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def episode_groups(self, language: str | None = None):
        """
        Get all of the episode groups that have been created for a TV show.
        With a group ID you can call the get TV episode group details  method.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("episode_groups")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, language: str | None = None):
        """
        Get the external ids for a TV show. We currently support the following
        external sources.

        Media Databases: IMDb ID, TVDB ID, Freebase MID*, Freebase ID*, TVRage
        ID*
        Social IDs: Facebook, Instagram, Twitter

        *Defunct or no longer available as a service.

        Args:
            language: (optional) ISO 639 code.

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

    def images(
        self, language: str | None = None, include_image_language: str | None = None
    ):
        """
        Get the images that belong to a TV show.

        Querying images with a language parameter will filter the results. If
        you want to include a fallback language (especially useful for
        backdrops) you can use the include_image_language parameter. This
        should be a comma separated value like so:
        include_image_language=en,null.

        Args:
            language: (optional) ISO 639 code.

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
        Get the keywords that have been added to a TV show.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("keywords")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def recommendations(self, language: str | None = None, page: int | None = None):
        """
        Get the list of TV show recommendations for this item.

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

    def reviews(self, language: str | None = None, page: int | None = None):
        """
        Get the reviews for a TV show.

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

    def screened_theatrically(self):
        """
        Get a list of seasons or episodes that have been screened in a film
        festival or theatre.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("screened_theatrically")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def similar(self, language: str | None = None, page: int | None = None):
        """
        Get a list of similar TV shows. These items are assembled by looking at
        keywords and genres.

        Args:
            language: (optional) ISO 639-1 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("similar")
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
        Get a list of the translations that exist for a TV show.

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
        Get the videos that have been added to a TV show.

        Args:
            language: (optional) ISO 639 code.

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
        Get a list of the availabilities per country by provider for tv.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("watch_providers")

        response = self._GET(path)
        self._set_attrs_to_values(response)

    def rating(
        self,
        value: float,
        session_id: str | None = None,
        guest_session_id: str | None = None,
    ):
        """
        Rate a TV show.

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
        Remove your rating for a TV show.

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
        Get the most newly created TV show. This is a live response and will
        continuously change.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("latest")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def airing_today(self, language: str | None = None, page: int | None = None):
        """
        Get a list of TV shows that are airing today. This query is purely day
        based as we do not currently support airing times.

        You can specify a timezone to offset the day calculation. Without a
        specified timezone, this query defaults to EST (Eastern Time
        UTC-05:00).

        Args:
            language: (optional) ISO 639 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("airing_today")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def on_the_air(self, language: str | None = None, page: int | None = None):
        """
        Get a list of shows that are currently on the air.

        This query looks for any TV show that has an episode with an air date
        in the next 7 days.

        Args:
            language: (optional) ISO 639 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("on_the_air")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def popular(self, language: str | None = None, page: int | None = None):
        """
        Get a list of the current popular TV shows on TMDb. This list updates
        daily.

        Args:
            language: (optional) ISO 639 code.
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

    def top_rated(self, language: str | None = None, page: int | None = None):
        """
        Get a list of the top rated TV shows on TMDb.

        Args:
            language: (optional) ISO 639 code.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_path("top_rated")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if page is not None:
            kwargs["page"] = page

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response


class TV_Seasons(TMDB):
    """
    TV Seasons functionality.

    See: https://developers.themoviedb.org/3/tv-seasons
    """

    BASE_PATH = "tv/{tv_id}/season/{season_number}"
    URLS = {
        "info": "",
        "account_states": "/account_states",
        "credits": "/credits",
        "external_ids": "/external_ids",
        "images": "/images",
        "videos": "/videos",
    }

    def __init__(self, tv_id, season_number):
        super().__init__()
        self.tv_id = tv_id
        self.season_number = season_number

    def info(self, language: str | None = None, append_to_response: str | None = None):
        """
        Get the TV season details by id.

        Supports append_to_response. Read more about this at
        https://developers.themoviedb.org/3/getting-started/append-to-response.

        Args:
            language: (optional) ISO 639 code.
            append_to_response: (optional) Append requests within the same
                namespace to the response.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_path("info")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if append_to_response is not None:
            kwargs["append_to_response"] = append_to_response

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def account_states(
        self,
        session_id: str,
        language: str | None = None,
        guest_session_id: str | None = None,
    ):
        """
        Returns all of the user ratings for the season's episodes.

        Args:
            language: (optional) ISO 639 code.
            session_id: (required) See Authentication.
            guest_session_id: (optional) See Authentication.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_path("account_states")
        kwargs = {"session_id": session_id}
        if language is not None:
            kwargs["language"] = language
        if guest_session_id is not None:
            kwargs["guest_session_id"] = guest_session_id

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self, language: str | None = None):
        """
        Get the credits for TV season.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_path("credits")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self, language: str | None = None):
        """
        Get the external ids for a TV season. We currently support the
        following external sources.

        Media Databases: TVDB ID, Freebase MID*, Freebase ID*, TVRage ID*

        *Defunct or no longer available as a service.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_path("external_ids")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def images(
        self, language: str | None = None, include_image_language: str | None = None
    ):
        """
        Get the images that belong to a TV season.

        Querying images with a language parameter will filter the results. If
        you want to include a fallback language (especially useful for
        backdrops) you can use the include_image_language parameter. This
        should be a comma separated value like so:
        include_image_language=en,null.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_path("images")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language
        if include_image_language is not None:
            kwargs["include_image_language"] = include_image_language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def videos(self, language: str | None = None):
        """
        Get the videos that have been added to a TV season.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_path("videos")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def _get_tv_id_season_number_path(self, key):
        return self._get_path(key).format(
            tv_id=self.tv_id, season_number=self.season_number
        )


class TV_Episodes(TMDB):
    """
    TV Episodes functionality.

    See: https://developers.themoviedb.org/3/tv-episodes
    """

    BASE_PATH = "tv/{tv_id}/season/{season_number}/episode/{episode_number}"
    URLS = {
        "info": "",
        "account_states": "/account_states",
        "credits": "/credits",
        "external_ids": "/external_ids",
        "images": "/images",
        "translations": "/translations",
        "rating": "/rating",
        "rating_delete": "/rating",
        "videos": "/videos",
    }

    def __init__(self, tv_id, season_number, episode_number):
        super().__init__()
        self.tv_id = tv_id
        self.season_number = season_number
        self.episode_number = episode_number

    def info(self, language: str | None = None, append_to_response: str | None = None):
        """
        Get the TV episode details by id.

        Supports append_to_response. Read more about this at
        https://developers.themoviedb.org/3/getting-started/append-to-response.

        Args:
            language: (optional) ISO 639 code.
            append_to_response: (optional) Append requests within the same
                namespace to the response.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("info")
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
        Get your rating for an episode.

        Args:
            session_id: (required) See Authentication.
            guest_session_id: (optional) See Authentication.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("account_states")
        kwargs = {"session_id": session_id}
        if guest_session_id is not None:
            kwargs["guest_session_id"] = guest_session_id

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def credits(self):
        """
        Get the credits (cast, crew and guest stars) for a TV episode.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("credits")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def external_ids(self):
        """
        Get the external ids for a TV episode. We currently support the
        following external sources.

        External Sources: IMDb ID, TVDB ID, Freebase MID*, Freebase ID*, TVRage
        ID*

        *Defunct or no longer available as a service.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("external_ids")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def images(self):
        """
        Get the images that belong to a TV episode.

        Querying images with a language parameter will filter the results. If
        you want to include a fallback language (especially useful for
        backdrops) you can use the include_image_language parameter. This
        should be a comma separated value like so:
        include_image_language=en,null.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("images")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def translations(self):
        """
        Get the translation data for an episode.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("translations")

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
        Rate a TV episode.

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
        path = self._get_tv_id_season_number_episode_number_path("rating")
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
        Remove your rating for a TV episode.

        A valid session or guest session ID is required. You can read more
        about how this works at
        https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id.

        Args:
            session_id: (optional) See Authentication.
            guest_session_id: (optional) See Authentication.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("rating_delete")
        kwargs = {}
        if session_id is not None:
            kwargs["session_id"] = session_id
        if guest_session_id is not None:
            kwargs["guest_session_id"] = guest_session_id

        response = self._DELETE(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def videos(self, language: str | None = None):
        """
        Get the videos that have been added to a TV episode.

        Args:
            language: (optional) ISO 639 code.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_tv_id_season_number_episode_number_path("videos")
        kwargs = {}
        if language is not None:
            kwargs["language"] = language

        response = self._GET(path, kwargs)
        self._set_attrs_to_values(response)
        return response

    def _get_tv_id_season_number_episode_number_path(self, key):
        return self._get_path(key).format(
            tv_id=self.tv_id,
            season_number=self.season_number,
            episode_number=self.episode_number,
        )


class TV_Episode_Groups(TMDB):
    """
    TV Episode Groups functionality.

    See: https://developers.themoviedb.org/3/tv-episode-groups
    """

    BASE_PATH = "tv/episode_group"
    URLS = {
        "info": "/{id}",
    }

    def __init__(self, id):
        super().__init__()
        self.id = id

    def info(self, language: str | None = None):
        """
        Get the details of a TV episode group. Groups support 7 different types
        which are enumerated as the following:
            1. Original air date
            2. Absolute
            3. DVD
            4. Digital
            5. Story arc
            6. Production
            7. TV

        Args:
            language: (optional) ISO 639 code.

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


class TV_Changes(TMDB):
    """
    Changes functionality for TV Series, Season and Episode.

    See: https://developers.themoviedb.org/3/tv/get-tv-changes
         https://developers.themoviedb.org/3/tv-seasons/get-tv-season-changes
         https://developers.themoviedb.org/3/tv-episodes/get-tv-episode-changes
    """

    BASE_PATH = "tv"
    URLS = {
        "series": "/{id}/changes",  # id => tv_id
        "season": "/season/{id}/changes",  # id => season_id
        "episode": "/episode/{id}/changes",  # id => episode_id
    }

    def __init__(self, id=0):
        super().__init__()
        self.id = id

    def series(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int | None = None,
    ):
        """
        Get the changes for a TV show. By default only the last 24 hours are returned.

        You can query up to 14 days in a single query by using the start_date
        and end_date query parameters.

        TV show changes are different than movie changes in that there are some
        edits on seasons and episodes that will create a change entry at the
        show level. These can be found under the season and episode keys. These
        keys will contain a series_id and episode_id. You can use the season
        changes and episode changes methods to look these up individually.

        Args:
            start_date: (optional) Filter the results with a start date.
                Expected format is 'YYYY-MM-DD'.
            end_date: (optional) Filter the results with a end date.
                Expected format is 'YYYY-MM-DD'.
            page: (optional) Minimum 1, maximum 1000, default 1.

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("series")
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

    def season(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int | None = None,
    ):
        """
        Get the changes for a TV season. By default only the last 24 hours are returned.

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
        path = self._get_id_path("season")
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

    def episode(
        self,
        start_date: str | None = None,
        end_date: str | None = None,
        page: int | None = None,
    ):
        """
        Get the changes for a TV episode. By default only the last 24 hours are returned.

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
        path = self._get_id_path("episode")
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


class Networks(TMDB):
    """
    Networks functionality.

    See: https://developers.themoviedb.org/3/networks
    """

    BASE_PATH = "network"
    URLS = {
        "info": "/{id}",
        "alternative_names": "/{id}/alternative_names",
        "images": "/{id}/images",
    }

    def __init__(self, id):
        super().__init__()
        self.id = id

    def info(self):
        """
        Get the details of a network.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("info")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def alternative_names(self):
        """
        Get the alternative names of a network.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("alternative_names")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response

    def images(self):
        """
        Get a TV network logos by id.

        There are two image formats that are supported for networks, PNG's and
        SVG's. You can see which type the original file is by looking at the
        file_type field. We prefer SVG's as they are resolution independent and
        as such, the width and height are only there to reflect the original
        asset that was uploaded. An SVG can be scaled properly beyond those
        dimensions if you call them as a PNG.

        For more information about how SVG's and PNG's can be used, take a read
        through https://developers.themoviedb.org/3/getting-started/images.

        Args:
            None

        Returns:
            A dict representation of the JSON returned from the API.
        """
        path = self._get_id_path("images")

        response = self._GET(path)
        self._set_attrs_to_values(response)
        return response
