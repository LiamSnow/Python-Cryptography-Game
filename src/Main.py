import pygame as pg
import random
import time

# Import Files
import Player as player
import Map as map
from Maps import _HUD as HUD

# Main.py

def create_window(width, height):
	win = pg.display.set_mode((width, height), pg.RESIZABLE)

	win.fill((255, 255, 255))

	pg.display.set_caption("Program")
	pg.display.set_icon(pg.image.load("icon.png"))

	pg.display.flip()
	map.docWH(width, height, win)
	return win

width, height = 1000, 600
def main():
	pg.init()

	global win, player, width, height

	win = create_window(width, height)

	running = True
	while running:
		start = time.time()
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
			if event.type == pg.VIDEORESIZE:
				width, height = event.size
				win = create_window(width, height)
			# Send Input To Classes
			for i in map.mapObjects:
				i.processInput(event, pg, win, width, height)

		win.fill([255, 255, 255])

		# Update Classes
		for i in map.mapObjects:
			i.update(pg, win, width, height)

		map.updateMap()

		if (map.getMap() != "MENU"):
			player.update(pg, win, width, height)
			HUD.update(pg, win, width, height)


		pg.display.update()
		time.sleep(max(1.0/60 - (time.time() - start), 0))

if __name__=="__main__":
	main()