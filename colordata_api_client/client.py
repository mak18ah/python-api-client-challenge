import requests
import json
from pydantic import BaseModel, Field

class ColorDataAPIClient(BaseModel):
    host: str = "127.0.0.1"
    port = 5000
    use_ssl: bool = False
    base_path = Field('/colordata/api/', const=True)
    version = Field('v1.0', const=True)
    
    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as error:
            return "{ 'code' : {}, 'error' : {}}".format(
                error.response.status_code, error.response.reason)

    @property
    def base_url(self):
        protocol = 'https' if self.use_ssl else 'http'
        return "{}://{}:{}{}{}".format(protocol, 
        self.host, self.port, self.base_path, self.version)

    @property
    def version_url(self):
        return "{}/version".format(self.base_url)

    @property
    def count_url(self):
        return "{}/count/".format(self.base_url)

