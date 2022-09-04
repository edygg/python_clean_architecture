import abc


class EntityRepository(abc.ABC):
    pass


class GetEntityRepository(EntityRepository):
    @abc.abstractmethod
    def get(self, reference, *args, **kwargs):
        raise NotImplementedError()


class CreateEntityRepository(EntityRepository, abc.ABC):
    @abc.abstractmethod
    def create(self, params, *args, **kwargs):
        raise NotImplementedError()


class UpdateEntityRepository(EntityRepository, abc.ABC):
    @abc.abstractmethod
    def update(self, params, *args, **kwargs):
        raise NotImplementedError()


class DeleteEntityRepository(EntityRepository, abc.ABC):
    @abc.abstractmethod
    def delete(self, params, *args, **kwargs):
        raise NotImplementedError()


class CRUDEntityRepository(
    GetEntityRepository,
    CreateEntityRepository,
    UpdateEntityRepository,
    DeleteEntityRepository,
    abc.ABC,
):
    pass