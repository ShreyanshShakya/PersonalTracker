# Personal AI OS

A Personal AI Operating System designed to act as your second brain. Built for complete privacy, maximum productivity, and stunning aesthetics.

## 🚀 Features

### **Phase 1: Foundation & Identity**
- **Authentication:** Secure email/password login powered by Better Auth.
- **Tasks Dashboard:** A highly responsive to-do list with optimistic UI updates (powered by TanStack Query).
- **Modern UI:** Built with Tailwind CSS v4, Lucide icons, and a premium dark-mode-first aesthetic.

### **Phase 2: Productivity Core**
- **Projects Hub:** Organize your goals with progress bars and deadline tracking.
- **Habit Tracker:** Build daily consistency with a visual streak tracker.
- **Knowledge Base (Notes):** A split-pane Markdown editor with real-time GitHub-flavored rendering.
- **Global Time Tracker:** A floating, toggleable widget that persists across your dashboard to track time spent on specific tasks.

*(Phase 3: AI Assistant integrations coming soon!)*

---

## 🛠 Tech Stack
- **Frontend:** Next.js 16 (Turbopack), React 19, Tailwind CSS v4, TanStack Query.
- **Backend:** FastAPI, Python, SQLAlchemy, Alembic.
- **Database:** PostgreSQL (with `pgvector` for future AI memory) & Redis.
- **Auth:** Better Auth.

---

## 💻 Local Development Setup

### 1. Start Infrastructure (PostgreSQL & Redis)
Ensure you have Docker installed and running.
```bash
docker compose up -d
```

### 2. Configure Environment Variables
In the `frontend` directory, create a `.env.local` file:
```env
BETTER_AUTH_URL=http://<YOUR_IP>:3000
BETTER_AUTH_SECRET=my_super_secret_key_12345
DATABASE_URL=postgresql://postgres:password@localhost:5432/personal_os
NEXT_PUBLIC_APP_URL=http://<YOUR_IP>:3000
```
*(Replace `<YOUR_IP>` with your local network IP if you are accessing via a phone/tablet, or `localhost` if testing strictly on your machine).*

### 3. Start the Backend
Open a new terminal in the `backend` directory.
```bash
# Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Database Migrations
alembic upgrade head

# Start FastAPI (accessible on your local network)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### 4. Start the Frontend
Open another terminal in the `frontend` directory.
```bash
# Install dependencies
npm install

# Start Next.js development server
npm run dev
```

Visit `http://localhost:3000` (or your local IP) to sign up and access your dashboard!
