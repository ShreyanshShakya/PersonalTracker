from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import User, Account

DATABASE_URL = "postgresql://postgres:password@localhost:5432/personal_os"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

print("--- USERS ---")
users = db.query(User).all()
for u in users:
    print(f"ID: {u.id}, Name: {u.name}, Email: {u.email}")

print("\n--- ACCOUNTS (Includes Passwords) ---")
accounts = db.query(Account).all()
for a in accounts:
    print(f"User ID: {a.userId}, Provider: {a.providerId}, Password Hash: {a.password}")
