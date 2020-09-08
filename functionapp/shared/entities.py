import dataclasses
from dataclasses import dataclass
from typing import List
@dataclass
class Person:

    fname: str
    lname: str
    challenges: List[dict] = None
    activities: List[dict] = None
