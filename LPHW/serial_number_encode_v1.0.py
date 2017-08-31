from math import *

class PCBLabel(object):
	
	global char_decode
	char_decode = { '00000' : "0",
								'00001' : "1",
								'00010' : "2",
								'00011' : "3",
								'00100' : "4",
								'00101' : "5",
								'00110' : "6",
								'00111' : "7",
								'01000' : "8",
								'01001' : "9",
								'01010' : "A",
								'01011' : "B",
								'01100' : "C",
								'01101' : "D", 
								'01110' : "E",
								'01111' : "F",
								'10000' : "G",
								'10001' : "H",
								'10010' : "J",
								'10011' : "K",
								'10100' : "L",
								'10101' : "M",
								'10110' : "N",
								'10111' : "P",
								'11000' : "R",
								'11001' : "T",
								'11010' : "U",
								'11011' : "V",
								'11100' : "W",
								'11101' : "X",
								'11110' : "Y",
								'11111' : "Z" 
							}
	
	def __init__(self, sn):
		self.sn = sn
	
	def dec2bin(self):
		binNum = bin(int(self.sn))[2:]
		return binNum
	
	def make20bit(self, bin):
		count = 0
		for num in bin:
			count +=1
		if count != 19:
			need = 20 - count
			newBin = ("0" * need) + bin
		return newBin
	
	def splitBits(self, newBin):
		char1 = newBin[:5]
		char2 = newBin[5:10]
		char3 = newBin[10:15]
		char4 = newBin[15:20]
		return char_decode[char1] + char_decode[char2] + char_decode[char3] + char_decode[char4] + "7" + "E" + "X" + "0" 

print "To quit, use CTRL+C"
while True:
	try:
		newLabel = raw_input("Enter EI9001T Card S/N > ")
		newSN = PCBLabel(newLabel)
		getBin = newSN.dec2bin()
		bit20 = newSN.make20bit(getBin)
		splitValues = newSN.splitBits(bit20)
		print "The PCB Label value for card S/N ", newLabel, " is ", splitValues
	except ValueError:
		print "Error. Invalid input"


''' 
=====================================================
modulo stuff that wasn't necessary
=====================================================

# a = (22646340512 - (22646340512 % 1048576))/1048576
# c = 262144

# for val in range(0, c-1):
	# if a * val % c == 1:
		# B = val
		# print B
		# break
	# else:
		# B = 0
		
# if B == 0:
	# print "nope"
	

# modo =  ((22646340512 - (22646340512 % 1048576))/1048576) % 262144
# print modo

# test = (22646340512 - (22646340512 % 1048576))
# print test, "and test div 1048576:", test/1048576

# print 22*32*(13+32*(3))


# sn = 21597
# sum = 10000000
# while True:
	# try:
		# if ((sum - (sum % 1048576))/1048576) % 262144 == sn:
			# print sum
			# break
		# else:
			# sum += 1
	# except ValueError:
		# print "no go"
'''