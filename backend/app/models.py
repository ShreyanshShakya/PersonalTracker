from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Text, Date
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "user"
    
    id = Column(String, primary_key=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    emailVerified = Column(Boolean, nullable=False)
    image = Column(String, nullable=True)
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)

class Session(Base):
    __tablename__ = "session"

    id = Column(String, primary_key=True)
    expiresAt = Column(DateTime, nullable=False)
    token = Column(String, unique=True, nullable=False)
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)
    ipAddress = Column(String, nullable=True)
    userAgent = Column(String, nullable=True)
    userId = Column(String, ForeignKey("user.id"), nullable=False)

class Account(Base):
    __tablename__ = "account"

    id = Column(String, primary_key=True)
    accountId = Column(String, nullable=False)
    providerId = Column(String, nullable=False)
    userId = Column(String, ForeignKey("user.id"), nullable=False)
    accessToken = Column(String, nullable=True)
    refreshToken = Column(String, nullable=True)
    idToken = Column(String, nullable=True)
    accessTokenExpiresAt = Column(DateTime, nullable=True)
    refreshTokenExpiresAt = Column(DateTime, nullable=True)
    scope = Column(String, nullable=True)
    password = Column(String, nullable=True)
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)

class Verification(Base):
    __tablename__ = "verification"

    id = Column(String, primary_key=True)
    identifier = Column(String, nullable=False)
    value = Column(String, nullable=False)
    expiresAt = Column(DateTime, nullable=False)
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)

class Project(Base):
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    deadline = Column(DateTime(timezone=True), nullable=True)
    progress = Column(Integer, default=0) # e.g. 0 to 100 percentage
    userId = Column(String, ForeignKey("user.id"), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    description = Column(Text, nullable=True)
    completed = Column(Boolean, default=False)
    projectId = Column(Integer, ForeignKey("projects.id"), nullable=True)
    userId = Column(String, ForeignKey("user.id"), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())

class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    userId = Column(String, ForeignKey("user.id"), nullable=False)
    currentStreak = Column(Integer, default=0)
    longestStreak = Column(Integer, default=0)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())

class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)
    habitId = Column(Integer, ForeignKey("habits.id"), nullable=False)
    date = Column(Date, nullable=False) # Only store the year-month-day
    completed = Column(Boolean, default=True)

class TimeSession(Base):
    __tablename__ = "time_sessions"
    
    id = Column(Integer, primary_key=True, index=True)
    taskId = Column(Integer, ForeignKey("tasks.id"), nullable=True)
    userId = Column(String, ForeignKey("user.id"), nullable=False)
    startTime = Column(DateTime(timezone=True), nullable=False)
    endTime = Column(DateTime(timezone=True), nullable=True)
    durationSeconds = Column(Integer, nullable=True)

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    content = Column(Text, nullable=True) # Markdown text
    tags = Column(String, nullable=True) # Comma separated for now
    aiSummary = Column(Text, nullable=True)
    userId = Column(String, ForeignKey("user.id"), nullable=False)
    createdAt = Column(DateTime(timezone=True), server_default=func.now())
    updatedAt = Column(DateTime(timezone=True), onupdate=func.now())
