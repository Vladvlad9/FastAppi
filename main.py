from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


from fastapi import FastAPI
import uvicorn

from crud.users import CRUDUser
from endpoints import users
from models import ASYNC_ENGINE, Base
from schemas import UserSchema

app = FastAPI(title="MyfirstProject in FastAPI")
app.include_router(users.router, prefix="/users", tags=["users"])

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="styles")
app.mount("/static", StaticFiles(directory="static"), name="pink")
app.mount("/static", StaticFiles(directory="static"), name="stat_js")


@app.get("/index2/", response_class=HTMLResponse)
async def index(request: Request):
    users = await CRUDUser.get_all()

    context = {'request': request, 'users': users}
    return templates.TemplateResponse("index.html", context=context)


# @app.post("/items/add_users/", response_class=HTMLResponse)
# async def add_users(request: Request, user: UserSchema):
#     users = await CRUDUser.get_all()
#     context = {'request': request, 'users': users}
#     return templates.TemplateResponse("add_users.html", context=context)


@app.on_event("startup")
async def startup():
    async with ASYNC_ENGINE.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.on_event("shutdown")
async def shutdown():
    await ASYNC_ENGINE.disconnect()


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", reload=True)