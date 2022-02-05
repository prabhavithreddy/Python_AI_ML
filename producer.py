import asyncio
import websockets

async def produce(message:str, host:str, port:int) -> None:
    async with websockets.connect(f"ws://{host}:{port}") as ws:
        await ws.send("Hello")
        await ws.recv()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(produce('Hello World!',host='localhost', port=4000))