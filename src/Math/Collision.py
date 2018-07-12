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