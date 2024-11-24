from sqlalchemy import Column, String, DateTime, ForeignKey, Integer

from config.db_config import Base


class PostEntity(Base):
    __tablename__ = 'Post'

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(1000), nullable=False)
    member_id = Column(Integer, ForeignKey('Member.id'), nullable=False)
    board_id = Column(String(50), nullable=False)
    created_at = Column(DateTime)

    def __repr__(self):
        """
        Post entity 필드값들을 리턴합니다.
        """
        return f"<User(id={self.id}, title='{self.title}', attribute='{self.attribute}', content='{self.content}', user_id='{self.user_id}', board='{self.board}', created_at='{self.created_at}')>"
