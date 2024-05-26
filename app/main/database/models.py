

from sqlalchemy import BigInteger, Integer, String, Date, Column, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, unique=True, nullable=False)

class DiaryEntry(Base):
    __tablename__ = 'diary_entries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    content = Column(String, nullable=False)

    user = relationship('User', back_populates='entries')

User.entries = relationship('DiaryEntry', order_by=DiaryEntry.id, back_populates='user')

