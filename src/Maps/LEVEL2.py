from Maps import _Elements as elements
import Player as player
from Math import Collision as collis
import Map as map
from Crypt import ces

# LEVEL1


# Main Loop
cipherText = "Estd td l Nlpdlc Ntaspc"
def update():
	return


def up():
	global cipherText
	cipherText = ces.encrypt(cipherText, 1)
	data[1].setText(cipherText)

	if (ces.encrypt(cipherText, 10) == "Drsc sc k Mkockb Mszrob"):
		map.mapObjects[4].unhide()
	else:
		map.mapObjects[4].hide()

	return

def down():
	global cipherText
	cipherText = ces.encrypt(cipherText, -1)
	data[1].setText(cipherText)

	if (ces.encrypt(cipherText, 10) == "Drsc sc k Mkockb Mszrob"):
		map.mapObjects[4].unhide()
	else:
		map.mapObjects[4].hide()

	return


# Data
data = [
	# Mech
	elements.backdropwall(300, 300, 900, 40),
	elements.text(cipherText, 35, [0, 0, 0], 600, 250),
	elements.backdropbutton(520, 140, 560, 180, "<", up),
	elements.backdropbutton(640, 140, 680, 180, ">", down),
	elements.platform(1000, 250, 1200, 250 - 30, True),

	# Floor
	elements.ground(-200, 0, 1800, 30),

	# Walls
	elements.wall(-200, 30, -170, 500),
	elements.wall(1800, 30, 1770, 500),

	# Door
	elements.door(1250, 560, 1250 + 100, 560 - 140, "LEVEL3", False),
	elements.platform(1200, 420, 1400, 420 - 30)
]