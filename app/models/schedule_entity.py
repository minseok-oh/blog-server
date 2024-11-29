from sqlalchemy import Column, Integer, String, ForeignKey, DateTime

from config.db_config import Base


class ScheduleEntity(Base):
    __tablename__ = 'Schedule'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(1000), nullable=False)
    member_id = Column(Integer, ForeignKey('Member.id'), nullable=False)
    started_at = Column(DateTime)
    ended_at = Column(DateTime)
    color = Column(String(10), nullable=False)

    def __repr__(self):
        """
        Schedule entity 필드값들을 리턴합니다.
        """
        return (f"ScheduleEntity(id={self.id!r}, title={self.title!r}, content={self.content!r},"
                f" member_id={self.member_id!r}, started_at={self.started_at!r}, ended_at={self.ended_at!r}, color={self.color!r})")


