from ..models import Music


def create_music(name: str, file_id: str, text: str, user: int):
    music = Music.create(name=name, file_id=file_id, text=text, user=user)
    return music



def get_music(id: int = None, href: str = None):
    return Music.get_by_id(id)


def delete_music(id: int):
    music = Music.get_by_id(id)
    music.delete_instance()
    return True
