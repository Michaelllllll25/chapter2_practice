import random

player = {
    "name": "Awesome-Sauce",
    "health": 50,
    "strength": 20
}

while player["healh"] > 0:
    if player["health"] < 0:
        break
    damage_taken = random.randrange(10, 25)
    print(f"Enemy hits {player['name']} for {damage_taken} damage.")
    # subtract the player's health by the damage_taken variable
    player["stregth"] -= 5
    damage_taken -= 5
    player["health"] -= damage_taken
    print()
    print(f"Player: {player['name']}")
    print(f"Health: {player['health']}")
    print()

print("Game Over!")
