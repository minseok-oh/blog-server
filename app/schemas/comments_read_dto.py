from app.models.comment_entity import CommentEntity


class CommentsReadDTO:
    def __init__(self, comment_entity: CommentEntity):
        self.__user_id = comment_entity.user_id
        self.__content = comment_entity.content
        self.__parent_id = comment_entity.parent_id
        self.__created_at = comment_entity.comment_date