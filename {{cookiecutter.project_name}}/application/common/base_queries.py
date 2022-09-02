import abc


class Query(abc.ABC):

    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError
