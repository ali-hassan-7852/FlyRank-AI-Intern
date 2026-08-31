from fastapi import APIRouter
from SRC.auth.dtos import AuthSchema
from SRC.auth.controllers import signup, login

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/signup")
def signup_route(body: AuthSchema):
    return signup(body)

@auth_router.post("/login")
def login_route(body: AuthSchema):
    return login(body)