import datetime
from unittest import TestCase

import bcrypt

from app.domains.user import User
from app.services.user_service import encrypt_password


class TestUserService(TestCase):

    def test_encrypt_password(self):
        #Given
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

        test_cases = [
            # same password
            ("test", "test", "test", "test1234!", "test", "test", "01012345678", "2020000000",
             datetime.datetime.now(), "test@test.com"),
            # different password
            ("test", "test", "test", "test4321!", "test", "test", "01012345678", "2020000000",
             datetime.datetime.now(), "test@test.com"),
        ]

        # When
        user = User(id=id,name=name,member_id=member_id,password=password,role=role,avatar=avatar,
                    phone_number=phone_number, student_number=student_number,birth=birth,email=email)

        encrypted_password = encrypt_password(user).password

        # Then
        self.assertTrue(bcrypt.checkpw(test_cases[0][3].encode('utf-8'), encrypted_password))
        self.assertFalse(bcrypt.checkpw(test_cases[1][3].encode('utf-8'), encrypted_password))
