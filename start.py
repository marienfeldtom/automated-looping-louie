from classes import Player
from classes import Drink
from classes import Ingredient
from mechanics import makeDrink
from mechanics import openVentil

players = [Player("Tom", 3), Player("Lasse", 3), Player("Jan", 3), Player("Jonas", 3)]
print("Es spielen mit:")
for player in players:
    print(player.name)
running = True
while(running):
    print("LÄUFT")
