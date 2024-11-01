from datetime import datetime

class DepartmentNotice:
    def __init__(self, title: str, created_date: datetime, link: str):
        self.__title = title
        self.__created_date = created_date
        self.__link = link

    @property
    def title(self) -> str:
        return self.__title

    @property
    def created_date(self) -> datetime:
        return self.__created_date

    @property
    def link(self) -> str:
        return self.__link

    def __repr__(self) -> str:
        return (f"DepartmentNotice(title={self.__title!r}, "
                f"created_date={self.__created_date!r}, link={self.__link!r})")
