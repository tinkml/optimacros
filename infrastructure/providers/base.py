from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    async def run(self):
        raise NotImplementedError
