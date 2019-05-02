
def makeDrink(player, drink):
    print (player.name + " bekommt einen " + drink.name)
    for ingredient in drink.ingredients:
        openVentil(ingredient.ventil, ingredient.time)
    print ("Getränk wurde erfolgreich eingefuellt")


def openVentil(ventil, time):
    print("Ventil " + ventil + " wird für " + time + "Sekunden geoeffnet")
