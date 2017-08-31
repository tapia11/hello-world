i = 0
numbers = []

while i < 6:
	print "At the top i is %d" % i
	numbers.append(i)
		
	i = i + 1
	print "Numbers now: ", numbers
	print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
	print num
	
def the_while(numero1, numero2, numero3):
	for num in range(numero1, numero2, numero3):
	# while numero1 < numero2:
		print "At the top i is %d" % numero1
		numbers.append(numero1)
			
		numero1 = numero1 + numero3
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % numero1


	print "The numbers: "

	for num in numbers:
		print num

startNum = int(raw_input("start number > "))
endNum = int(raw_input("end number > "))
incNum = int(raw_input("increment number > "))
the_while(startNum, endNum, incNum)