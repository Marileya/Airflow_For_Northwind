import asyncio

from core.db import check_connection


if __name__ == "__main__":
    asyncio.run(check_connection())
