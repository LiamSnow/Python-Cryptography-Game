from Maps import _Elements as elements
import Player as player
from Math import Collision as collis
import Map as map

# LEVEL1


# Main Loop
def update():

	return

# Data
data = [
	# Floor
	elements.ground(-200, 0, 1800, 30),

	# Walls
	elements.wall(-200, 30, -170, 500),
	elements.wall(1800, 30, 1770, 500),

	# Platforms
	elements.platform(200, 200, 400, 230),
	elements.platform(600, 300, 800, 330),

	# Door
	elements.door(650, 500, 750, 330, "LEVEL2", False)
]