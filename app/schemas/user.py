import datetime
import re


class User:
    name_regex_korean = re.compile(r"^[가-힣]+$")
    name_regex_english = re.compile(r"^[a-zA-Z]+$")

    member_id_regex = re.compile(r"^[a-z0-9]+$")
    
    password_regex_upper = re.compile(r"[A-Z]")
    password_regex_lower = re.compile(r"[a-z]")
    password_regex_digits = re.compile(r"\d")
    password_regex_special_word = re.compile(r'[!@#$%^&*()_+~`{}\[\]:;"\'<>,.?/\\|-]')
    
    student_number_regex = re.compile(r"^\d{6,11}$")

    email_regex = re.compile(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    
    PASSWORD_VALIDATE_CONDITION_COUNT = 3
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_MAX_LENGTH = 12

    def __init__(self, id: str, name: str, member_id: str, password: str, role: str, avatar: str, phone_number: str,
                 student_number: str, birth: datetime, email: str):
        self._validate_name(name=name)
        self._validate_member_id(member_id=member_id)
        self._validate_password(password=password)
        self._validate_student_number(student_number=student_number)
        self._validate_email(email=email)
        
        self.__id = id
        self.__name = name
        self.__member_id = member_id
        self.__password = password
        self.__role = role
        self.__avatar = avatar
        self.__phone_number = phone_number
        self.__student_number = student_number
        self.__birth = birth
        self.__email = email

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def member_id(self) -> str:
        return self.__member_id

    @property
    def password(self) -> str:
        return self.__password

    @property
    def role(self) -> str:
        return self.__role

    @property
    def avatar(self) -> str:
        return self.__avatar

    @property
    def phone_number(self) -> str:
        return self.__phone_number

    @property
    def student_number(self) -> str:
        return self.__student_number

    @property
    def birth(self) -> datetime:
        return self.__birth

    @property
    def email(self) -> str:
        return self.__email
    
    def _validate_name(self, name: str) -> None:
        """
        이름의 유효성을 검사합니다.
        """
        if name is None:
            raise ValueError(f"현재 이름: None")
        
        if not (self.name_regex_korean.match(name) or self.name_regex_english.match(name)):
            raise ValueError(f"현재 이름: {name}")
      
    def _validate_member_id(self, member_id: str) -> None:
        """
        아이디의 유효성을 검사합니다.
        """
        if member_id is None:
            raise ValueError(f"현재 아이디: None")
        
        if User.member_id_regex.match(member_id) is None:
            raise ValueError(f"현재 아이디: {member_id}")

    def _validate_password(self, password):
        """
        비밀번호의 유효성을 검사합니다.
        """
        if password is None:
            raise ValueError(f"현재 비밀번호: None")
        if not (User.PASSWORD_MIN_LENGTH < len(password) < User.PASSWORD_MAX_LENGTH):
            raise ValueError(f"현재 비밀번호 길이: {len(password)}")

        count = 0

        if User.password_regex_lower.search(password):
            count += 1
        if User.password_regex_upper.search(password):
            count += 1
        if User.password_regex_digits.search(password):
            count += 1
        if User.password_regex_special_word.search(password):
            count += 1

        if count < User.PASSWORD_VALIDATE_CONDITION_COUNT:
            raise ValueError(f"현재 비밀번호: {password}")

    def _validate_student_number(self, student_number: str) -> None:
        """
        학번의 유효성을 검사합니다.
        """
        if student_number is None:
            raise ValueError(f"현재 학번: None")

        if User.student_number_regex.match(student_number) is None:
            raise ValueError(f"현재 학번: {student_number}")
        
    def _validate_email(self, email: str) -> None:
        """
        이메일의 유효성을 검사합니다.
        """
        if email is None:
            raise ValueError(f"현재 이메일: None")
        
        if User.email_regex.match(email) is None:
            raise ValueError(f"현재 이메일: {email}")
