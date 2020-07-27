from fastapi import APIRouter, HTTPException

from api.models import ListResponse
from api.satellite.data import SATELLITES
from api.satellite.models import Satellite

router = APIRouter()


@router.get("", response_model=ListResponse[Satellite])
def list_satellites():
    return {"results": sorted(list(SATELLITES.values()), key=lambda s: s["name"])}


@router.get("/{satellite_name}", response_model=Satellite)
def get_satellite(satellite_name: str):
    try:
        return SATELLITES[satellite_name]
    except KeyError:
        raise HTTPException(status_code=404, detail="Satellite not found")
