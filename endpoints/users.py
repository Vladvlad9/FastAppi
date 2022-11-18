from fastapi import APIRouter

from crud.users import CRUDUser
from schemas import UserSchema, UserInDBSchema

router = APIRouter()


#limit: int = 10, skip: int = 100
@router.get("/")
async def read_users():
    return await CRUDUser.get_all()


@router.post("/", response_model=UserSchema)
async def add(user: UserSchema):
    return await CRUDUser.add(user=user)


@router.put("/", response_model=UserSchema)
async def update(user: UserInDBSchema):
    return await CRUDUser.update(users=user)