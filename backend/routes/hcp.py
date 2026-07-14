from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.models.hcp import HCP
from app.schemas.hcp import HCPCreate, HCPResponse

router = APIRouter()

# Database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create HCP
@router.post("/", response_model=HCPResponse)
def create_hcp(hcp: HCPCreate, db: Session = Depends(get_db)):
    new_hcp = HCP(
        name=hcp.name,
        specialization=hcp.specialization,
        hospital=hcp.hospital,
        city=hcp.city
    )

    db.add(new_hcp)
    db.commit()
    db.refresh(new_hcp)

    return new_hcp

# Get all HCPs
@router.get("/", response_model=list[HCPResponse])
def get_hcps(db: Session = Depends(get_db)):
    return db.query(HCP).all()
