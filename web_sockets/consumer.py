import asyncio
import websockets
from websockets.legacy.client import WebSocketClientProtocol


async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
    async for message in websocket:
        print("Message: ",message)

async def consume(hostname: str, port: int) -> None:
    websocket_resource_url = f"ws://{hostname}:{port}"
    async with websockets.connect(websocket_resource_url) as websocket:
        await consumer_handler(websocket)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete((consume(hostname='localhost', port=4000)))
    loop.run_forever()