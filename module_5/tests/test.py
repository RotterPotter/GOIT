import asyncio
from time import sleep, time


fake_users = [
    {'id': 1, 'name': 'April Murphy', 'company': 'Bailey Inc', 'email': 'shawnlittle@example.org'},
    {'id': 2, 'name': 'Emily Alexander', 'company': 'Martinez-Smith', 'email': 'turnerandrew@example.org'},
    {'id': 3, 'name': 'Patric Jones', 'company': 'Young, Pruitt and Milller', 'email': 'alancoleman@example.net'}
]


def get_user_sync(uid:int) -> dict:
    sleep(0.5)
    user, = list(filter(lambda user: user["id"] == uid, fake_users))
    return user

async def get_user_async(uid:int) -> dict:
    print(f'In function {uid}')
    await asyncio.sleep(0.5)
    user, = list(filter(lambda user: user['id'] == uid, fake_users))
    print(f'Out function {uid}')
    return user

async def main():
    r = []
    for i in range(1,4):
        r.append(get_user_async(i))
    return await asyncio.gather(*r)
    
if __name__ == '__main__':
    result = asyncio.run(main())
    print(result)