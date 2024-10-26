from unittest import TestCase

from app.models.post import Post
from datetime import datetime


class TestPost(TestCase):
    def test_valid_post_creation(self):
        # Given
        post_id = "1"
        title = "title"
        attribute = "attribute"
        content = "content"
        user_id = "1"
        board = "board"
        created_at = datetime.now()

        # When
        post = Post(id=post_id, title=title, attribute=attribute, content=content, user_id=user_id, board=board,
                    created_at=created_at)

        # Then
        self.assertEqual(post.id, post_id)
        self.assertEqual(post.title, title)
        self.assertEqual(post.attribute, attribute)
        self.assertEqual(post.content, content)
        self.assertEqual(post.user_id, user_id)
        self.assertEqual(post.board, board)
        self.assertEqual(post.created_at, created_at)

    def test_post_repr(self):
        # Given
        post_id = "1"
        title = "title"
        attribute = "attribute"
        content = "content"
        user_id = "1"
        board = "board"
        created_at = datetime.now()

        # When
        post = Post(id=post_id, title=title, attribute=attribute, content=content, user_id=user_id, board=board,
                    created_at=created_at)

        # Then
        self.assertEqual(repr(post),
                         f"Post(id={post_id!r}, title={title!r}, attribute={attribute!r}, content={content!r}, "
                         f"writer={user_id!r}, board={board!r}, created_at={created_at!r})")

    def test_invalid_post_creation(self):
        # Given
        test_cases = [
            # title
            ("1", None, "test", "test", "1", "test", datetime.now()),
            ("1", "", "test", "test", "1", "test", datetime.now())
        ]

        # Expect
        for test_case in test_cases:
            with self.assertRaises(ValueError):
                Post(*test_case)

    def test_post_creation_with_html_tags_in_title(self):
        # Given
        post_id = "1"
        title = "<br/>"
        attribute = "attribute"
        content = "content"
        user_id = "1"
        board = "board"
        created_at = datetime.now()

        # When
        post = Post(id=post_id, title=title, attribute=attribute, content=content, user_id=user_id, board=board,
                    created_at=created_at)

        # Then
        self.assertNotIn("<", post.title)
        self.assertNotIn(">", post.title)
