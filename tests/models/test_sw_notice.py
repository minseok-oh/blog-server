from unittest import TestCase
from datetime import datetime
from app.schemas.sw_notice import SWNotice

class TestSWNotice(TestCase):
    def test_sw_notice_repr(self):
        # Given
        title = "2024학년 현장실습 체험수기 공모전 수상자 안내"
        created_date = datetime(2024, 10, 31)
        link = "https://sw7up.cbnu.ac.kr/community/notice/6723317ac5191d0dbe9a11b6"

        # When
        notice = SWNotice(
            title=title,
            created_date=created_date,
            link=link
        )

        # Then
        expected_repr = (f"SWNotice(title={title!r}, "
                        f"created_date={created_date!r}, link={link!r})")
        self.assertEqual(repr(notice), expected_repr)