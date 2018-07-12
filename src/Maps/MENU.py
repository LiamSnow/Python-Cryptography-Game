from Maps import _Elements as elements
import Map as map

# MENU

def StartGame():
	map.setMap("LEVEL1")

data = [
	elements.button(40, 45, 60, 55, "Start Game", StartGame)
]

def update():
	return