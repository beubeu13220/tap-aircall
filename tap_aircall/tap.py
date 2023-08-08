"""aircall tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_aircall.streams import (
    CallsStream,
    UsersStream,
    UserStream,
    TeamsStream,
    TeamStream,
    CallStream,
    NumbersStream,
    NumberStream,
    ContactsStream,
    ContactStream,
    TagsStream,
    TagStream
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    CallsStream,
    # CallStream,
    UsersStream,
    # UserStream,
    TeamsStream,
    # TeamStream,
    NumbersStream,
    NumberStream,
    ContactsStream,
    # ContactStream,
    TagsStream,
    # TagStream
]


class Tapaircall(Tap):
    """aircall tap class."""
    name = "tap-aircall"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_token",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "api_id",
            th.StringType,
            required=True,
            description="The id to authenticate against the API service"
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
