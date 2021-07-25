import aiohttp
import asyncio
from bs4 import BeautifulSoup



async def index(session):
    url = 'https://eurotrips.com.ua/aviatur-v-gruziyu'
    async with session.get(url) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        soup = BeautifulSoup (html, 'html.parser')
        #print(soup)
        name = soup.section['data-name']
        price = soup.section['data-price-usd']
        print(name, price)
        #print("Body:", html, "...")


async def doc(session):
    url = "https://eurotrips.com.ua/fly-avia-u-kappadokiyu"
    async with session.get(url) as response:
        print("Status:", response.status)
        print("Content-type:", response.headers['content-type'])

        html = await response.text()
        soup = BeautifulSoup (html, 'html.parser')
        #print(soup)
        name = soup.section['data-name']
        price = soup.section['data-price-usd']
        print(name, price)
        #print("Body:", html, "...")

async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(index(session), doc(session))



if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
