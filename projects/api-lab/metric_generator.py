import random
import time
import requests

API_URL = "http://localhost:8000/metrics"

sources = [
    "cpu",
    "memory",
    "disk",
    "network"
]

while True:

    source = random.choice(sources)

    value = round(random.uniform(10, 95), 2)

    payload = {
        "source": source,
        "metric_value": value
    }

    response = requests.post(API_URL, json=payload)

    print(payload, response.status_code)

    time.sleep(5)