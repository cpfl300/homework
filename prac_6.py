def compare(text):
	reverse = text[::-1]

	i = 0
	while (i < len(text)):
		if text[i] != reverse[i]:
			return ("different")
			break
		i=i+1

sent = 'refer'

result = compare(sent)

if (result!="different"):
	print "same"

else:
	print result

