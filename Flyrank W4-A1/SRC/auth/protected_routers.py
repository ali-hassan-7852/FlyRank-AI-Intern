from fastapi import APIRouter, Header, HTTPException

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
    # Not verifying yet — just confirming a token was presented (Stage 3 adds verification)
    return {"message": "Token received (not yet verified)"}