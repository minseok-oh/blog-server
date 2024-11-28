from sqlalchemy import Column, String, DateTime, Integer

from config.db_config import Base


class UserEntity(Base):
    __tablename__ = 'Member'

    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    member_id = Column(String(20), nullable=False)
    nickname = Column(String(20), nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(20))
    avatar = Column(String(100))
    phone_number = Column(String(20))
    student_number = Column(String(20), nullable=False)
    birth = Column(DateTime)
    email = Column(String(50))

    def __repr__(self):
        """
        User entity 필드값들을 리턴합니다.
        """
        return f"<User(id={self.id}, name='{self.name}', member_id='{self.member_id}', password='{self.password}', role='{self.role}', avartar='{self.avatar}', phone_number='{self.phone_number}, student_number='{self.student_number}', birth='{self.birth}', email='{self.email}')>"