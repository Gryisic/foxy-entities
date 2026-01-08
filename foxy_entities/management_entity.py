from typing import Self, Type, TypeVar

from foxy_entities.abc import SocialMediaEntity
from foxy_entities.exceptions import (
    # new
    InvalidEntityTypeError,
    AbstractEntityUsageError,
    EntityNotFoundError,
    # deprecated
    EntityTypeException,
    BanningAbcClass,
    PresenceObjectException,
)

SocialMediaEntityType = TypeVar("SocialMediaEntityType", bound=SocialMediaEntity)


class EntitiesController:
    """
        A virtual storage controller class that provides methods
        for adding and retrieving entities with simple Round Robin balancing
    """

    def __init__(self) -> None:
        self.__entity_virtual_storage: dict[str, list[SocialMediaEntity]] = {}

    def get_virtual_storage(self) -> dict[str, list[SocialMediaEntity]]:
        return self.__entity_virtual_storage.copy()

    @staticmethod
    def update_sequence_entity(
        sequence_entity: list[SocialMediaEntity],
        social_media_entity: SocialMediaEntity,
    ) -> list[SocialMediaEntity]:
        return [social_media_entity] + sequence_entity

    def add_entity(self, social_media_entity: SocialMediaEntity) -> Self:
        try:
            if not isinstance(social_media_entity, SocialMediaEntity):
                raise InvalidEntityTypeError(social_media_entity)

            if type(social_media_entity) is SocialMediaEntity:
                raise AbstractEntityUsageError()

        except InvalidEntityTypeError as exc:
            raise EntityTypeException(social_media_entity) from exc
        except AbstractEntityUsageError as exc:
            raise BanningAbcClass() from exc

        key = social_media_entity.__class__.__name__
        sequence = self.__entity_virtual_storage.get(key, [])
        self.__entity_virtual_storage[key] = self.update_sequence_entity(
            sequence, social_media_entity
        )
        return self

    def get_entity(
        self, social_media_type: Type[SocialMediaEntityType]
    ) -> SocialMediaEntityType:
        try:
            if not issubclass(social_media_type, SocialMediaEntity):
                raise InvalidEntityTypeError(social_media_type)

            if social_media_type is SocialMediaEntity:
                raise AbstractEntityUsageError()

            key = social_media_type.__name__
            sequence = self.__entity_virtual_storage.get(key)

            if not sequence:
                raise EntityNotFoundError(social_media_type)

        except InvalidEntityTypeError as exc:
            raise EntityTypeException(social_media_type) from exc
        except AbstractEntityUsageError as exc:
            raise BanningAbcClass() from exc
        except EntityNotFoundError as exc:
            raise PresenceObjectException(social_media_type) from exc

        entity = sequence.pop()

        if sequence:
            self.__entity_virtual_storage[key] = sequence
        else:
            del self.__entity_virtual_storage[key]

        return entity
