from classes import Player
from classes import Drink
from classes import Ingredient
from mechanics import makeDrink
from mechanics import openVentil
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
players = [Player("Tom", 3), Player("Lasse", 3), Player("Jan", 3), Player("Jonas", 3)]
print("Es spielen mit:")
for player in players:
    print(player.name)
running = True

GPIO.setup(20, GPIO.OUT)
print("An")
GPIO.output(20, GPIO.HIGH)
time.sleep(3)
print("Aus")
GPIO.output(20, GPIO.LOW)
print("Fertig")
GPIO.cleanup()
