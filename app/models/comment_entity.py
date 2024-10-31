from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class CommentEntity(Base):
    __tablename__ = 'Comment'

    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey('Member.id'), nullable=False)
    content = Column(String, ForeignKey('Post.id'))
    parent_id = Column(String, ForeignKey('Comment.id'))  # 대댓글을 위한 자기 참조 외래 키
    comment_date = Column(DateTime)

    def __repr__(self):
        return f"<User(id={self.id}, user_id='{self.user_id}', content='{self.content}', parent_id='{self.parent_id}', comment_date='{self.comment_date}')>"
