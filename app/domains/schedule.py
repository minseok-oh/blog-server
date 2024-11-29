from datetime import datetime


class Schedule:

    def __init__(self, id: int, title: str, content: str, member_id: int, started_at: datetime, ended_at: datetime,
                 color: str):
        self._validate_title(title=title)
        self._validate_content(content=content)
        self._validate_time(started_at=started_at, ended_at=ended_at)

        self.__id = id
        self.__title = self._make_valid_title(title=title)
        self.__content = self._make_valid_content(content=content)
        self.__member_id = member_id
        self.__started_at = started_at
        self.__ended_at = ended_at
        self.__color = color

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
    def started_at(self):
        return self.__started_at

    @property
    def ended_at(self):
        return self.__ended_at

    @property
    def color(self):
        return self.__color

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

    def _validate_time(self, started_at, ended_at):
        """
        일정의 시작 시간과 종료 시간을 검사합니다.
        """
        if started_at > ended_at:
            raise ValueError("시작 시간이 종료 시간보다 늦을 수 없습니다.")
