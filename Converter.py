def mainMenu ():
	print("===================")
	print("Mark's Converter")
	print("===================")
	nav = raw_input("[Temp] , [Weight] , [Planetary] , [Quit] >>>")
	if (nav == "Temp"):
		fToC()
	elif (nav == "Weight"):
		pToG()
	elif (nav == "Quit"):
		print("QUITTING APPLICATION")
	elif (nav == "Planetary"):
		planetWeight()
	else:
		print("Not Acceptable Input.")
		mainMenu()

def fToC ():
	x = raw_input("Starting Temp: [C] or [F]? >>>")
	if (x == "C"):
		cToFCalc()
	elif (x == "F"):
		fToCCalc()
	elif (x == "Menu"):
		mainMenu()
	else:
		print("Not Acceptable Input.")
		fToC()

def fToCCalc ():
	x = input("Temperature In F >>>")
	x = (x - 32) * 0.5556
	print(x,"C")
	print("===================")
	fToC()

def cToFCalc ():
	x = input("Temperature In C >>>")
	x = (x/0.5556) + 32
	print(x,"F")
	print("===================")
	fToC()

def pToG ():
	x = raw_input("Starting Weight: [P] or [G]? >>>")
	if (x == "P"):
		pToGCalc()
	elif (x == "G"):
		gToPCalc()
	elif (x == "Menu"):
		mainMenu()
	else:
		print("Not Acceptable Input.")
		pToG()
def pToGCalc ():
	x = input("Weight In Pounds >>>")
	x = x/0.0022
	print(x,"Grams")
	print("===================")
	pToG()

def gToPCalc ():
	x = input("Mass In Grams >>>")
	x = x * 0.0022
	print(x,"Pounds")
	print("===================")
	pToG()

def planetWeight ():
	planet = raw_input("Select A Planet: [Mercury] , [Venus] , [Mars] , [Jupiter] , [Saturn] , [Uranus] , [Neptune] >>>")
	if (planet == "Mercury"):
		x = input("Weight In Pounds >>>")
		x = x * 0.38
		print("Your Weight On Mercury Is: ",x,"Pounds.")
		print("===================")
		planetWeight()
	elif (planet == "Venus"):
		x = input("Weight In Pounds >>>")
		x = x * 0.82
		print("Your Weight On Venus Is: ",x,"Pounds")
		print("===================")
		planetWeight()
	elif (planet == "Mars"):
		x = input("Weight In Pounds >>>")
		x = x * 0.375
		print("Your Weight On Mars Is: ",x,"Pounds")
		print("===================")
		planetWeight()
	elif (planet == "Jupiter"):
		x = input("Weight In Pounds >>>")
		x = x * 2.5
		print("Your Weight On Jupiter Is: ",x,"Pounds")
		print("===================")
		planetWeight()
	elif (planet == "Saturn"):
		x = input("Weight In Pounds >>>")
		x = x * 1.07
		print("Your Weight On Saturn Is: ",x,"Pounds")
		print("===================")
		planetWeight()
	elif (planet == "Uranus"):
		x = input("Weight In Pounds >>>")
		x = x * 0.86
		print("Your Weight On Uranus Is: ",x,"Pounds")
		print("===================")
		planetWeight()
	elif (planet == "Neptune"):
		x = input("Weight In Pounds >>>")
		x = x * 1.10
		print("Your Weight On Neptune Is: ",x,"Pounds")
		print("===================")
		planetWeight()
	elif (planet == "Menu"):
		mainMenu()
	else:
		print("Not Acceptable Input.")
		planetWeight()

mainMenu()