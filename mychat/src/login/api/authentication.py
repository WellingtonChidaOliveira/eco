from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from ..application.user_service import UserService
from ..schemas.user_schemas import UserLogin, UserCreate
from ..infrastructure.database import get_session

router = APIRouter()

@router.post("/login")
def login_user(user: UserLogin, session: Session = Depends(get_session)):
    user_service = UserService(session)
    try:
        token = user_service.login(user)
        return JSONResponse(status_code=200, content={"access_token": token, "token_type": "bearer"})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/register")
def register_user(user: UserCreate, session: Session = Depends(get_session)):
    user_service = UserService(session)
    try:
        token = user_service.register(user)
        return JSONResponse(status_code=201, content={"message": "User created successfully.", "access_token": token, "token_type": "bearer"})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/users")
def get_users(session: Session = Depends(get_session)):
    return JSONResponse(status_code=200, content={"hello": "world"})

@router.delete("/user/{email}")
def delete_user(email: str, session: Session = Depends(get_session)):
    user_service = UserService(session)
    try:
        user_service.delete(email)
        return JSONResponse(status_code=200, content={"message": "User deleted successfully."})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))