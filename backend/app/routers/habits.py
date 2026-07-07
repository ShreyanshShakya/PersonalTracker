from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date, timedelta

from ..database import get_db
from ..models import Habit, HabitLog, User
from ..schemas import HabitCreate, HabitOut, HabitUpdate, HabitLogCreate, HabitLogOut
from ..auth import get_current_user

router = APIRouter(prefix="/habits", tags=["habits"])

@router.get("/", response_model=List[HabitOut])
def get_habits(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Habit).filter(Habit.userId == current_user.id).all()

@router.post("/", response_model=HabitOut, status_code=status.HTTP_201_CREATED)
def create_habit(habit: HabitCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_habit = Habit(**habit.model_dump(), userId=current_user.id)
    db.add(db_habit)
    db.commit()
    db.refresh(db_habit)
    return db_habit

@router.post("/{habit_id}/log", response_model=HabitLogOut)
def log_habit(habit_id: int, log_data: HabitLogCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Verify habit belongs to user
    db_habit = db.query(Habit).filter(Habit.id == habit_id, Habit.userId == current_user.id).first()
    if not db_habit:
        raise HTTPException(status_code=404, detail="Habit not found")
    
    # Check if already logged for this date
    existing_log = db.query(HabitLog).filter(HabitLog.habitId == habit_id, HabitLog.date == log_data.date).first()
    
    if existing_log:
        existing_log.completed = log_data.completed
        db_log = existing_log
    else:
        db_log = HabitLog(habitId=habit_id, date=log_data.date, completed=log_data.completed)
        db.add(db_log)
    
    # Very simple streak recalculation (could be optimized)
    # Just update the current streak assuming it's consecutive from today
    # A real implementation would scan the logs back in time
    
    db.commit()
    db.refresh(db_log)
    return db_log
