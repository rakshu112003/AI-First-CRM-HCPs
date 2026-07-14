from sqlalchemy import Column, Integer, String, ForeignKey
from app.database.database import Base

class Interaction(Base):
    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)
    hcp_id = Column(Integer, ForeignKey("hcps.id"))
    notes = Column(String)
    summary = Column(String)
    follow_up = Column(String)
    sentiment = Column(String)
