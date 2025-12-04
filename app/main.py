from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

from .get_consumption_volume_endpoint import get_consumption_volume
from .startup.load_models import load_consumption_model

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.state.consumption_model = load_consumption_model()
app.include_router(get_consumption_volume.router)