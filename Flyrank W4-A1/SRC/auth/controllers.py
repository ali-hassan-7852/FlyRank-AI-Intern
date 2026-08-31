from fastapi import HTTPException
from SRC.auth.dtos import AuthSchema
from SRC.utils.supabase_client import supabase

def signup(body: AuthSchema):
    if not body.email or not body.password:
        raise HTTPException(400, detail="Email and password are required")

    try:
        result = supabase.auth.sign_up({"email": body.email, "password": body.password})
    except Exception as e:
        raise HTTPException(400, detail=str(e))

    return {"status": "User created successfully", "data": result.user}

def login(body: AuthSchema):
    if not body.email or not body.password:
        raise HTTPException(400, detail="Email and password are required")

    try:
        result = supabase.auth.sign_in_with_password({"email": body.email, "password": body.password})
    except Exception:
        raise HTTPException(401, detail="Invalid login credentials")

    return {
        "status": "Login successful",
        "access_token": result.session.access_token,
        "refresh_token": result.session.refresh_token,
    }