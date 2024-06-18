from dataclasses import dataclass

from datetime import date


@dataclass
class User:
    tg_id: int
    join_date: date
    id: int | None = None