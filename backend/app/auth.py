from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from datetime import datetime
from .database import get_db
from .models import Session as SessionModel, User

def get_current_user(request: Request, db: Session = Depends(get_db)):
    # Better Auth sets a cookie named 'better-auth.session_token'
    # We also allow it to be passed in headers for cross-origin frontend fetches
    token = request.cookies.get("better-auth.session_token") or request.headers.get("better-auth.session_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    # Verify token in DB
    session = db.query(SessionModel).filter(SessionModel.token == token).first()
    if not session:
        raise HTTPException(status_code=401, detail="Invalid session")
    
    if session.expiresAt < datetime.utcnow():
        raise HTTPException(status_code=401, detail="Session expired")
    
    user = db.query(User).filter(User.id == session.userId).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
        
    return user
