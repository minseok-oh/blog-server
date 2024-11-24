from __future__ import annotations

from datetime import datetime


class Post:
    def __init__(self, id: int | None, title: str, content: str, member_id: int, board_id: str,
                 created_at: datetime):
        self._validate_title(title=title)
        self._validate_content(content=content)

        self.__id = id
        self.__title = self._make_valid_title(title=title)
        self.__content = self._make_valid_content(content=content)
        self.__member_id = member_id
        self.__board_id = board_id
        self.__created_at = created_at

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def content(self):
        return self.__content

    @property
    def member_id(self):
        return self.__member_id

    @property
    def board_id(self):
        return self.__board_id

    @property
    def created_at(self):
        return self.__created_at

    def __repr__(self):
        return (f"Post(id={self.__id!r}, title={self.__title!r}, content={self.__content!r},"
                f" writer={self.__member_id!r}, board={self.__board_id!r}, created_at={self.__created_at!r})")

    def _validate_title(self, title: str) -> None:
        """
        글 제목의 유효성을 검사합니다.
        """
        if not title:
            raise ValueError(f"현재 제목: {title}")

    def _make_valid_title(self, title: str) -> str:
        """
        글 제목을 유효한 제목으로 변경합니다.
        """
        return title.replace('<', '&lt;').replace('>', '&gt;')

    def _validate_content(self, content: str):
        """
        글 내용의 유효성을 검사합니다.
        """
        if not content:
            raise ValueError(f"현재 내용: {content}")

    def _make_valid_content(self, content: str) -> str:
        """
        글 내용을 유효한 내용으로 변경합니다.
        """
        return content.replace('<', '&lt;').replace('>', '&gt;')