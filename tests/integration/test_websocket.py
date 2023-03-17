import pytest
from fastapi.testclient import TestClient

from infrastructure.providers.http import HttpProvider


@pytest.mark.asyncio
@pytest.mark.parametrize("data, answer, valid", (
        ("4", 24, True),
        (4, 24, True),
        ("String", "Value is not a number", False),
))
async def test_websocket(data, answer, valid):
    provider = HttpProvider()
    client = TestClient(provider.web_app)
    with client.websocket_connect("/api/ws/factorial") as websocket:
        websocket.send_text(data)

        received_text = websocket.receive_text()
        assert answer == received_text
