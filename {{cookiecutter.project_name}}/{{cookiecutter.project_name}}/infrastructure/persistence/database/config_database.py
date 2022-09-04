import uuid

from sqlalchemy import Boolean, Column, ForeignKey, String, Table
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# TODO Defined your tables and models here. For instance:
  
# currency_table = Table(
#     "currencies",
#     Base.metadata,
#     Column("iso_code", String(15), primary_key=True),
#     Column("name", String(150), nullable=False),
#     Column("symbol", String(20)),
# )
#
#  
# bank_table = Table(
#     "banks",
#     Base.metadata,
#     Column("id", UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
#     Column("name", String(150), nullable=False),
#     Column("country", String(15), ForeignKey("countries.iso_code")),
#     Column("config", JSONB(), default=dict),
# )
#
#  
# class CurrencyModel(Base):
#     __table__ = currency_table
#
#  
# class BankModel(Base):
#     __table__ = bank_table

