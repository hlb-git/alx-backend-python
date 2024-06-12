#!/usr/bin/env python3
"""async_generator module"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """async_generator: coroutine that loops 10 times, each time asynchronously"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
