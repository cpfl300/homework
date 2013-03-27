def abs_val(number):
	if number == 0 or number > 0:
		return number
	else :
		return -number

num = input ("input number! : ")
result = abs_val(num)
print result
