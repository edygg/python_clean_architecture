import abc


class Command(abc.ABC):
    
    @abc.abstractmethod
    def __call__(self, *args, **kwargs):
        raise NotImplementedError