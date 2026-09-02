from fastapi import APIRouter, Header, HTTPException, Depends
from SRC.utils.supabase_client import supabase

public_router = APIRouter(tags=["public"])
protected_router = APIRouter(prefix="/protected", tags=["protected"])

def get_current_user(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, detail="Access token required")

    token = authorization.split(" ")[1]

    try:
        result = supabase.auth.get_user(token)
    except Exception:
        raise HTTPException(401, detail="Invalid or expired token")

    if not result or not result.user:
        raise HTTPException(401, detail="Invalid or expired token")

    return result.user


@public_router.get("/public/info")
def public_info():
    return {"message": "Welcome stranger! This info is public."}


@protected_router.get("/profile")
def profile(user=Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at,
    }


@protected_router.get("/dashboard")
def dashboard(user=Depends(get_current_user)):
    return {"message": f"Welcome to your dashboard, {user.email}"}