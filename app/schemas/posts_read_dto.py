from app.domains.post import Post


class PostsReadDTO:
    def __init__(self, post_entity: Post):
        self.__id = post_entity.id
        self.__title = post_entity.title
        self.__created_at = post_entity.created_at
