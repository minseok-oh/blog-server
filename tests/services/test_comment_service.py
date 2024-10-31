from unittest import TestCase
from datetime import datetime

from app.schemas.comment_create_dto import CommentCreateDTO
from app.services.comment_service import update_comment


class Test(TestCase):

    def test_update_comment(self):
        # Given
        id = "1"
        user_id = "1"
        content = "content"
        parent_id = "0"
        comment_date = datetime.now()
        comment = CommentCreateDTO(id=id, user_id=user_id, content=content, parent_id=parent_id, comment_date=comment_date)

        # When
        updated_comment = update_comment(comment)

        # Then
        self.assertEqual(updated_comment.id, id)
        self.assertEqual(updated_comment.user_id, user_id)
        self.assertEqual(updated_comment.content, content)
        self.assertEqual(updated_comment.parent_id, parent_id)
        self.assertNotEqual(updated_comment.comment_date, comment_date)

