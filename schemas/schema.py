from pydantic import BaseModel
from datetime import date

class SitesSchema(BaseModel):
    title: str
    url: str
    xpath: str

class ProductShema(BaseModel):
    sites_id: str
    price: str
    dt_create: date