from aiohttp import ClientSession
from asyncio import run


async def fetch(url: str) -> bytes:
    async with ClientSession() as session:
        async with session.get(url) as resp:
            response = await resp.read()
    assert len(response) == 399609


if __name__ == "__main__":
    response = run(
        fetch("https://tomdeneire.be/static/homepage/img/profile.png")
    )
