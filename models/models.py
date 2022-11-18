from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, Text, BigInteger

Base = declarative_base()


class User(Base):
    __tablename__: str = "users"

    id = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    phone = Column(Text, nullable=False)
    email = Column(Text, nullable=False)


class Main(Base):
    __tablename__ = "main"

    id = Column(Integer, primary_key=True)
    mame = Column(Text, nullable=False)
    description = Column(Text, nullable=False)