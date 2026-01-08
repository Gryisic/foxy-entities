from foxy_entities.abc import SocialMediaEntity
from foxy_entities.exceptions import (
    FoxyEntityException,
    InvalidEntityTypeError,
    AbstractEntityUsageError,
    EntityNotFoundError,
)


class DummyEntity(SocialMediaEntity):
    pass


def test_all_exceptions_inherit_from_base():
    assert issubclass(InvalidEntityTypeError, FoxyEntityException)
    assert issubclass(AbstractEntityUsageError, FoxyEntityException)
    assert issubclass(EntityNotFoundError, FoxyEntityException)


def test_invalid_entity_type_error_message():
    value = 123
    exc = InvalidEntityTypeError(value)
    assert "is not a SocialMediaEntity" in str(exc)


def test_abstract_entity_usage_error_message():
    exc = AbstractEntityUsageError()
    assert "abstract base class" in str(exc)


def test_entity_not_found_error_message():
    exc = EntityNotFoundError(DummyEntity)
    assert DummyEntity.__name__ in str(exc)


def test_base_exception_catching():
    try:
        raise EntityNotFoundError(DummyEntity)
    except FoxyEntityException as exc:
        assert isinstance(exc, EntityNotFoundError)


def test_exception_is_exception():
    exc = InvalidEntityTypeError("test")
    assert isinstance(exc, Exception)
