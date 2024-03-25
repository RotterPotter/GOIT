import sys 
import aiohttp
import asyncio
from datetime import datetime, timedelta



now_date = datetime.now()

async def create_dates(number_of_days:int) -> list:
    dates = []

    for i in range(number_of_days):
        date = now_date - timedelta(i)
        date = ".".join(reversed(str(date).split(' ')[0].split('-')))
        dates.append(date)
    return dates

async def create_links(dates:list):
    links = []

    for date in dates:
        link = f'https://api.privatbank.ua/p24api/exchange_rates?date={date}'
        links.append(link)

    return links

async def take_data(session: aiohttp.ClientSession, link:str) -> str:
    try:
        async with session.get(link) as response:
            if response.status == 200:
                result = await response.json()
                return await result
                
            
            
    except aiohttp.ServerTimeoutError as error:
        return str(error)
    
    except aiohttp.ClientConnectionError as error:
        return str(error)

async def format_data(data:list):
    new_lst = list()

    for json in data:
        if json["exchangeRate"][1] and json["exchangeRate"][6]:
            my_dict = {json["date"]:{
                "EUR": {
                    "sale": json["exchangeRate"][1]["saleRateNB"],
                    "purchase": json["exchangeRate"][1]["purchaseRateNB"]
                },
                "USD":{
                    "sale": json["exchangeRate"][6]["saleRateNB"],
                    "purchase": json["exchangeRate"][6]["saleRateNB"] 
                } 
            }}
            new_lst.append(my_dict)
    return new_lst

async def main():
    number_of_days = int(sys.argv[1])
    dates = await create_dates(number_of_days)
    links = await create_links(dates)

    async with aiohttp.ClientSession() as session:
        res: list = await asyncio.gather(
            *([take_data(session, link) for link in links])
        )
        print(await format_data(res))

        

if __name__ == '__main__':
    asyncio.run(main())