from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timezone

from ..database import get_db
from ..models import TimeSession, User, Task
from ..schemas import TimeSessionCreate, TimeSessionOut
from ..auth import get_current_user

router = APIRouter(prefix="/time-sessions", tags=["time-sessions"])

@router.get("/", response_model=List[TimeSessionOut])
def get_time_sessions(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(TimeSession).filter(TimeSession.userId == current_user.id).all()

@router.post("/start", response_model=TimeSessionOut, status_code=status.HTTP_201_CREATED)
def start_session(session: TimeSessionCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Check if there is already an active session
    active = db.query(TimeSession).filter(TimeSession.userId == current_user.id, TimeSession.endTime == None).first()
    if active:
        raise HTTPException(status_code=400, detail="A time session is already active. Please stop it first.")
        
    db_session = TimeSession(
        taskId=session.taskId,
        userId=current_user.id,
        startTime=datetime.now(timezone.utc)
    )
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session

@router.post("/{session_id}/stop", response_model=TimeSessionOut)
def stop_session(session_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_session = db.query(TimeSession).filter(TimeSession.id == session_id, TimeSession.userId == current_user.id).first()
    if not db_session:
        raise HTTPException(status_code=404, detail="Time session not found")
        
    if db_session.endTime is not None:
        raise HTTPException(status_code=400, detail="Session is already stopped")
        
    db_session.endTime = datetime.now(timezone.utc)
    # Calculate duration
    duration = db_session.endTime - db_session.startTime
    db_session.durationSeconds = int(duration.total_seconds())
    
    db.commit()
    db.refresh(db_session)
    return db_session
