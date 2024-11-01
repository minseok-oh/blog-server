from datetime import datetime
from unittest import TestCase

from app.domains.comment import Comment


class TestPost(TestCase):

    def test_valid_comment_creation(self):
        # Given
        id = "1"
        user_id = "2020000000"
        content = "content"
        parent_id = "0"
        comment_date = datetime.now()

        # When
        comment = CommentCreateDTO(id=id, user_id=user_id, content=content, parent_id=parent_id, comment_date=comment_date)

        # Then
        self.assertEqual(comment.id, id)
        self.assertEqual(comment.user_id, user_id)
        self.assertEqual(comment.content, content)
        self.assertEqual(comment.parent_id, parent_id)
        self.assertEqual(comment.comment_date, comment_date)

    def test_invalid_comment_creation(self):
        # Given
        test_cases = [
            ("1", "2020000000", "", "0", datetime.now()),
            ("1", "2020000000", None, "0", datetime.now())
        ]

        # Expect
        for test_case in test_cases:
            with self.assertRaises(ValueError):
                CommentCreateDTO(*test_case)

    def test_comment_creation_with_html_tags_in_content(self):
        # Given
        id = "1"
        user_id = "2020000000"
        content = "<html>"
        parent_id = "0"
        comment_date = datetime.now()

        # When
        comment = CommentCreateDTO(id=id, user_id=user_id, content=content, parent_id=parent_id, comment_date=comment_date)

        # Then
        self.assertNotIn("<", comment.content)
        self.assertNotIn(">", comment.content)

    def test_comment_repr(self):
        # Given
        id = "1"
        user_id = "2020000000"
        content = "content"
        parent_id = "0"
        comment_date = datetime.now()

        # When
        comment = CommentCreateDTO(id=id, user_id=user_id, content=content, parent_id=parent_id, comment_date=comment_date)

        # Then
        self.assertEqual(repr(comment),
                         f"Comment(id={id!r}, user_id={user_id!r}, content={content!r}, "
                         f"parent_id={parent_id!r}, comment_date={comment_date!r})")

    def test_update_comment_date(self):
        # Given
        id = "1"
        user_id = "2020000000"
        content = "content"
        parent_id = "0"
        comment_date = datetime.now()
        comment = CommentCreateDTO(id=id, user_id=user_id, content=content, parent_id=parent_id, comment_date=comment_date)

        # When
        new_comment = comment.update_comment_date()

        # Then
        self.assertNotEqual(comment, new_comment)
        self.assertEqual(new_comment.id, id)
        self.assertEqual(new_comment.user_id, user_id)
        self.assertEqual(new_comment.content, content)
        self.assertEqual(new_comment.parent_id, parent_id)
        self.assertNotEqual(new_comment.comment_date, comment_date)
