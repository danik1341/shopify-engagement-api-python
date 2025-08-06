from fastapi import APIRouter
from models.session import SessionData
from services.tracker import handle_session

router = APIRouter()


@router.post("")
async def track_session(session: SessionData):
    return handle_session(session)
