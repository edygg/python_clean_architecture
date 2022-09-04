from injector import ClassAssistedBuilder, Injector
from sqlalchemy.orm import sessionmaker

from {{cookiecutter.project_name}}.application.unit_of_work import UnitOfWork


class SQLAlchemyUnitOfWork(UnitOfWork):
    def __init__(
        self,
        session_factory: sessionmaker,
    ) -> None:
        super().__init__()
        self._session_factory: sessionmaker = session_factory

    def __enter__(self):
        self._session = self._session_factory()
        injector = Injector()

        # TODO Init repositories here. For instance:
        # currency_repo_builder = injector.get(ClassAssistedBuilder[CurrencyRepository])
        # 
        # self.currencies = currency_repo_builder.build(
        #     session=self._session,
        # )
        
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()