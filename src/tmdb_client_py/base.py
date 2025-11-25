"""
tmdb_client_py.base
~~~~~~~~~~~~~~~
This module implements the base class of tmdb_client_py.

Created by Celia Oakley on 2013-10-31.

:copyright: (c) 2013-2025 by Celia Oakley
:license: GPLv3, see LICENSE for more details
"""

import json
import requests


class APIKeyError(Exception):
    pass


class TMDB:
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Connection": "close",
    }
    BASE_PATH = ""
    URLS = {}

    def __init__(self):
        from . import API_VERSION, REQUESTS_SESSION, REQUESTS_TIMEOUT

        self.base_uri = "https://api.themoviedb.org"
        self.base_uri += "/{version}".format(version=API_VERSION)
        self.session = REQUESTS_SESSION
        self.timeout = REQUESTS_TIMEOUT
        self.id = None

    def _get_path(self, key):
        return self.BASE_PATH + self.URLS[key]

    def _get_id_path(self, key):
        return self._get_path(key).format(id=self.id)

    def _get_complete_url(self, path):
        return "{base_uri}/{path}".format(base_uri=self.base_uri, path=path)

    def _get_params(self, params):
        # Remove session_id and guest_session_id from URL parameters as they should be in headers
        if params:
            # Remove session-related parameters that will be handled in headers
            params.pop("session_id", None)
            params.pop("guest_session_id", None)
            for key, value in params.items():
                if isinstance(params[key], bool):
                    params[key] = "true" if value is True else "false"
        return params

    def _request(self, method, path, params=None, payload=None):
        url = self._get_complete_url(path)
        params = self._get_params(params)

        # Add API key as Authorization header
        headers = self.headers.copy()
        from . import API_KEY

        if not API_KEY:
            raise APIKeyError
        headers["Authorization"] = f"Bearer {API_KEY}"

        # Create a new request session if no global session is defined
        if self.session is None:
            response = requests.request(
                method,
                url,
                params=params,
                data=json.dumps(payload) if payload else payload,
                headers=headers,
                timeout=self.timeout,
            )

        # Use the global requests session the user provided
        else:
            response = self.session.request(
                method,
                url,
                params=params,
                data=json.dumps(payload) if payload else payload,
                headers=headers,
                timeout=self.timeout,
            )

        response.raise_for_status()
        response.encoding = "utf-8"
        return response.json()

    def _GET(self, path, params=None):
        print(path, params)
        return self._request("GET", path, params=params)

    def _POST(self, path, params=None, payload=None):
        return self._request("POST", path, params=params, payload=payload)

    def _DELETE(self, path, params=None, payload=None):
        return self._request("DELETE", path, params=params, payload=payload)

    def _set_attrs_to_values(self, response={}):
        """
        Set attributes to dictionary values.

        - e.g.
        >>> import tmdb_client_py as tmdb
        >>> movie = tmdb.Movies(103332)
        >>> response = movie.info()
        >>> movie.title  # instead of response['title']
        """
        if isinstance(response, dict):
            for key in response.keys():
                if not hasattr(self, key) or not callable(getattr(self, key)):
                    setattr(self, key, response[key])
