from ..models import User


def get_user(id: int) -> User or None:
    user = User.get_or_none(User.id == id)
    return user


def create_user(id: int, name: str, username: str) -> User:
    user = User.create(id=id, name=name, username=username)
    return user


async def get_or_create_user(id: int, name: str, username: str):
    user = get_user(id)
    if user:
        user.name = name
        user.username = username
        user.save()
    else:
        user = create_user(id, name, username)
    return user