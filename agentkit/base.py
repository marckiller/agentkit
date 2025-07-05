class BaseAgent:
    def __init__(self, api_url: str, api_key: str, client):
        self.api_url = api_url
        self.api_token = api_key
        self.client = client

    def fetch(self) -> dict:
        raise NotImplementedError("You must implement the fetch() method.")
    
    def send(self, data: dict) -> dict:
        return self.client.post("/agent/readings", json={"data": data})

    def run(self):
        data = self.fetch()
        return self.send(data)