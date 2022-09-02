import abc

class UnitOfWork(abc.ABC):
    # TODO Your abstract repositories goes here: ex.
    # currencies: AbstractCurrencyRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError