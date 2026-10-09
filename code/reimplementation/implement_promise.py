import asyncio


async def delay(ms, value):
    await asyncio.sleep(ms / 1000)
    return value


async def fetch_with_retry(fn, retries):
    try:
        return await fn()
    except Exception:
        if retries <= 0:
            raise
        return await fetch_with_retry(fn, retries - 1)
