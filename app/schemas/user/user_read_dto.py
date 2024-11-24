from app.domains.user import User


class UserReadDTO:
    def __init__(self, user_entity: User):
        self.__name = user_entity.name
        self.__role = user_entity.role
        self.__email = user_entity.email
        self.__avatar = user_entity.avatar
        self.__phone_number = user_entity.phone_number
