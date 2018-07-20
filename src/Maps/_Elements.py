import Player as player
from Math import Curve as curve
from Math import Collision as collis
from Other import Cursors as cursors
import Map as map
import pygame as pg
from Maps import _HUD as HUD

# Map Elements

class ground:
	def __init__(self, x1, y1, x2, y2):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.boxPhysics = True

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	# Drawing
	def update(self, pg, win, ww, wh):
		pg.draw.polygon(win, [0, 0, 0], [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 0)
		pg.draw.polygon(win, [0, 0, 0], [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 5)
		return

class door:
	def __init__(self, x1, y1, x2, y2, levelName, locked=True):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.ln = levelName
		self.locked = locked

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		def getKeyPress(key):
			return (pg.key.get_pressed()[ord(key)])

		if (getKeyPress('e') and not self.locked and (collis.simpleRectDistance(player.getCollisionBox(), [self.x1, self.y1, self.x2, self.y2]) < 80)):
			map.setMap(self.ln)

		return

	def setLocked(self, locked=True):
		self.locked = locked
	def lock(self):
		self.locked = True
	def unlock(self):
		self.locked = False

	# Drawing
	def update(self, pg, win, ww, wh):
		pg.draw.polygon(win, [230, 230, 230], [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 0)

		if (self.locked):
			pg.draw.lines(win, [255, 0, 0], False, [
				map.worldCordToScreen([self.x1, self.y1]),
				map.worldCordToScreen([self.x2, self.y2])
			], 5)
			pg.draw.lines(win, [255, 0, 0], False, [
				map.worldCordToScreen([self.x2, self.y1]),
				map.worldCordToScreen([self.x1, self.y2])
			], 5)

		pg.draw.lines(win, [0, 0, 0], True, [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 5)
		pg.draw.circle(
			win, 
			[0, 0, 0], 
			[int(map.worldXToScreen(self.x1 + ((self.x2 - self.x1) / 5))), int(map.worldYToScreen((self.y1 + self.y2) / 2))], 
			int(map.worldUnitToScreen(10)), 
			0
		)

		if (collis.simpleRectDistance(player.getCollisionBox(), [self.x1, self.y1, self.x2, self.y2]) < 80):
			HUD.setMessage("This Door is Locked" if self.locked else "Press E To Enter")

		return

class wall:
	def __init__(self, x1, y1, x2, y2):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.boxPhysics = True

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	# Drawing
	def update(self, pg, win, ww, wh):
		pg.draw.polygon(win, [0, 0, 0], [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 0)
		pg.draw.polygon(win, [0, 0, 0], [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 5)
		return

class platform:
	def __init__(self, x1, y1, x2, y2, hidden=False):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.boxPhysics = not hidden
		self.hidden = hidden

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	def setHidden(hid):
		self.hidden = hid
		self.boxPhysics = not hid
	def hide(self):
		self.hidden = True 
		self.boxPhysics = False
	def unhide(self):   
		self.hidden = False
		self.boxPhysics = True

	# Drawing
	def update(self, pg, win, ww, wh):
		if not self.hidden:
			pg.draw.polygon(win, [0, 0, 0], [
				map.worldCordToScreen([self.x1, self.y1]),
				map.worldCordToScreen([self.x2, self.y1]),
				map.worldCordToScreen([self.x2, self.y2]),
				map.worldCordToScreen([self.x1, self.y2])
			], 0)
			pg.draw.polygon(win, [0, 0, 0], [
				map.worldCordToScreen([self.x1, self.y1]),
				map.worldCordToScreen([self.x2, self.y1]),
				map.worldCordToScreen([self.x2, self.y2]),
				map.worldCordToScreen([self.x1, self.y2])
			], 5)
		return

class button:
	def __init__(self, x1, y1, x2, y2, text, callback):
		self.x, self.y, self.w, self.h, self.x2, self.y2 = x1 / 100, y1 / 100, (x2 - x1) / 100, (y2 - y1) / 100, x2 / 100, y2 / 100
		self.txt = text
		self.hover = False
		self.click = False
		self.callback = callback
		self.clickAnim = 1

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
			
		def posOnButton(pos):
			return (pos[0] > (self.x * ww) and pos[0] < (self.x2 * ww) and pos[1] > (self.y * wh) and pos[1] < (self.y2 * wh))

		def updateHover():
			isHover = posOnButton(evt.pos)
			if (isHover and not self.hover):
				self.hover = True
				pg.mouse.set_cursor(*cursors.pointer)
			elif (not isHover and self.hover):
				self.hover = False
				pg.mouse.set_cursor(*pg.cursors.arrow)


		if (evt.type == pg.MOUSEMOTION):
			updateHover()

		if (evt.type == pg.MOUSEBUTTONUP):
			updateHover()
			self.click = False
			self.clickAnim = 0
			if posOnButton(evt.pos):
				self.callback()

		if (evt.type == pg.MOUSEBUTTONDOWN):
			updateHover()
			if posOnButton(evt.pos):
				self.click = True
				self.clickAnim = 1

		return

	# Drawing
	def update(self, pg, win, ww, wh):
		buttonOff = (self.w * 0.05 * wh)
		buttonColor = [100, 100, 100] if self.hover else [0, 0, 0]
		# Lower (Bottom Right)
		pg.draw.rect(win, buttonColor, [
			self.x * ww + (buttonOff * curve.curve(self.clickAnim)),
			self.y * wh + (buttonOff * curve.curve(self.clickAnim)), 
			self.w * ww - (buttonOff), 
			self.h * wh - (buttonOff)
		], 5)
		# Higher (Top Left)
		pg.draw.rect(win, [255, 255, 255], [
			self.x * ww, 
			self.y * wh, 
			self.w * ww - (buttonOff), 
			self.h * wh - (buttonOff)
		], 0)
		pg.draw.rect(win, buttonColor, [
			self.x * ww, 
			self.y * wh, 
			self.w * ww - (buttonOff), 
			self.h * wh - (buttonOff)
		], 5)

		# Text
		TextSurf = pg.font.Font('Fonts/Roboto-Regular.ttf', int((self.w * ww * 0.02 if (self.w * ww < self.h * wh) else self.h * wh * 0.03) * len(self.txt))).render(self.txt, True, [0, 0, 0])
		TextRect = TextSurf.get_rect()
		TextRect.center = ((self.x + (self.w / 2)) * ww - (buttonOff / 2), (self.y + (self.h / 2)) * wh - (buttonOff / 2))
		win.blit(TextSurf, TextRect)

		# Anim

		if (self.click and self.clickAnim > 0):
			self.clickAnim -= 0.05
		elif (not self.click and self.clickAnim < 1):
			self.clickAnim += 0.03

		return

class backdropwall:
	def __init__(self, x1, y1, x2, y2):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	# Drawing
	def update(self, pg, win, ww, wh):
		pg.draw.polygon(win, [230, 230, 230], [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 0)
		pg.draw.polygon(win, [220, 220, 220], [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 5)
		return

class text:
	def __init__(self, text, size, color, x, y, hidden=False):
		self.x, self.y = x, y
		self.size = size
		self.text = text
		self.color = color
		self.hidden = hidden

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	def setText(self, text):
		self.text = text

	def setHidden(self, hidden):
		self.hidden = hidden
	def hide(self):
		self.hidden = True
	def unhide(self):
		self.hidden = False

	# Drawing
	def update(self, pg, win, ww, wh):
		if not self.hidden:
			textSize = int(map.worldUnitToScreen(self.size))
			TextSurf = pg.font.Font('Fonts/Roboto-Regular.ttf', textSize).render(self.text, True, self.color)
			TextRect = TextSurf.get_rect()
			TextRect.center = (
				int(map.worldXToScreen(self.x)), 
				int(map.worldYToScreen(self.y))
			)
			win.blit(TextSurf, TextRect)
		return

class textField:
	def __init__(self, placeholder, x1, y1, x2, y2, oninputCallback):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.placeholder = placeholder
		self.callback = oninputCallback
		self.value = ""
		self.active = False
		self.hover = False

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):

		def posOnButton(pos):
			def nir(a, x, y):
				if (x <= y):
					return a >= x and a <= y
				else:
					return a >= y and a <= x
			
			return (
				nir(pos[0], (map.worldXToScreen(self.x1)), (map.worldXToScreen(self.x2))) and
				nir(pos[1], (map.worldYToScreen(self.y1)), (map.worldYToScreen(self.y2)))
			)

		def updateHover():
			isHover = posOnButton(evt.pos)
			if (isHover and not self.hover):
				self.hover = True
				pg.mouse.set_cursor(*cursors.textmarker)
			elif (not isHover and self.hover):
				self.hover = False
				pg.mouse.set_cursor(*pg.cursors.arrow)

		if (evt.type == pg.KEYDOWN and self.active):
			key = evt.key
			if (key >= 32 and key <= 126):
				if ((evt.mod == 1 or evt.mod == 2) and (key >= 97 and key <= 122)):
					key -= 32
				self.value += chr(key)
				self.callback(self.value)
			elif (key == 127 or key == 8):
				self.value = self.value[:-1]
				self.callback(self.value)
			elif (key == 27 or key == 13):
				self.active = False
				player.inUi = False

		if (evt.type == pg.MOUSEMOTION):
			updateHover()

		if (evt.type == pg.MOUSEBUTTONUP):
			updateHover()
			if posOnButton(evt.pos):
				self.active = True
				player.inUi = True
			else:
				self.active = False
				player.inUi = False

		return

	def setActive(self, active):
		self.active = active
		player.inUi = active

	# Drawing
	def update(self, pg, win, ww, wh):
		# Text
		text = (self.value + ("|" if self.active else "")) if (self.value != "" or self.active) else self.placeholder
		color = [0, 0, 0] if (self.value != "" or self.active) else [100, 100, 100]
		textSize = map.worldUnitToScreen((self.x2 - self.x1) * 0.07)
		TextSurf = pg.font.Font('Fonts/Roboto-Regular.ttf', int(textSize)).render(text, True, color)
		TextRect = TextSurf.get_rect()
		TextRect.center = (
			int(map.worldXToScreen((self.x2 + self.x1) / 2)), 
			int(map.worldYToScreen((self.y2 + self.y1) / 2))
		)
		win.blit(TextSurf, TextRect)

		# Outline
		pg.draw.lines(win, [0, 0, 0], True, [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 3)
		return

class physButton:
	def __init__(self, x1, y1, x2, y2, clickedCallback, unclickedCallback):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.ccb = clickedCallback
		self.ucb = unclickedCallback
		self.clicked = False

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	# Drawing
	def update(self, pg, win, ww, wh):
		if collis.rectanglesOverlap([self.x1, self.y1, self.x2, self.y2], player.getCollisionBox()):
			if (not self.clicked):
				self.clicked = True
				self.ccb()
		elif (self.clicked):
			self.clicked = False
			self.ucb()

		y1 = self.y2 + ((self.y1 - self.y2) / 10) if self.clicked else self.y1 

		pg.draw.polygon(win, [255, 20, 20], [
			map.worldCordToScreen([self.x1, y1]),
			map.worldCordToScreen([self.x2, y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 0)

		pg.draw.lines(win, [255, 20, 20], True, [
			map.worldCordToScreen([self.x1, y1]),
			map.worldCordToScreen([self.x2, y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 5)

		return

class backdropbutton:
	def __init__(self, x1, y1, x2, y2, text, callback):
		self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
		self.txt = text
		self.hover = False
		self.click = False
		self.callback = callback

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
			
		def posOnButton(pos):
			def nir(a, x, y):
				if (x <= y):
					return a >= x and a <= y
				else:
					return a >= y and a <= x
			
			return (
				nir(pos[0], (map.worldXToScreen(self.x1)), (map.worldXToScreen(self.x2))) and
				nir(pos[1], (map.worldYToScreen(self.y1)), (map.worldYToScreen(self.y2)))
			)

		def updateHover():
			isHover = posOnButton(evt.pos)
			if (isHover and not self.hover):
				self.hover = True
				pg.mouse.set_cursor(*cursors.pointer)
			elif (not isHover and self.hover):
				self.hover = False
				pg.mouse.set_cursor(*pg.cursors.arrow)


		if (evt.type == pg.MOUSEMOTION):
			updateHover()

		if (evt.type == pg.MOUSEBUTTONUP):
			updateHover()
			self.click = False
			if posOnButton(evt.pos):
				self.callback()

		if (evt.type == pg.MOUSEBUTTONDOWN):
			updateHover()
			if posOnButton(evt.pos):
				self.click = True

		return

	# Drawing
	def update(self, pg, win, ww, wh):
		bColor = ([50, 50, 50] if self.hover else [0, 0, 0])
		pg.draw.polygon(win, bColor, [
			map.worldCordToScreen([self.x1, self.y1]),
			map.worldCordToScreen([self.x2, self.y1]),
			map.worldCordToScreen([self.x2, self.y2]),
			map.worldCordToScreen([self.x1, self.y2])
		], 5)

		# Text
		TextSurf = pg.font.Font('Fonts/Roboto-Regular.ttf', 
			int((self.x2 - self.x1) * 0.8 * len(self.txt))
		).render(self.txt, True, bColor)
		TextRect = TextSurf.get_rect()
		TextRect.center = (
			(map.worldXToScreen(self.x2) + map.worldXToScreen(self.x1)) / 2, 
			(map.worldYToScreen(self.y2) + map.worldYToScreen(self.y1)) / 2
		)
		win.blit(TextSurf, TextRect)

		return