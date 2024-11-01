import datetime
import re


class Comment:
    content_regex_has_letter = re.compile('.*[a-zA-Z가-힣]+.*')

    def __init__(self, id: int, user_id: int, content: str, parent_id: int, comment_date: datetime):
        self._validate_content(content=content)

        self.__id = id
        self.__user_id = user_id
        self.__content = self._make_validate_content(content=content)
        self.__parent_id = parent_id
        self.__comment_date = comment_date

    @property
    def id(self) -> str:
        return self.__id

    @property
    def user_id(self) -> str:
        return self.__user_id

    @property
    def content(self) -> str:
        return self.__content

    @property
    def parent_id(self) -> str:
        return self.__parent_id

    @property
    def comment_date(self) -> str:
        return self.__comment_date

    def __repr__(self):
        return (f"Comment(id={self.__id!r}, user_id={self.__user_id!r}, content={self.__content!r},"
                f" parent_id={self.__parent_id!r}, comment_date={self.__comment_date!r})")

    def _validate_content(self, content) -> None:
        """
        댓글의 유효성을 검사합니다.
        """
        if content is None:
            raise ValueError(f"현재 댓글: {content}")

        if Comment.content_regex_has_letter.match(content) is None:
            raise ValueError(f"현재 댓글: {content}")

    def _make_validate_content(self, content: str) -> str:
        """
        댓글을 유효한 댓글로 변경합니다.
        """
        return content.replace('<', '&lt;').replace('>', '&gt;')

    def update_comment_date(self) -> "Comment":
        """
        댓글을 수정하면 작성일자를 변경합니다.
        """
        return Comment(self.id, self.user_id, self.content, self.parent_id, datetime.datetime.now())
