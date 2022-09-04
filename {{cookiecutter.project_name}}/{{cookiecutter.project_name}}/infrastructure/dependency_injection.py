import injector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

from {{cookiecutter.project_name}}.application.unit_of_work import UnitOfWork
from {{cookiecutter.project_name}}.infrastructure.persistence.unit_of_work import SQLAlchemyUnitOfWork


class UnitOfWorkInfrastructure(injector.Module):
    @injector.provider
    def sql_alchemy_session_maker(self) -> sessionmaker:
        return sessionmaker(bind=create_engine(settings.DATABASE_URL))

    @injector.provider
    def sql_alchemy_unit_of_work(
        self,
        session_maker: sessionmaker
    ) -> UnitOfWork:
        return SQLAlchemyUnitOfWork(session_maker)


injector = injector.Injector(
    [
        UnitOfWorkInfrastructure(),
    ]
)