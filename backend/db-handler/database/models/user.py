from sqlalchemy import Column, Integer, String, BigInteger, CHAR, DateTime
from database.connection import Base

class User(Base):
    __tablename__ = "tbl_user"

    user_uuid = Column(CHAR(36), primary_key=true, index=True)
    user_name = Column(String, nullable=False, unique=True)
    user_password = Column(String, nullable=False)
    user_created_at = Column(DateTime, nullable=False)

class Role(Base):
    __tablename__ = "tbl_role"

    role_id = Column(int, primary_key=True, autoincrement=True)
    role_name = Column(String, nullable=False, unique=True)