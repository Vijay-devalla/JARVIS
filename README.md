# Jarvis AI

A modern Web Application containing a React frontend and a FastAPI backend.

## Project Structure

- `frontend/`: React application powered by Vite.
- `backend/`: Python backend powered by FastAPI.
- `docker-compose.yml`: For running both services together.

## Running the project

### Using Docker

If you have Docker installed, you can easily spin up the environment:
```bash
docker-compose up --build
```
This will start:
- Frontend on `http://localhost:5173`
- Backend API on `http://localhost:8000`

### Running Locally

**Backend (Requires Python >= 3.8):**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Frontend (Requires Node.js):**
```bash
cd frontend
npm install
npm run dev
```
