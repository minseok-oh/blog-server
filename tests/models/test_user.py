import datetime
from unittest import TestCase

from app.domains.user import User


class TestUser(TestCase):

    def test_valid_user_creation(self):
        # Given
        id = "test"
        name = "test"
        member_id = "test"
        password = "test1234!"
        role = "test"
        avatar = "test"
        phone_number = "01012345678"
        student_number = "202000000"
        birth = datetime.datetime.now()
        email = "test@test.com"

        # When
        user = User(id=id, name=name, member_id=member_id, password=password, role=role, avatar=avatar,
                    phone_number=phone_number, student_number=student_number, birth=birth, email=email)

        # Then
        self.assertEqual(user.id, id)
        self.assertEqual(user.name, name)
        self.assertEqual(user.member_id, member_id)
        self.assertEqual(user.password, password)
        self.assertEqual(user.role, role)
        self.assertEqual(user.avatar, avatar)
        self.assertEqual(user.phone_number, phone_number)
        self.assertEqual(user.student_number, student_number)
        self.assertEqual(user.birth, birth)
        self.assertEqual(user.email, email)

    def test_invalid_user_creation(self):
        # Given
        test_cases = [
            # name
            ("test", None, "test", "test", "test", "test", "01012345678", "202000000", datetime.datetime.now(),
             "test@test.com"),
            ("test", "invalid_name", "test", "test", "test", "test", "01012345678", "202000000", datetime.datetime.now(),
             "test@test.com"),
            # member_id
             ("test", "test", None, "test", "test", "test", "01012345678", "202000000", datetime.datetime.now(),
             "test@test.com"),
             ("test", "test", "invalid_member_id", "test", "test", "test", "01012345678", "202000000", datetime.datetime.now(),
             "test@test.com"),
            # password
            ("test", "test", "test", None, "test", "test", "01012345678", "202000000", datetime.datetime.now(),
             "test@test.com"),
            ("test", "test", "test", "invalid_password", "test", "test", "01012345678", "202000000",
             datetime.datetime.now(), "test@test.com"),
            ("test", "test", "test", "test1234", "test", "test", "01012345678", "202000000",
             datetime.datetime.now(), "test@test.com"),
            # student_number
            ("test", "test", "test", "test", "test", "test", "01012345678", None, datetime.datetime.now(),
             "test@test.com"),
            ("test", "test", "test", "test", "test", "test", "01012345678", "invalid_number", datetime.datetime.now(),
             "test@test.com"),
            # email
            ("test", "test", "test", "test", "test", "test", "01012345678", "202000000", datetime.datetime.now(),
             None),
            ("test", "test", "test", "test", "test", "test", "01012345678", "202000000", datetime.datetime.now(),
             "test@.com")
        ]

        # Expect
        for test_case in test_cases:
            with self.assertRaises(ValueError):
                User(*test_case)
