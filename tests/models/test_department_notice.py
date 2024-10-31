from unittest import TestCase
from datetime import datetime
from app.schemas.department_notice import DepartmentNotice

class TestDepartmentNotice(TestCase):
    def test_department_notice_repr(self):
        # Given
        title = "2025학년도 1학기 학석사연계과정 학생 선발 안내"
        created_date = datetime(2024, 10, 29)
        link = "https://computer.chungbuk.ac.kr/bbs/bbs.php?task=view&db=notice&no=2381&page=1&search=&searchKey=&category=&pgID=ID12415888101"

        # When
        notice = DepartmentNotice(
            title=title,
            created_date=created_date,
            link=link
        )

        # Then
        expected_repr = (f"DepartmentNotice(title={title!r}, "
                        f"created_date={created_date!r}, link={link!r})")
        self.assertEqual(repr(notice), expected_repr)