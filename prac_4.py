import math

def sqrt(x1,x2,y1,y2):
	
	result_x = (x2-x1)**2
	result_y = (y2-y1)**2
	result= math.sqrt(result_x + result_y)

	return result


a1 = 4
a2 = 1
b1 = 6
b2 = 2

len = sqrt(a1, a2, b1, b2)

print len
