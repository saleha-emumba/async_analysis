import time
import aiohttp
import asyncio
from typing import Dict, List


async def fetch(session: aiohttp.ClientSession, url: str) -> Dict:
    start = time.perf_counter()

    try:
        async with session.get(url, timeout=10) as resp:
            await resp.text()
            return {
                "url": url,
                "status": resp.status,
                "time": time.perf_counter() - start,
            }

    except Exception as e:
        # import pdb
        # pdb.set_trace()  # Add BREAKPOINT HERE FOR DEBUGGING!
        return {
            "url": url,
            "status": None,
            "time": time.perf_counter() - start,
            "error": str(e),
        }

    except Exception as e:
        return {
            "url": url,
            "status": None,
            "time": time.perf_counter() - start,
            "error": str(e),
        }


async def fetch_all(urls: List[str], limit: int = 10) -> List[Dict]:
    results: List[Dict] = []
    sem = asyncio.Semaphore(limit)

    async def limited_fetch(url: str):
        async with sem:
            result = await fetch(session, url)
            results.append(result)

    async with aiohttp.ClientSession() as session:
        async with asyncio.TaskGroup() as tg:
            for url in urls:
                tg.create_task(limited_fetch(url))

    return results
