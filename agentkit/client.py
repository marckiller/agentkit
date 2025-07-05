

import os
import requests

class ApiClient:
    def __init__(self, base_url: str, name: str, description: str = ""):
        self.base_url = base_url
        self.name = name
        self.description = description
        self.token_file = ".agent_token"
        self.api_token = self._load_or_register()

    def _auth_headers(self) -> dict:
        return {"api-key": self.api_token}

    def _load_or_register(self) -> str:
        if os.path.exists(self.token_file):
            with open(self.token_file, "r") as f:
                return f.read().strip()
        return self._register_and_save_token()

    def _register_and_save_token(self) -> str:
        payload = {"name": self.name, "description": self.description}
        response = requests.post(f"{self.base_url}/agent/register", json=payload)
        response.raise_for_status()
        token = response.json()["api_key"]
        with open(self.token_file, "w") as f:
            f.write(token)
        return token

    def post_reading(self, data: dict) -> dict:
        response = requests.post(f"{self.base_url}/agent/readings", json={"data": data}, headers=self._auth_headers())
        response.raise_for_status()
        return response.json()

    def ping(self) -> dict:
        response = requests.get(f"{self.base_url}/agent/ping", headers=self._auth_headers())
        response.raise_for_status()
        return response.json()