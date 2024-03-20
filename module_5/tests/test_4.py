import platform

import aiohttp
import asyncio


async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('https://api.privatbank.us/p24api/pubinfo?json&exchange&coursid=5') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['Content-type'])
            print("cookies:", response.cookies)
            result = await response.json()
            return result


if __name__ == "__main__":
    r = asyncio.run(main())
    print(r)            
