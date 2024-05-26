from sqlalchemy import BigInteger, Integer, String, Date, Column, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String)  # Добавьте этот столбец
    email = Column(String)

    entries = relationship('DiaryEntry', order_by='DiaryEntry.id', back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, tg_id={self.tg_id}, username={self.username})>"


class DiaryEntry(Base):
    __tablename__ = 'diary_entries'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(Date, nullable=False)
    content = Column(String, nullable=False)

    user = relationship('User', back_populates='entries')

    def __repr__(self):
        return f"<DiaryEntry(id={self.id}, user_id={self.user_id}, date={self.date}, content={self.content})>"