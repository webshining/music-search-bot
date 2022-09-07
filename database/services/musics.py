from ..models import Music


def create_music(href: str, music_href: str, name: str, text: str, user: int):
    music = Music.create(href=href, music_href=music_href, name=name, text=text, user=user)
    return music


def get_music(id: int = None, href: str = None):
    return Music.get_or_none((Music.id == id) if id else (Music.href == href))


def delete_music(href: str, user: int):
    music = Music.get_or_none(Music.user == user, Music.href == href)
    music.delete_instance()
    return True
