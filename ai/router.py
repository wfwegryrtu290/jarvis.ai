from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Optional


@dataclass
class Route:
    name: str
    handler: Callable
    description: str = ""


class AIRouter:
    """
    Централен Router.

    Избира кой агент трябва да изпълни задачата.
    """

    def __init__(self):
        self.routes: Dict[str, Route] = {}

    def register(
        self,
        name: str,
        handler: Callable,
        description: str = ""
    ) -> None:

        self.routes[name.lower()] = Route(
            name=name.lower(),
            handler=handler,
            description=description
        )

    def unregister(self, name: str) -> None:

        self.routes.pop(name.lower(), None)

    def resolve(self, name: str) -> Optional[Route]:

        return self.routes.get(name.lower())

    def dispatch(
        self,
        name: str,
        *args,
        **kwargs
    ):

        route = self.resolve(name)

        if route is None:
            raise ValueError(
                f"Няма регистриран route: {name}"
            )

        return route.handler(
            *args,
            **kwargs
        )

    def list_routes(self):

        return {
            key: value.description
            for key, value in self.routes.items()
        }


router = AIRouter()
