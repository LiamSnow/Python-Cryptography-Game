from Maps import _Elements as elements
import Player as player
from Math import Collision as collis
import Map as map
from Crypt import vig

# LEVEL1


# Main Loop
cipherText = "Wvvl rm p Jdkvtxyi Yiaswu!"
def update():
	if (player.y < -1000):
		player.x, player.y = 0, 500
	return

def ProcessInput(val):
	global cipherText
	if (val != ""):
		map.mapObjects[1].setText(vig.decrypt(cipherText, val))

		if vig.encrypt(vig.decrypt(cipherText, val), "oof") == "Hvng ng f Jnusssfj Qndvjf!":
			map.mapObjects.append(elements.platform(0, 290, 200 + 0, 290 - 30))
			map.mapObjects[2].setActive(False)

	return

def ShowKey():
	map.mapObjects[6].unhide()
	return

def HideKey():
	map.mapObjects[6].hide()
	return


# Data
data = [
	# Mech
	elements.backdropwall(300, 300, 900, 40),
	elements.text(cipherText, 35, [0, 0, 0], 600, 250),
	elements.textField("Enter Key Here", 450, 150, 750, 150 + 30, ProcessInput),
	elements.platform(-390, 190, -370 + 200, 190 - 30),
	elements.platform(-670, 300, -670 + 200, 300 - 30),
	elements.physButton(-550, 320, -550 + 50, 320 - 20, ShowKey, HideKey),
	elements.text("Dont Jump Over The Walls", 30, [0, 0, 0], -400, 450, True),

	# Floor
	elements.ground(-700, 0, 1800, 30),

	# Walls
	elements.wall(-700, 30, -700 + 30, 500),
	elements.wall(1800, 30, 1800 - 30, 500),

	# Door
	elements.door(350, 560, 350 + 100, 560 - 140, "LEVEL4", False),
	elements.platform(300, 420, 300 + 200, 420 - 30)
]