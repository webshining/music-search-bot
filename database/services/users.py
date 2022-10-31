from ..models import Song, User, users_collection


async def get_users():
    users = await users_collection.find()
    return [User(**u) for u in users]


async def get_user(id: int):
    user = await users_collection.find_one({'id': id})
    return User(**user) if user else None


async def create_user(id: int, name: str, username: str, lang: str):
    user = await users_collection.insert_one({'id': id, 'name': name, 'username': username, 'lang': lang, 'songs': []})
    return await get_user(user.inserted_id)


async def update_user(id: int, **kwargs):
    user = await users_collection.find_one_and_update({'id': id}, {'$set': {**kwargs}}, return_document=True)
    return User(**user)


async def get_or_create_user(id: int, name: str, username: str, lang: str):
    user = await get_user(id)
    user = await update_user(id, name=name, username=username) if user else await create_user(id, name, username, lang)
    return user