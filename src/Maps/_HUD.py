# HUD

import Map as map

mes = None
def setMessage(message):
	global mes
	mes = message

def update(pg, win, ww, wh):
	# Alert
	global mes
	if (mes != None and mes != ""):
		x1 = (ww / 2) - (ww / 10)
		x2 = (ww / 2) + (ww / 10)
		y1 = (wh / 1.2) - (wh / 30)
		y2 = (wh / 1.2) + (wh / 30)
		w = x2 - x1
		h = y2 - y1

		# Background
		#pg.draw.polygon(win, [230, 230, 230], [
		#	[x1, y1],
		#	[x2, y1],
		#	[x2, y2],
		#	[x1, y2]
		#], 0)
		pg.draw.lines(win, [0, 0, 0], True, [
			[x1, y1],
			[x2, y1],
			[x2, y2],
			[x1, y2]
		], 5)

		# Text
		textSize = int(w / 14)
		TextSurf = pg.font.Font('Fonts/Roboto-Regular.ttf', textSize).render(mes, True, [0, 0, 0])
		TextRect = TextSurf.get_rect()
		TextRect.center = (
			(x2 + x1) / 2,
			(y2 + y1) / 2
		)
		win.blit(TextSurf, TextRect)

		mes = None

	# Outline
	outline_off = 2
	pg.draw.lines(win, [0, 0, 0], True, [
		[outline_off, outline_off],
		[ww - outline_off, outline_off],
		[ww - outline_off, wh - outline_off],
		[outline_off, wh - outline_off]
	], 10)

	# Map Name
	pg.draw.polygon(win, [0, 0, 0], [
		[(ww / 2) - (ww / 10), 0],
		[(ww / 2) + (ww / 10), 0],
		[(ww / 2) + (ww / 10), (ww / 20)],
		[(ww / 2) - (ww / 10), (ww / 20)]
	], 0)
	pg.draw.polygon(win, [0, 0, 0], [
		[(ww / 2) - (ww / 10), 0],
		[(ww / 2) + (ww / 10), 0],
		[(ww / 2) + (ww / 10), (ww / 20)],
		[(ww / 2) - (ww / 10), (ww / 20)]
	], 10)

	textSize = int(ww / 25)
	TextSurf = pg.font.Font('Fonts/Roboto-Regular.ttf', textSize).render(map.getMap(), True, [255, 255, 255])
	TextRect = TextSurf.get_rect()
	TextRect.center = (
		((ww / 2) + (ww / 2)) / 2,
		(ww / 34)
	)
	win.blit(TextSurf, TextRect)