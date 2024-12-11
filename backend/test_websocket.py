import asyncio
import websockets
import json

async def test_websocket():
    uri = "ws://localhost:8000/ws/updates"
    async with websockets.connect(uri) as websocket:
        # Send a test message
        test_message = json.dumps({"type": "test", "data": "Hello WebSocket"})
        print(f"Sending: {test_message}")
        await websocket.send(test_message)

        # Receive the response
        response = await websocket.recv()
        print(f"Received: {response}")

if __name__ == "__main__":
    asyncio.run(test_websocket())
