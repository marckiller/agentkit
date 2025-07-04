class BaseAgent:

    def __init__(self, api_url: str, api_key: str, client):

        self.api_url
        self.api_token

    def fetch(self) -> dict:
        raise NotImplementedError("You must implement the fetch() method.")
    
    def send(self, data: dict) -> dict:
        self.client.post("/agent/readings", json={"data": data})

    def run(self):
        data = self.fetch()
        self.send(data)