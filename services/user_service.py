from db import registered_emails, users
from models.user import User
from errors.errors import AlreadyRegisteredError


def register_user(name: str, age: int, email: str):
    '''
    reisters a new user
    '''
    if email.lower() in registered_emails:
        raise AlreadyRegisteredError()
    new_user = User(name, age, email)
    registered_emails.add(email.lower())
    users.append(new_user)
    return new_user
