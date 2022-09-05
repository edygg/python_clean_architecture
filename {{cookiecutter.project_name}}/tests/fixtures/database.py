import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from config import settings

from {{cookiecutter.project_name}}.infrastructure.persistence.database import config_database



@pytest.fixture(scope="session")
def connection():
    engine = create_engine(settings.DATABASE_URL)
    return engine.connect()


@pytest.fixture(scope="session")
def setup_database(connection):
    config_database.Base.metadata.bind = connection
    config_database.Base.metadata.create_all()

    yield

    config_database.Base.metadata.drop_all()


@pytest.fixture
def db_session(setup_database, connection):
    """
    Connects to Postgres DB using SQLAlchemy
    :param setup_database:
    :param connection:
    :param carrier:
    :return: DB session to postgres db.
    """
    transaction = connection.begin()
    current_session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=connection)
    )
    seed_database(current_session)
    yield current_session
    transaction.rollback()


def seed_database(session):
    # currencies = [{"iso_code": "USD", "name": "Dollar", "symbol": "$"}]

    # countries = [{"iso_code": "HND", "name": "Honduras", "currency": "USD"}]

    # journey_providers = [{"name": "Interplai", "provider_code": "interplai"}]

    # corporations = [{"id": carrier.corporation.id, "name": carrier.corporation.name}]

    # carriers = [
    #     {"id": carrier.id, "name": carrier.name, "corporation": carrier.corporation.id}
    # ]

    # for currency in currencies:
    #     session.add(CurrencyModel(**currency))

    # session.commit()

    # for country in countries:
    #     session.add(CountryModel(**country))

    # session.commit()

    # for journey_provider in journey_providers:
    #     session.add(JourneyProviderModel(**journey_provider))

    # session.commit()

    # for corporation in corporations:
    #     session.add(CorporationModel(**corporation))

    # session.commit()

    # for carrier in carriers:
    #     session.add(CarrierModel(**carrier))

    # session.commit()
    pass