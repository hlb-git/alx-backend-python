#!/usr/bin/env python3
"""async_comprehension module"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension: coroutine that collects 10 random numbers using an async comprehensing"""
    return [n async for n in async_generator()]
