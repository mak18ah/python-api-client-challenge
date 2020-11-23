from .client import ColorDataAPIClient
from pydantic import BaseModel

CLIENT = ColorDataAPIClient()

class ColorDataResponsePayload(BaseModel):
    count: int

class APIVersionResponsePayload(BaseModel):
    version: int

def query_color_count(color):
    payload = ColorDataAPIClient.get(CLIENT.count_url + color)         
    return ColorDataResponsePayload(count=payload["count"])

def query_api_version():        
    payload = ColorDataAPIClient.get(CLIENT.version_url)         
    return APIVersionResponsePayload(version=payload["version"])
