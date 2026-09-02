from fastapi import APIRouter, status, Depends
from SRC.auth.dtos import AuthSchema
from SRC.auth.controllers import signup, login, logout
from SRC.auth.protected_routers import get_current_user

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.post("/signup", status_code=status.HTTP_201_CREATED)
def signup_route(body: AuthSchema):
    return signup(body)

@auth_router.post("/login")
def login_route(body: AuthSchema):
    return login(body)

@auth_router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout_route(user=Depends(get_current_user)):
    logout()