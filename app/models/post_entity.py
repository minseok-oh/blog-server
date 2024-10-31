from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PostEntity(Base):
    __tablename__ = 'Post'

    id = Column(String, primary_key=True)
    title = Column(String, nullable=False)
    attribute = Column(String)
    content = Column(String, nullable=False)
    user_id = Column(String, ForeignKey('Member.id'), nullable=False)
    board = Column(String)
    created_at = Column(DateTime)

    def __repr__(self):
        return f"<User(id={self.id}, title='{self.title}', attribute='{self.attribute}', content='{self.content}', user_id='{self.user_id}', board='{self.board}', created_at='{self.created_at}')>"

