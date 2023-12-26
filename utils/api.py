import asyncio

from requests_html import AsyncHTMLSession

URL = 'https://holychords.pro'


async def get_songs(search_name: str):
    session = AsyncHTMLSession(loop=asyncio.get_event_loop())
    search_name = '+'.join(search_name.split(' '))
    r = await session.get(f'{URL}/search?name={search_name}')
    results = [
        {'href': a.attrs['data-audio-id'], 'name': a.attrs['data-audio-name'], 'artist': a.attrs['data-artist-name']}
        for a in r.html.find('a.mr-3.play')]
    return results


async def get_text(href: str):
    session = AsyncHTMLSession()
    r = await session.get(f'{URL}/{href}')
    await r.html.arender()
    result = []
    blocks = r.html.find('.blocks')
    if blocks:
        for i in blocks:
            videlit_line = i.find(".videlit_line", first=True).text
            text = '\n'.join([i.text for i in i.find('.text')])
            if videlit_line:
                result.append(f'<b>{videlit_line}</b>')
            if text:
                result.append(text)
    return '\n'.join(result) if result else None
