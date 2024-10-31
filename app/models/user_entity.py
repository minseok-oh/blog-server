from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class UserEntity(Base):
    __tablename__ = 'Member'

    id = Column(String, primary_key=True, foreign_key=True)
    name = Column(String, nullable=False)
    member_id = Column(String, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String)
    avatar = Column(String)
    phone_number = Column(String)
    student_number = Column(String, nullable=False)
    birth = Column(DateTime)
    email = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', member_id='{self.member_id}', password='{self.password}', role='{self.role}', avartar='{self.avatar}', phone_number='{self.phone_number}, student_number='{self.student_number}', birth='{self.birth}', email='{self.email}')>"