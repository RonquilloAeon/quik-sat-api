from pydantic import BaseModel


class Satellite(BaseModel):
    name: str
    catalog_number: str
    classification: str
