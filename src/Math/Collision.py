import math

# Collision.py

def rectanglesOverlap(r1, r2):
	return (
		r1[0] < r2[2] and
		r1[2] > r2[0] and
		r1[1] < r2[3] and
		r1[3] > r2[1]
	)


def linesOverlap(x1, y1, x2, y2, x3, y3, x4, y4):
	try:
		uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
		uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
		if (uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1):
			return True
		return False
	except ZeroDivisionError:
		return False

def rectOverlapLine(r1, l1):
	lines = [[r1[0], r1[1], r1[2], r1[1]], [r1[2], r1[1], r1[2], r1[3]], [r1[2], r1[3], r1[0], r1[3]], [r1[0], r1[3], r1[0], r1[1]]]
	overlap = False
	for i in lines:
		if (linesOverlap(i[0], i[1], i[2], i[3], l1[0], l1[1], l1[2], l1[3])):
			overlap = True
	return overlap

# Returns [directionChar, distance_in_world_units]
def rectDistance(r1, r2):
	dir = rectangleDir(r1, r2)
	if (dir != None):
		def avg(a, b):
			return (a + b) / 2

		def pickClosest(a1, b1, a2, b2):
			t = [[a1, a2], [b1, a2], [a1, b2], [b1, b2]]

			l = float("inf")
			li = None
			for i in t:
				if (abs(i[0] - i[1]) < l):
					l = abs(i[0] - i[1])
					li = i
			return li
		
		points = None
		if (dir == "N" or dir == "S"):
			# X
			xp = avg(r1[0], r1[2]) if ((r1[2] - r1[0]) < (r2[2] - r2[0])) else avg(r2[0], r2[2])
			
			# Y
			c = pickClosest(r1[1], r1[3], r2[1], r2[3])

			# Points [Player, Box]
			points = [[xp, c[0]], [xp, c[1]]]
		else:
			# Y
			yp = avg(r1[1], r1[3]) if ((r1[3] - r1[1]) < (r2[3] - r2[1])) else avg(r2[1], r2[3])
			
			# X
			c = pickClosest(r1[0], r1[2], r2[0], r2[2])

			# Points [Player, Box]
			points = [[c[0], yp], [c[1], yp]]
		
		dst = math.hypot(points[0][0] - points[1][0], points[0][1] - points[1][1])

		return [dir, dst]
	return [None, None]

def rectangleDir(r1, r2):
	def numberOverlap(x1, x2, y1, y2):
		return max(x1, y1) <= min(x2,y2)

	def avg(a, b):
		return (a + b) / 2

	if (numberOverlap(r1[0], r1[2], r2[0], r2[2])):
		if (avg(r1[1], r1[3]) > avg(r2[1], r2[3])):
			return 'S'
		else:
			return 'N'

	elif (numberOverlap(r1[1], r1[3], r2[1], r2[3])):
		if (avg(r1[0], r1[2]) > avg(r2[0], r2[2])):
			return 'W'
		else:
			return 'E'

	return