'''
experiment with if statements and a function using a simple traffic light scenario

Author: Landon Harrison
Version: 01/10/2025
'''

def stop_light(lightColor):
    if(lightColor == "red"):
        return "stop."

    elif(lightColor == "yellow"):
        return "slow down."

    elif(lightColor == "green"):
        return "go."

    else:
        return "???"
    

color = "red"

print(f"\ndriver approaches the {color} light and must {stop_light(color)}\n")

color = "green"

print(f"driver approaches the next light, and {color} means {stop_light(color)}\n")

color = "yellow"

print(f"driver approaches a {color} light, and starts to {stop_light(color)}\n")

color = "blue"

print(f"\'wait a {color} light? {stop_light(color)}\'\n")