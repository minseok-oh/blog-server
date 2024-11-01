import bcrypt

from app.models.user import User


def encrypt_password(user : User):
    """
    암호화된 비밀번호를 갖는 UserEntity 리턴하는 함수.
    솔트는 중간 중간에 랜덤으로 문자열을 넣는 것이다.
    """
    user.password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    return user