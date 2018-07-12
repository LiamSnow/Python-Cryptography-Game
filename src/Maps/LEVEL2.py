from Maps import _Elements as elements
import Player as player
from Math import Collision as collis
import Map as map

# LEVEL1


# Main Loop
doorOpen = False
def update():
	global doorOpen

	if not doorOpen and collis.rectanglesOverlap(player.getCollisionBox(), [15, 15, 25, 25]):
		doorOpen = True
		map.mapObjects[0].close()

	return

def DoorEnter():
	print("Door Entered")
	map.setMap("LEVEL3")


# Data
data = [
	elements.door(90, 37, 90, 53, DoorEnter),
	elements.wall(10, 10, 90, 10),
	elements.wall(10, 10, 10, 90),
	elements.wall(10, 90, 90, 90),
	elements.wall(90, 10, 90, 37),
	elements.wall(90, 53, 90, 90),
	elements.rect(15, 15, 25, 25)
]