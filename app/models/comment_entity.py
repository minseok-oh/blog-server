from sqlalchemy import Column, String, DateTime, ForeignKey, Integer

from config.db_config import Base


class CommentEntity(Base):
    __tablename__ = 'Comment'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('Member.id'), nullable=False)
    content = Column(String(1000), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    parent_id = Column(Integer, ForeignKey('Comment.id'))
    created_at = Column(DateTime)

    def __repr__(self):
        """
        Comment entity 필드값들을 리턴합니다.
        """
        return f"<User(id={self.id}, user_id='{self.user_id}', content='{self.content}', parent_id='{self.parent_id}', comment_date='{self.comment_date}')>"

