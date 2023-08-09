"""aircall tap class."""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk import typing as th  # JSON schema typing helpers

# TODO: Import your custom stream types here:
from tap_aircall.streams import (
    CallsStream,
    ContactsStream,
    NumbersStream,
    NumberStream,
    TagsStream,
    TeamsStream,
    UsersStream,
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
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "api_id",
            th.StringType,
            required=True,
            description="The id to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            # Avoid to use current time in from parameter
            required=True,
            description="The earliest record date to sync",
        ),
        th.Property(
            "end_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
