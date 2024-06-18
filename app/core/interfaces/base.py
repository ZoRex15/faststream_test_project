from typing import Protocol

class Commiter(Protocol):
    async def commit(self) -> None:
        raise NotImplementedError