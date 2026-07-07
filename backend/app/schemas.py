from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

# --- Projects ---
class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None
    deadline: Optional[datetime] = None
    progress: int = 0

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    title: Optional[str] = None

class ProjectOut(ProjectBase):
    id: int
    userId: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True

# --- Tasks ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
    projectId: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: Optional[str] = None
    completed: Optional[bool] = None
    projectId: Optional[int] = None

class TaskOut(TaskBase):
    id: int
    userId: str
    createdAt: datetime
    updatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True

# --- Habits ---
class HabitBase(BaseModel):
    title: str

class HabitCreate(HabitBase):
    pass

class HabitUpdate(HabitBase):
    title: Optional[str] = None

class HabitOut(HabitBase):
    id: int
    userId: str
    currentStreak: int
    longestStreak: int
    createdAt: datetime
    updatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True

class HabitLogCreate(BaseModel):
    date: date
    completed: bool = True

class HabitLogOut(BaseModel):
    id: int
    habitId: int
    date: date
    completed: bool

    class Config:
        from_attributes = True

# --- Time Sessions ---
class TimeSessionCreate(BaseModel):
    taskId: Optional[int] = None

class TimeSessionOut(BaseModel):
    id: int
    taskId: Optional[int]
    userId: str
    startTime: datetime
    endTime: Optional[datetime] = None
    durationSeconds: Optional[int] = None

    class Config:
        from_attributes = True

# --- Notes ---
class NoteBase(BaseModel):
    title: str
    content: Optional[str] = None
    tags: Optional[str] = None

class NoteCreate(NoteBase):
    pass

class NoteUpdate(NoteBase):
    title: Optional[str] = None
    content: Optional[str] = None
    tags: Optional[str] = None

class NoteOut(NoteBase):
    id: int
    userId: str
    aiSummary: Optional[str] = None
    createdAt: datetime
    updatedAt: Optional[datetime] = None

    class Config:
        from_attributes = True
