from fastapi import FastAPI
from user.infrastructure.routers import user_route, auth_route
from client.infrastructure.routers import client_route

app = FastAPI()

app.include_router(user_route.router, prefix="/users", tags=["users"])
app.include_router(auth_route.router, prefix="/auth", tags=["auth"])
app.include_router(client_route.router, prefix="/clients", tags=["clients"])