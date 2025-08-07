from sqlalchemy import create_engine, Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from sqlalchemy import desc
from features.data_save_signals import signals


Base = declarative_base()

class UserData(Base):
    __tablename__ = "userdata"
    email = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    mac_address = Column(String, nullable=False)
    ip_address = Column(String, nullable=True)
    location = Column(String, nullable=True)
    credits = Column(Integer, default=0)


class Notification(Base):
    __tablename__ = "notification"
    id = Column(Integer, primary_key=True, autoincrement=True)
    message = Column(String, nullable=True)
    time = Column(DateTime, default=datetime.now)  # Changed to datetime.now

    @classmethod
    def add_notification(cls, session, message):
        new_notif = cls(message=message)
        session.add(new_notif)
        count = session.query(cls).count()
        if count > 8:
            oldest = session.query(cls).order_by(cls.time).limit(count - 8).all()
            for notif in oldest:
                session.delete(notif)
        session.commit()
        signals.notification_saved.emit()
        return new_notif


engine = create_engine('sqlite:///userdata.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)