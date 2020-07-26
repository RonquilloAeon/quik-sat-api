from fastapi import FastAPI

from api.config import Config
from api.satellite import views as satellite_views
from api.satellite.data import get_satellites

app = FastAPI()
app.include_router(satellite_views.router, prefix="/satellites")
config = Config()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.on_event("startup")
async def load_satellite_data():
    await get_satellites(config.SATELLITE_REPOSITORY_URL)
