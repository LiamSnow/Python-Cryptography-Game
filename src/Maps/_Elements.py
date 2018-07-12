import Player as player
from Math import Curve as curve
from Math import Collision as collis
from Other import Cursors as cursors

# Map Elements

class door():
	def __init__(self, x1, y1, x2, y2, callback, _3d=False):
		self.x1, self.y1, self.x2, self.y2 = x1 / 100, y1 / 100, x2 / 100, y2 / 100
		self.lineCollision = True
		self.closed = False
		self.callback = callback
		self._3d = _3d

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	# Drawing
	def update(self, pg, win, ww, wh):
		if not self.closed:
			if self._3d:
				yOff = 0.09
				xOff = 0.04
				lineWidth = 4
				for i in range(0, 2):
					pg.draw.aalines(win, [0, 0, 0], True, [
						[self.x1 * ww, self.y1 * wh], [self.x2 * ww, self.y2 * wh],
						[self.x1 * ww, self.y1 * wh], [(self.x1 + xOff) * ww, (self.y1 - yOff) * wh],
						[(self.x1 + xOff) * ww, (self.y1 - yOff) * wh], [(self.x2 + xOff) * ww, (self.y2 - yOff) * wh],
						[(self.x2 + xOff) * ww, (self.y2 - yOff) * wh], [self.x2 * ww, self.y2 * wh]
					], 2)
			else:
				pg.draw.line(win, [0, 0, 0], [self.x1 * ww, self.y1 * wh], [self.x2 * ww, self.y2 * wh], lineWidth)
		
		if (collis.rectOverlapLine(player.getCollisionBox(), [self.x1 * 100, self.y1 * 100, self.x2 * 100, self.y2 * 100])):
			self.callback()

		return

	def close(self):
		self.closed = True
		self.lineCollision = False

	def open(self):
		self.closed = False
		self.lineCollision = True

class wall():
	def __init__(self, x1, y1, x2, y2, _3d=False):
		self.x1, self.y1, self.x2, self.y2 = x1 / 100, y1 / 100, x2 / 100, y2 / 100
		self.lineCollision = True
		self._3d = _3d

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	# Drawing
	def update(self, pg, win, ww, wh):
		if self._3d:
			yOff = 0.09
			xOff = 0.04
			pg.draw.polygon(win, [230, 230, 230], [
				[self.x1 * ww, self.y1 * wh], [self.x2 * ww, self.y2 * wh],
				[self.x1 * ww, self.y1 * wh], [(self.x1 + xOff) * ww, (self.y1 - yOff) * wh],
				[(self.x1 + xOff) * ww, (self.y1 - yOff) * wh], [(self.x2 + xOff) * ww, (self.y2 - yOff) * wh],
				[(self.x2 + xOff) * ww, (self.y2 - yOff) * wh], [self.x2 * ww, self.y2 * wh]
			], 0)
			pg.draw.aalines(win, [0, 0, 0], True, [
				[self.x1 * ww, self.y1 * wh], [self.x2 * ww, self.y2 * wh],
				[self.x1 * ww, self.y1 * wh], [(self.x1 + xOff) * ww, (self.y1 - yOff) * wh],
				[(self.x1 + xOff) * ww, (self.y1 - yOff) * wh], [(self.x2 + xOff) * ww, (self.y2 - yOff) * wh],
				[(self.x2 + xOff) * ww, (self.y2 - yOff) * wh], [self.x2 * ww, self.y2 * wh]
			], 2)
		else:
			# Bottom
			pg.draw.aaline(win, [0, 0, 0], [self.x1 * ww, self.y1 * wh], [self.x2 * ww, self.y2 * wh], 2)
		
		return

class rect():
	def __init__(self, x1, y1, x2, y2, _3d=False, _3dHeight=5):
		self.x1, self.y1, self.x2, self.y2 = x1 / 100, y1 / 100, x2 / 100, y2 / 100
		self._3d = _3d
		self._3dH = _3dHeight / 100

	# Interaction
	def processInput(self, evt, pg, win, ww, wh):
		return

	# Drawing
	def update(self, pg, win, ww, wh):
		if (self._3d):
			yOff = self._3dH
			xOff = -self._3dH / 2.5
			pg.draw.polygon(win, [230, 230, 230], [
				[(self.x2) * ww, (self.y1) * wh],
				[(self.x2) * ww, (self.y2) * wh],
				[(self.x2 + xOff) * ww, (self.y2 + yOff) * wh],
				[(self.x1 + xOff) * ww, (self.y2 + yOff) * wh],
				[(self.x1 + xOff) * ww, (self.y1 + yOff) * wh],
				[(self.x1) * ww, (self.y1) * wh]
			], 0)
			pg.draw.aalines(win, [230, 230, 230], True, [
				[(self.x2) * ww, (self.y1) * wh],
				[(self.x2) * ww, (self.y2) * wh],
				[(self.x2 + xOff) * ww, (self.y2 + yOff) * wh],
				[(self.x1 + xOff) * ww, (self.y2 + yOff) * wh],
				[(self.x1 + xOff) * ww, (self.y1 + yOff) * wh],
				[(self.x1) * ww, (self.y1) * wh]
			], 2)
			pg.draw.aalines(win, [0, 0, 0], False, [
				[(self.x1) * ww, (self.y1) * wh],
				[(self.x1) * ww, (self.y2) * wh],
				[(self.x1 + xOff) * ww, (self.y2 + yOff) * wh],
				[(self.x1) * ww, (self.y2) * wh],
				[(self.x2) * ww, (self.y2) * wh]
			], 2)
		else:
			pg.draw.aalines(win, [0, 0, 0], True, [
				[(self.x1) * ww, (self.y1) * wh],
				[(self.x2) * ww, (self.y1) * wh],
				[(self.x2) * ww, (self.y2) * wh],
				[(self.x1) * ww, (self.y2) * wh]
			], 2)

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
		], 1)
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
		], 1)

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