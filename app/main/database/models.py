from sqlalchemy import BigInteger, Integer, String, Date, Column, ForeignKey, Float
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    tg_id = Column(BigInteger, unique=True, nullable=False)
    username = Column(String)
    email = Column(String)

    entries = relationship('DiaryEntry', order_by='DiaryEntry.id', back_populates='user')
    activities = relationship('ActivityTracking', order_by='ActivityTracking.id', back_populates='user')

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


class ActivityTracking(Base):
    __tablename__ = 'activity_tracking'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    activity_name = Column(String, nullable=False)
    duration = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    user = relationship('User', back_populates='activities')

    def __repr__(self):
        return (f"<ActivityTracking(id={self.id}, user_id={self.user_id},"
                f" activity_name={self.activity_name}, duration={self.duration}, date={self.date})>")
