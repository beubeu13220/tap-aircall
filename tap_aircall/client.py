"""REST client handling, including aircallStream base class."""

from pathlib import Path
from typing import Any, Dict, Optional, Iterable
from urllib.parse import urlparse, parse_qs

import requests
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class aircallStream(RESTStream):
    """aircall stream class."""

    url_base = "https://api.aircall.io/"

    records_jsonpath = "$[*]"  # Or override `parse_response`.
    next_page_token_jsonpath = "$.meta.next_page_link"  # Or override `get_next_page_token`.

    @property
    def authenticator(self) -> BasicAuthenticator:
        """Return a new authenticator object."""
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config.get("api_id"),
            password=self.config.get("api_token"),
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")
        # If not using an authenticator, you may also provide inline auth headers:
        # headers["Private-Token"] = self.config.get("auth_token")
        return headers

    def get_next_page_token(
            self, response: requests.Response, previous_token: Optional[Any]
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        if self.next_page_token_jsonpath:
            all_matches = extract_jsonpath(
                self.next_page_token_jsonpath, response.json()
            )
            first_match = next(iter(all_matches), None)
            next_page_token = first_match
        else:
            next_page_token = response.headers.get("X-Next-Page", None)

        return next_page_token

    def get_url_params(
            self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            # format next_page_token: "https://api.aircall.io/v1/calls?page=2&per_page=20"
            # page & per_page require int params
            # extract query from next_page_token string
            next_page_token_query: Dict = parse_qs(urlparse(next_page_token).query)
            params["page"] = int(next_page_token_query.get('page', ['1'])[0])  # Default si 1
            params["per_page"] = int(next_page_token_query.get('per_page', ['20'])[0])  # Default is 20
        if self.replication_key:
            params["order"] = "asc"
            # params["order_by"] = self.replication_key
        starting_time = self.get_starting_timestamp(context)
        if starting_time:
            params["from"] = str(round(starting_time.timestamp()))

        return params

    def prepare_request_payload(
            self, context: Optional[dict], next_page_token: Optional[Any]
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        # TODO: Parse response body and return a set of records.

        self.logger.info(f"meta: {list(extract_jsonpath('$.meta.[*]', input=response.json()))}")

        yield from extract_jsonpath(self.records_jsonpath, input=response.json())

    def post_process(self, row: dict, context: Optional[dict]) -> dict:
        """As needed, append or transform raw data to match expected structure."""
        # TODO: Delete this method if not needed.
        return row
