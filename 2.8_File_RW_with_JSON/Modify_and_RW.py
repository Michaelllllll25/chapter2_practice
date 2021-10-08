import json

data = [{
        "section": "Dictionaries",
        "name": "Person Info",
        "points": 10,
        "published": "false"
    },
    {
        "section": "Dictionaries",
        "name": "Mini Passivist RPG",
        "points": 25,
        "published": "false"
    }]


with open("exercises.json", "w") as f:
    json.dump(data, f, indent=4)              # Replaces


