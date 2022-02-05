import asyncio

async def foo():
    async for i in range(1, 101):
        await print(i, end='\n')

if __name__ == '__main_':
    loop = asyncio.get_event_loop()
    loop.run(foo())