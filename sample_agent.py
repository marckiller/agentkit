from agentkit.client import ApiClient
import time
import random
from datetime import datetime

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
        # attach a timestamp indicating when the data was collected
        response = client.post_reading(data, timestamp=datetime.utcnow())
        print("Data sent successfully:", response)
        # adjust the sleep interval as needed (in seconds)
        time.sleep(3600)