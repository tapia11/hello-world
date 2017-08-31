from math import *
import sys

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

class serialNumber(object):

	global char_encode
	char_encode = { "0" : 0,
							 "1" : 1,
							 "2" : 2,
							 "3" : 3,
							 "4" : 4,
							 "5" : 5,
							 "6" : 6,
							 "7" : 7,
							 "8" : 8,
							 "9" : 9,
							 "A" : 10,
							 "B" : 11,
							 "C" : 12,
							 "D" : 13, 
							 "E" : 14,
							 "F" : 15,
							 "G" : 16,
							 "H" : 17,
							 "J" : 18,
							 "K" : 19,
							 "L" : 20,
							 "M" : 21,
							 "N" : 22,
							 "P" : 23,
							 "R" : 24,
							 "T" : 25,
							 "U" : 26,
							 "V" : 27,
							 "W" : 28,
							 "X" : 29,
							 "Y" : 30,
							 "Z" : 31 
							}
		
	def __init__(self, pcblabel):
		self.pcblabel = pcblabel
	
	def getNums(self):
		nums = []
		for val in self.pcblabel:
			nums.append(char_encode[val.upper()])
		return nums
	
	def findSN(self, nums):
		sum = nums[7]+32*(nums[6]+32*(nums[5]+32*(nums[4]+32*(nums[3]+32*(nums[2]+32*(nums[1]+32*(nums[0])))))))
		modo =  ((sum - (sum % 1048576))/1048576) % 262144
		return modo


while True:
	print "(1) SN to PCB Label"
	print "(2) PCB Label to SN"
	print "(3) Quit \n" 
	try:
		select = int(raw_input("> "))
	except ValueError:
		print "Error. Invalid input"
	
	if select == 1:
		print "\nTo quit, use CTRL+C\n"
		while True:
			try:
				newLabel = raw_input("Enter EI9001T Card S/N > ")
				newSN = PCBLabel(newLabel)
				getBin = newSN.dec2bin()
				bit20 = newSN.make20bit(getBin)
				splitValues = newSN.splitBits(bit20)
				print "The PCB Label value for card S/N ", newLabel, " is ", splitValues, "\n"
			except ValueError:
				print "Error. Invalid input"

	elif select == 2:
		print "\nTo quit, use CTRL+C\n"
		while True:
			try:
				PCBtoSN = raw_input("Enter EI9001T PCB Label >")
				newPCB2SN = serialNumber(PCBtoSN)
				numVals = newPCB2SN.getNums()
				SN_value = newPCB2SN.findSN(numVals)
				print "The SN value for card label", PCBtoSN.upper(), " is ", SN_value, "\n" 
			except ValueError:
				print "Error. Invalid input"
	else:
		sys.exit()
			