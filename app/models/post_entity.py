from sqlalchemy import Column, String, DateTime, ForeignKey, Integer

from config.db_config import Base


class PostEntity(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    attribute = Column(String(20), nullable=False)
    content = Column(String(1000), nullable=False)
    member_id = Column(Integer, ForeignKey('Member.id'), nullable=False)
    board = Column(String(20), nullable=False)
    created_at = Column(DateTime)

    def __repr__(self):
        return f"<User(id={self.id}, title='{self.title}', attribute='{self.attribute}', content='{self.content}', user_id='{self.user_id}', board='{self.board}', created_at='{self.created_at}')>"
