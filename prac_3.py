def fuction(number):
	if number > 0 and number < 10:
		return number+10
	elif number > 10 and number < 100:
		return number*0.1

num = input("input number! : ")
result = fuction(num)
print result
