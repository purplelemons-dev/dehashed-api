import requests as r
from base64 import b64encode as b64
from dataclasses import dataclass


@dataclass
class DataPoint:
    id: str
    email: str
    username: str
    ip_address: str
    username: str
    password: str
    hashed_password: str
    name: str
    vin: str
    address: str
    phone: str
    database_name: str


class Dehashed:
    entries: list[DataPoint] = []

    def __init__(self, email, api_key):
        self.email = email
        self.api_key = api_key
        self.s = r.Session()

    @property
    def headers(self):
        return {
            "Accept": "application/json",
            "Authorization": f"Basic {b64(f'{self.email}:{self.api_key}'.encode()).decode()}",
        }

    def from_email(self, email):
        url = f"https://api.dehashed.com/search?query=email:{email}"
        response = self.s.get(url, headers=self.headers)
        response.raise_for_status()
        json = response.json()
        self.entries = [DataPoint(**entry) for entry in json["entries"]]
        return self.entries
