import os
import glob
from sqlalchemy import create_engine, text

# 1. Connect to DB and drop everything
engine = create_engine("postgresql://postgres:password@localhost:5432/personal_os")
with engine.begin() as conn:
    conn.execute(text("DROP SCHEMA public CASCADE;"))
    conn.execute(text("CREATE SCHEMA public;"))
    conn.execute(text("GRANT ALL ON SCHEMA public TO postgres;"))
    conn.execute(text("GRANT ALL ON SCHEMA public TO public;"))

print("Database wiped clean.")

# 2. Delete all old migration files
migration_dir = "alembic/versions"
for filename in glob.glob(os.path.join(migration_dir, "*.py")):
    try:
        os.remove(filename)
        print(f"Deleted old migration: {filename}")
    except OSError:
        pass
