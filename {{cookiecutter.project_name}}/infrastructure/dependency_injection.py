import injector
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from config import settings


class UnitOfWorkInfrastructure(injector.Module):
    @injector.provider
    def sql_alchemy_session_maker(self) -> sessionmaker:
        return sessionmaker(bind=create_engine(settings.DATABASE_URL))

    @injector.provider
    def sql_alchemy_unit_of_work(
        self,
        session_maker: sessionmaker
    ) -> AbstractUnitOfWork:
        return SQLAlchemyUnitOfWork(session_maker)


injector = injector.Injector(
    [
        UnitOfWorkInfrastructure(),
    ]
)