from dataclasses import dataclass
from aiogram import Router
from .registration import router as registration_router


@dataclass(frozen=True)
class BotRoutes:
    routers: tuple

    def register_routes(self, app: Router):
        for router in self.routers:
            app.include_router(router)


__routes__ = BotRoutes(routers=(registration_router,))
