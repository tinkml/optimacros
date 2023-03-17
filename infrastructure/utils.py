import abc
import asyncio

from concurrent.futures import ProcessPoolExecutor
from typing import Callable, Any


class CPU(abc.ABC):

    @classmethod
    @abc.abstractmethod
    async def execute(cls, *args, **kwargs):
        raise NotImplementedError


class HighLoadTask(CPU):

    @classmethod
    async def execute(cls, func: Callable, *args) -> Any:
        with ProcessPoolExecutor() as executor:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(executor, func, *args)
            return result
