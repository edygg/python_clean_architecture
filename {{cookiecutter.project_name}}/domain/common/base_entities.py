import abc
from uuid import UUID


class Entity(abc.ABC):
    _identifier: UUID

    @property
    def id(self) -> UUID:
        return self._identifier


class Aggregate(Entity, abc.ABC):
    pass