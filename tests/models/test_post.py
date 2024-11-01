from unittest import TestCase

from app.domains.post import Post
from datetime import datetime


class TestPost(TestCase):
    def test_valid_post_creation(self):
        # Given
        post_id = "1"
        title = "title"
        content = "content"
        member_id = 1
        board_id = 1
        created_at = datetime.now()

        # When
        post = Post(id=post_id, title=title, content=content, member_id=member_id, board_id=board_id, created_at=created_at)

        # Then
        self.assertEqual(post.id, post_id)
        self.assertEqual(post.title, title)
        self.assertEqual(post.content, content)
        self.assertEqual(post.member_id, member_id)
        self.assertEqual(post.board_id, board_id)
        self.assertEqual(post.created_at, created_at)

    def test_post_repr(self):
        # Given
        post_id = "1"
        title = "title"
        content = "content"
        member_id = 1
        board_id = 1
        created_at = datetime.now()

        # When
        post = Post(id=post_id, title=title, content=content, member_id=member_id, board_id=board_id,
                    created_at=created_at)

        # Then
        self.assertEqual(repr(post),
                         f"Post(id={post_id!r}, title={title!r}, content={content!r}, "
                         f"writer={member_id!r}, board={board_id!r}, created_at={created_at!r})")

    def test_invalid_post_creation(self):
        # Given
        test_cases = [
            # title
            ("1", None, "test", 1, 1, datetime.now()),
            ("1", "", "test", 1, 1, datetime.now()),
            ("1", "test", None, 1, 1, datetime.now()),
            ("1", "test", "", 1, 1, datetime.now())
        ]

        # Expect
        for test_case in test_cases:
            with self.assertRaises(ValueError):
                PostCreateDTO(*test_case)

    def test_post_creation_with_html_tags_in_title(self):
        # Given
        post_id = "1"
        title = "<br/>"
        content = "content"
        member_id = 1
        board_id = 1
        created_at = datetime.now()

        # When
        post = Post(id=post_id, title=title, content=content, member_id=member_id, board_id=board_id,
                    created_at=created_at)

        # Then
        self.assertNotIn("<", post.title)
        self.assertNotIn(">", post.title)

    def test_post_creation_with_html_tags_in_content(self):
        # Given
        post_id = "1"
        title = "title"
        content = "<br/>"
        member_id = 1
        board_id = 1
        created_at = datetime.now()

        # When
        post = Post(id=post_id, title=title, content=content, member_id=member_id, board_id=board_id,
                    created_at=created_at)

        # Then
        self.assertNotIn("<", post.title)
        self.assertNotIn(">", post.title)

