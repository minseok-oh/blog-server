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
    hits = Column(Integer)

    def __repr__(self):
        """
        Post entity 필드값들을 리턴합니다.
        """
        return (f"PostEntity(id={self.id!r}, title={self.title!r}, content={self.content!r},"
                f" member_id={self.member_id!r}, board_id={self.board_id!r}, created_at={self.created_at!r})")
