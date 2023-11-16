import typing as t

from singer_sdk.typing import PropertiesList


class OptionalPropertiesList(PropertiesList):
    """Optional Properties List, which wraps one or more named properties."""

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize OptionalPropertiesList from its list of properties."""
        super().__init__(*args, **kwargs)

    @property
    def type_dict(self) -> dict:  # type: ignore[override]
        """Override Get type dictionary.

        Returns:
            A dictionary describing the type.
        """
        type_dict: t.Dict = super().type_dict
        if type_dict.get("type"):
            type_dict.update({"type": ["object", "null"]})
        return type_dict
