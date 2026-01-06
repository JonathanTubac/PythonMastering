import requests

def get_questions(params):
    response = requests.get("https://opentdb.com/api.php", params)
    response.raise_for_status()
    data = response.json()
    return data["results"]

params = {
    "amount": 10,
    "type": "boolean"
}

question_data = get_questions(params)
