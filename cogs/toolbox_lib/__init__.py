import os
import requests

NOMICS_KEY = os.environ.get("NOMICS_KEY")

NOMICS_BASE_URL = "https://api.nomics.com/v1/"
NOMICS_EXCH_RT_URL = f"{NOMICS_BASE_URL}exchange-rates?key={NOMICS_KEY}&formats=json"

print(NOMICS_EXCH_RT_URL)

def fetch_exchange(currency="usd"):
    res = requests.get(NOMICS_EXCH_RT_URL)
    data = res.json()

    return data
