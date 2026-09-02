from fastapi import APIRouter, Header, HTTPException
from SRC.utils.supabase_client import supabase

public_router = APIRouter(tags=["public"])
protected_router = APIRouter(prefix="/protected", tags=["protected"])

@public_router.get("/public/info")
def public_info():
    return {"message": "Welcome stranger! This info is public."}

@protected_router.get("/profile")
def profile(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(401, detail="Access token required")

    token = authorization.split(" ")[1]

    try:
        result = supabase.auth.get_user(token)
    except Exception as e:
        print("DEBUG get_user error:", repr(e))
        raise HTTPException(401, detail="Invalid or expired token")

    if not result or not result.user:
        print("DEBUG result was falsy:", result)
        raise HTTPException(401, detail="Invalid or expired token")

    user = result.user
    return {
        "id": user.id,
        "email": user.email,
        "created_at": user.created_at,
    }