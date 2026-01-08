from __future__ import annotations

from typing import Any
from typing_extensions import deprecated

from foxy_entities.abc import SocialMediaEntity

@deprecated("This exception is deprecated and will be removed in a future release. Use exceptions derived from FoxyEntityException instead.")
class EntityTypeException(Exception):
    """Deprecated. Use InvalidEntityTypeError."""

    def __init__(self, value: Any) -> None:
        super().__init__(
            f"{value!r} does not correspond to the SocialMediaEntity abstract base class"
        )


@deprecated("This exception is deprecated and will be removed in a future release. Use exceptions derived from FoxyEntityException instead.")
class PresenceObjectException(Exception):
    """Deprecated. Use EntityNotFoundError."""

    def __init__(self, entity_type: Any) -> None:
        super().__init__(f"No entities registered for type {entity_type!r}")


@deprecated("This exception is deprecated and will be removed in a future release. Use exceptions derived from FoxyEntityException instead.")
class BanningAbcClass(Exception):
    """Deprecated. Use AbstractEntityUsageError."""

    def __init__(self) -> None:
        super().__init__("Passing SocialMediaEntity abstract class is forbidden")


class FoxyEntityException(Exception):
    """Base exception for all foxy-entities related errors."""
    pass


class InvalidEntityTypeError(FoxyEntityException):
    def __init__(self, value: Any) -> None:
        super().__init__(
            f"{value!r} is not a SocialMediaEntity instance or subclass"
        )


class AbstractEntityUsageError(FoxyEntityException):
    def __init__(self) -> None:
        super().__init__(
            "Using SocialMediaEntity abstract base class directly is forbidden"
        )


class EntityNotFoundError(FoxyEntityException):
    def __init__(self, entity_type: type[SocialMediaEntity]) -> None:
        super().__init__(
            f"No entities available for type {entity_type.__name__}"
        )
