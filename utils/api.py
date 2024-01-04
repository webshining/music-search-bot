import asyncio
import re

from pydantic import BaseModel, model_validator
from requests_html import AsyncHTMLSession


class Song(BaseModel):
    id: int
    name: str
    artist: str
    file: str
    text: str

    def get_text(self, chords: bool = False) -> list[str] | str:
        if not chords:
            remove_chords = re.compile(
                r'([A-H][b\#/]?(2|5|6|7|9|11|13|\+|\+2|\+4|\+5|\+6|\+7|\+9|\+11|\+13|6\/9|7\-5|7\-9|7\#5|\#5|7\#9|\#9|7\+3|7\+5|7\+9|7b5|7b9|7sus2|7sus4|sus4|add2|add4|add6|add9|aug|dim|dim7|m\/maj7|m6|m7|m7b5|m9|m11|m13|maj|maj7|maj9|maj11|maj13|mb5|m|sus|sus2|sus4|m7add11|add11|b5|-5|4)*)')
            return '\n'.join([i for i in remove_chords.sub('', self.text).split('\n') if i.strip()])
        return self.text

    @model_validator(mode="before")
    @classmethod
    def isp_name(cls, data: dict) -> str:
        data["artist"] = data["artist"]["isp_name"]
        return data


URL = 'https://holychords.pro'


async def get_songs(search_name: str) -> list[Song]:
    session = AsyncHTMLSession(loop=asyncio.get_event_loop())
    search_name = '+'.join(search_name.split(' '))
    r = await session.get(f'{URL}/search?name={search_name}', headers={"X-Requested-With": "XMLHttpRequest"})
    return [Song(**i) for i in r.json()["musics"]["data"]]
