import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from app.main import app, tasks


@pytest_asyncio.fixture
async def client():
    tasks.clear()
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="httpx://test"
    ) as c:
        yield c
