import os

base = 'backend'
files = {
    'app/__init__.py': '',
    'app/main.py': 'from fastapi import FastAPI\nfrom app.api.routes import router\n\napp = FastAPI(title="Jarvis AI API")\n\napp.include_router(router)\n\n@app.get("/")\ndef read_root():\n    return {"message": "Welcome to Jarvis AI"}\n',
    'app/api/__init__.py': '',
    'app/api/routes.py': 'from fastapi import APIRouter\n\nrouter = APIRouter()\n\n@router.get("/status")\ndef status():\n    return {"status": "ok"}\n',
    'app/core/__init__.py': '',
    'app/core/config.py': 'import os\n\nclass Settings:\n    pass\n\nsettings = Settings()\n',
    'app/core/security.py': '# Security helpers\n',
    'app/services/__init__.py': '',
    'app/services/ai_service.py': 'def get_ai_response(prompt: str):\n    pass\n',
    'app/services/voice_service.py': 'def process_voice():\n    pass\n',
    'app/services/automation_service.py': 'def run_automation():\n    pass\n',
    'app/services/memory_service.py': 'def remember():\n    pass\n',
    'app/models/__init__.py': '',
    'app/models/schemas.py': 'from pydantic import BaseModel\n\nclass MessageStatus(BaseModel):\n    status: str\n',
    'app/utils/__init__.py': '',
    'app/utils/helpers.py': 'def helper():\n    pass\n',
    'requirements.txt': 'fastapi\nuvicorn[standard]\npydantic\npython-dotenv\nrequests\n',
    '.env': '# Environment variables\n'
}

for filepath, content in files.items():
    full_path = os.path.join(base, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)

print("Backend structure built successfully.")
