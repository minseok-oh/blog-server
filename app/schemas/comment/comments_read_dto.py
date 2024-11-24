from app.domains.comment import Comment


class CommentsReadDTO:
    def __init__(self, comment_entity: Comment):
        self.__user_id = comment_entity.user_id
        self.__content = comment_entity.content
        self.__parent_id = comment_entity.parent_id
