"""Stream type classes for tap-aircall."""

from typing import List, Optional

from tap_aircall.client import aircallStream

from .schemas import (
    call_properties,
    contact_properties,
    number_properties,
    tag_properties,
    teams_properties,
    user_properties,
)


class UsersStream(aircallStream):
    """Define custom stream."""

    name = "users"
    path = "v1/users"
    primary_keys = ["id"]
    replication_key = "created_at"
    schema = user_properties.to_dict()
    records_jsonpath = "$.users[*]"  # Or override `parse_response`.

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"user_id": record["id"]}


class UserStream(aircallStream):
    """Define custom stream."""

    name = "user"
    parent_stream_type = UsersStream
    path = "v1/users/{user_id}"

    primary_keys = ["id"]
    # replication_key = "created_at"
    schema = user_properties.to_dict()
    records_jsonpath = "$.user[*]"  # Or override `parse_response`.
    #  not to store any state bookmarks for the child stream
    state_partitioning_keys: Optional[List[str]] = []


class CallsStream(aircallStream):
    """Define custom stream."""

    name = "calls"
    path = "v1/calls"
    primary_keys = ["id"]

    # FUJ-4262, Aircall tap for Wine Enthusiast is not fetching data beyond 3/20
    # Changed replication_key to look at call start date/time vs call id
    # replication_key = "id"
    replication_key = "started_at"

    schema = call_properties.to_dict()
    records_jsonpath = "$.calls[*]"  # Or override `parse_response`.

    post_process_datetime_types = ["started_at", "answered_at", "ended_at"]

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"call_id": record["id"]}


class CallStream(aircallStream):
    """
    Retrieve a Call data like duration, direction, status, timestamps, comments or tags…
    https://developer.aircall.io/api-references/#retrieve-a-call
    """

    name = "call"
    parent_stream_type = CallsStream
    path = "v1/calls/{call_id}"

    primary_keys = ["id"]
    replication_key = "started_at"
    schema = call_properties.to_dict()
    records_jsonpath = "$.call[*]"  # Or override `parse_response`.
    #  not to store any state bookmarks for the child stream

    post_process_datetime_types = ["started_at", "answered_at", "ended_at"]

    state_partitioning_keys: Optional[List[str]] = []


class TeamsStream(aircallStream):
    """
    Fetch all Teams associated to a company and their information
    https://developer.aircall.io/api-references/#list-all-teams
    """

    name = "teams"
    path = "v1/teams"
    primary_keys = ["id"]
    # replication_key = "created_at"
    schema = teams_properties.to_dict()
    records_jsonpath = "$.teams[*]"  # Or override `parse_response`.

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"team_id": record["id"]}


class TeamStream(aircallStream):
    """
    Retrieve details of a specific Team.
    https://developer.aircall.io/api-references/#retrieve-a-team
    """

    name = "team"
    parent_stream_type = TeamsStream
    path = "v1/teams/{team_id}"

    primary_keys = ["id"]
    # replication_key = "created_at"
    schema = teams_properties.to_dict()
    records_jsonpath = "$.team[*]"  # Or override `parse_response`.
    #  not to store any state bookmarks for the child stream
    state_partitioning_keys: Optional[List[str]] = []


class NumbersStream(aircallStream):
    """
    Fetch all Numbers associated to a company and their information.
    https://developer.aircall.io/api-references/#list-all-numbers
    """

    name = "numbers"
    path = "v1/numbers"
    primary_keys = ["id"]
    replication_key = "created_at"
    schema = number_properties.to_dict()
    records_jsonpath = "$.numbers[*]"  # Or override `parse_response`.

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"number_id": record["id"]}


class NumberStream(aircallStream):
    """
    Retrieve a Call data like duration, direction, status, timestamps, comments or tags…
    https://developer.aircall.io/api-references/#retrieve-a-call
    """

    name = "number"
    parent_stream_type = NumbersStream
    path = "v1/numbers/{number_id}"

    primary_keys = ["id"]
    # replication_key = "created_at"
    schema = number_properties.to_dict()
    records_jsonpath = "$.number[*]"  # Or override `parse_response`.
    #  not to store any state bookmarks for the child stream
    state_partitioning_keys: Optional[List[str]] = []


class ContactsStream(aircallStream):
    """
    Fetch all the shared Contacts associated to a company with their phone numbers and emails information.
    https://developer.aircall.io/api-references/#list-all-contacts # noqa: E501
    """

    name = "contacts"
    path = "v1/contacts"
    primary_keys = ["id"]
    replication_key = "updated_at"
    schema = contact_properties.to_dict()
    records_jsonpath = "$.contacts[*]"  # Or override `parse_response`.

    post_process_datetime_types = ["created_at", "updated_at"]

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"contact_id": record["id"]}


class ContactStream(aircallStream):
    """
    Retrieve details of a specific Contact.
    https://developer.aircall.io/api-references/#retrieve-a-contact
    """

    name = "contact"
    parent_stream_type = ContactsStream
    path = "v1/contacts/{contact_id}"

    primary_keys = ["id"]
    # replication_key = "updated_at"
    schema = contact_properties.to_dict()
    records_jsonpath = "$.contact[*]"  # Or override `parse_response`.
    #  not to store any state bookmarks for the child stream

    post_process_datetime_types = ["created_at", "updated_at"]

    state_partitioning_keys: Optional[List[str]] = []


class TagsStream(aircallStream):
    """
    Fetch all Tags associated to a company and their information.
    https://developer.aircall.io/api-references/#list-all-tags
    """

    name = "tags"
    path = "v1/tags"
    primary_keys = ["id"]
    # replication_key = "created_at"
    schema = tag_properties.to_dict()
    records_jsonpath = "$.tags[*]"  # Or override `parse_response`.

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"tag_id": record["id"]}


class TagStream(aircallStream):
    """
    Retrieve details of a specific Contact.
    https://developer.aircall.io/api-references/#retrieve-a-contact
    """

    name = "tag"
    parent_stream_type = TagsStream
    path = "v1/tags/{tag_id}"

    primary_keys = ["id"]
    # replication_key = "created_at"
    schema = tag_properties.to_dict()
    records_jsonpath = "$.tag[*]"  # Or override `parse_response`.
    #  not to store any state bookmarks for the child stream
    state_partitioning_keys: Optional[List[str]] = []
