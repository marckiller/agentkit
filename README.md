# agentkit

`agentkit` is a minimal and pluggable Python framework designed for building lightweight data collection agents that communicate with a central data center via a REST API.

It is built to seamlessly integrate with the [`modular-data-pipeline`](https://github.com/marckiller/modular-data-pipeline) backend, which handles data agents registration and data storage.

## Features

- Auto-registration of agents
- Token-based authentication
- Simple interface to send readings
- Heartbeat/ping functionality
- Easily extendable with your own data-fetching logic

## How to Use

### 1. Clone both repositories

```bash
git clone https://github.com/marckiller/modular-data-pipeline
git clone https://github.com/marckiller/agentkit
```

### 2. Start the backend server

In the `modular-data-pipeline` directory, run the following commands to initialize the database (only required on first run) and start the backend server:

```bash
python app/db/init_db.py     # Run once to initialize the database
uvicorn app.main:app --reload --port 8000
```

You can change the port by modifying the `--port` value.  
The backend will be available at `http://localhost:<port>`.

### 3. Implement your agent

In `agentkit/sample_agent.py`, write your custom data-fetching logic inside `fake_fetch()`:

```python
def fake_fetch():
    # Replace with your own data collection logic
    return {"value": 42}
```

You can also customize the agent's behavior, such as how often it sends data, by modifying the main loop in `sample_agent.py`. For example, adjust the `time.sleep(...)` interval to control the frequency of data transmission.


### 4. Run the agent

From the `agentkit` directory:

```bash
python sample_agent.py
```

This will:
- Register the agent (only once)
- Save the API key locally in `.agent_token`
- Periodically send data to the backend

## Authentication

Each agent is issued an API key during registration. All future requests are authenticated via a custom header:

```
api-key: your-token-here
```

## Backend Endpoints Used

- `POST /agent/register`
- `POST /agent/readings`
- `GET /agent/ping`

## Directory Structure

```
agentkit/
├── agentkit/
│   └── client.py    # The API client
├── sample_agent.py  # Main loop for fetching
└── .agent_token     # Local API key storage
```

## Requirements

- Python
- `requests` library

## Tips

- Use multiple agents with different names to simulate multiple data sources.
- You may optionally use the `BaseAgent` class from `agentkit/base.py` to structure your agents using an OOP approach. This is useful when implementing multiple agents with shared logic.
