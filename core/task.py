from dataclasses import dataclass, field
from typing import Dict
import uuid


@dataclass
class Task:

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    agent: str = ""

    tool: str = ""

    arguments: Dict = field(default_factory=dict)

    status: str = "waiting"