import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.tracker import router as track_session_router

load_dotenv()  # Load environment variables from .env

app = FastAPI()

# === CORS ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change in production to your client URL!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Routes ===
app.include_router(track_session_router, prefix="/track-session")

# === Run App ===
if __name__ == "__main__":
    import uvicorn

    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 3000))
    uvicorn.run("main:app", host=host, port=port, reload=True)
