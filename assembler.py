import sys

def error(e):
	print("Error raised by assembler:", e)
	quit()

def process(file):
	pFile = ""

	file = file.upper()
	isComm = False
	for char in file:
		if (char != "\n") and (isComm == True):
			continue
		elif (char == "\n") and (isComm == True):
			isComm = False
		elif char == ";":
			isComm = True
		elif isComm == False:
			pFile += char
	pFile = pFile.split()

	return pFile

def addCodeGen(R1, R2):
	code = 0
	if (R1 == "A") and (R2 == "B"):
		code = 16
	elif (R1 == "B") and (R2 == "A"):
		code = 17
	else:
		error("ADD symbol uses unautorised registers")
	return code

def subCodeGen(R1, R2):
	code = 0
	if (R1 == "A") and (R2 == "B"):
		code = 32
	elif (R1 == "B") and (R2 == "A"):
		code = 33
	else:
		error("SUB symbol uses unautorised registers")
	return code

def ldaCodeGen(R1, R2):
	code = 0
	if (R1 == "A") and (R2 == "A"):
		code = 48
	elif (R1 == "A") and (R2 == "B"):
		code = 49
	elif (R1 == "B") and (R2 == "B"):
		code = 50
	elif (R1 == "B") and (R2 == "A"):
		code = 51
	elif (R1 == "A") and (R2.isdigit()):
		code = [52, int(R2)]
	elif (R1 == "B") and (R2.isdigit()):
		code = [53, int(R2)]
	else:
		error("LDA symbol uses unautorised registers")
	return code

def evaluate(file):
	tempCode = []
	finalCode = []
	variables = {}

	sectionStart = False
	sectionData = False
	sectionText = False

	add = False
	sub = False
	lda = False

	R1 = None
	R2 = None

	setVar = False

	lastVar = ""

	fileList = process(file)

	print(fileList)

	for word in fileList:

		if sectionStart == True:
			if word == ".DATA":
				sectionData = True
				sectionStart = False
			elif word == ".TEXT":
				sectionText = True
				sectionStart = False
		elif (sectionData == True) and (word != "SECTION"):
			if setVar == True:
				variables[lastVar] = word
				setVar = False
			else:
				lastVar = word
				setVar = True
		elif (sectionText == True) and (word != "SECTION"):
			if add == True:
				if R1 == None:

					R1 = word
				elif R2 == None:
					R2 = word
					tempCode.append(addCodeGen(R1,R2))
					R1 = None
					R2 = None
					add = False

			elif sub == True:
				if R1 == None:
					R1 = word
				elif R2 == None:
					R2 = word
					tempCode.append(subCodeGen(R1,R2))
					R1 = None
					R2 = None
					sub = False

			elif lda == True:
				if R1 == None:
					R1 = word
				elif R2 == None:
					R2 = word[1:-1]
					tempCodeOne = ldaCodeGen(R1,R2)
					for i in tempCodeOne:
						tempCode.append(i)
					R1 = None
					R2 = None
					lda = False

			else:	
				if word == "ADD":
					add = True
				elif word == "SUB":
					sub = True
				elif word == "LDA":
					lda = True
				else:
					error("Unrecognizable symbol")
		else:
			if word == "SECTION":
				sectionText = False
				sectionData = False
				sectionStart = True

	print(tempCode)
	print(variables)

	a = ""
	for x in tempCode:
		a += str(x)
		a += '\n'

	return a

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Please add a file to be assembled.")
		quit()
	elif len(sys.argv) < 3:
		print("Please add a name for the assembled file.")
		quit()
	else:
		open(sys.argv[2], "w").write(evaluate(open(sys.argv[1], "r").read()))