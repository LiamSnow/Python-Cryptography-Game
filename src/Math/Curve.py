
# Curve.py

def curve(perc):
	t = perc
	x_0 = 0
	y_0 = 0
	x_1 = .4
	y_1 = 0
	x_2 = .2
	y_2 = 1
	x_3 = 1
	y_3 = 1
	return ((1-t) * ((1-t) * ((1-t) * x_0 + t * x_1) + t * ((1-t) * x_1 + t * x_2)) + t * ((1-t) * ((1-t) * x_1 + t * x_2) + t * ((1-t) * x_2 + t * x_3)))

