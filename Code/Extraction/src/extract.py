import requests as r
import json



def extract_data_from_api(count: int, timestamp:str) -> dict :
    request = f'https://aoe2.net/api/matches?game=aoe2de&count={count}&since={timestamp}'
    response = r.get(request)
    return response.json()

