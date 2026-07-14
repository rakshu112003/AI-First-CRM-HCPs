from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.database import Base, engine
from app.models import hcp, interaction
from app.routes import hcp as hcp_routes
from app.routes import interaction as interaction_routes


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="AI-First CRM for HCPs"
)


# Enable React Frontend Connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Include Routes
app.include_router(
    hcp_routes.router,
    prefix="/hcps",
    tags=["HCP"]
)

app.include_router(
    interaction_routes.router,
    prefix="/interactions",
    tags=["Interaction"]
)


@app.get("/")
def root():
    return {
        "message": "HCP CRM Backend is Running!"
    }
