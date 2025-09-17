import requests
import json

def request(action, **params):
    return requests.post("http://localhost:8765", json={
        "action": action,
        "version": 6,
        "params": params
    }).json()


result = request("findNotes", query="deck:English")
notes = request("notesInfo", notes=result['result'])
with open("My_deck_english.json", "w", encoding="utf-8") as f:
    json.dump(notes['result'], f, ensure_ascii=False, indent=2)
