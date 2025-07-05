from agentkit.client import ApiClient
import time
import random

# Define your custom data-fetching logic here
# This function should return a dictionary representing the data payload
def fake_fetch():
    return {"value": random.randint(0, 100)}

if __name__ == "__main__":
    # Initialize the API client with the backend URL and agent name
    client = ApiClient(base_url="http://localhost:8000", name="demo-agent")

    # Start the main loop to fetch and post data every 3600 seconds
    while True:
        data = fake_fetch()
        response = client.post_reading(data)
        print("Data sent successfully:", response)
        time.sleep(3600)