from unittest import TestCase

from app.schemas.post_create_dto import PostCreateDTO
from app.services.post_service import create_post
from datetime import datetime


class TestPostService(TestCase):

    def test_create_post(self):
        # Given
        # TODO: 외래키로 사용되는 개체를 먼저 등록합니다.

        title = "Test Title"
        content = "Test Content"
        member_id = 1
        board_id = 1

        # When
        result = create_post(title=title, content=content, member_id=member_id, board_id=board_id)

        # Then
        # self.assertIsInstance(result, Post)
        # self.assertEqual(result.title, title)
        # self.assertEqual(result.content, content)
        # self.assertEqual(result.member_id, member_id)
        # self.assertEqual(result.board_id, board_id)
        # self.assertTrue(isinstance(result.created_at, datetime))