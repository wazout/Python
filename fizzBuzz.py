count = 0
while (count < 1000000):
	count += 1
	if(count % 3 == 0) and (count %5 == 0):
		print("%s - FIZZBUZZ!!" % count)
		
	elif(count % 3 == 0):
		print("%s - FIZZ!!" % count)
		
	elif(count % 5 == 0):
		print("%s - BUZZ!!" % count)
		
	else:
		print(count)