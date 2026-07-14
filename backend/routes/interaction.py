from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.interaction import Interaction
from app.schemas.interaction import InteractionCreate, InteractionResponse
from app.services.groq_service import generate_ai_response

router = APIRouter(
    prefix="/interactions",
    tags=["Interaction"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=InteractionResponse)
def create_interaction(
    interaction: InteractionCreate,
    db: Session = Depends(get_db)
):

    # Generate AI response
    ai_result = generate_ai_response(interaction.notes)

    new_interaction = Interaction(
        hcp_id=interaction.hcp_id,
        notes=interaction.notes,
        summary=ai_result,
        follow_up="AI suggested follow-up",
        sentiment="AI analyzed sentiment"
    )

    db.add(new_interaction)
    db.commit()
    db.refresh(new_interaction)

    return new_interaction


@router.get("/", response_model=list[InteractionResponse])
def get_interactions(
    db: Session = Depends(get_db)
):
    interactions = db.query(Interaction).all()
    return interactions
