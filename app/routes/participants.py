from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.participant import Participant
from app.schemas.participant import ParticipantCreate, ParticipantOut

router = APIRouter(prefix="/participants", tags=["Participants"])

@router.post("/", response_model=ParticipantOut)
def create_participant(participant: ParticipantCreate, db: Session = Depends(get_db)):
    db_participant = Participant(user_id=participant.user_id, trivia_id=participant.trivia_id)
    db.add(db_participant)
    db.commit()
    db.refresh(db_participant)
    return db_participant

@router.get("/", response_model=List[ParticipantOut])
def list_participants(db: Session = Depends(get_db)):
    return db.query(Participant).all()
