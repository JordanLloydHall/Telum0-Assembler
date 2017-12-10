
def error(e):
	print("Error raised by assembler:", e)
	quit()

def process(file):
	file = file.split("\n")
	pFile = []
	tokFile = []

	for line in range(len(file)):
		file[line] = file[line].upper()
		pFile.append("")

		for char in range(len(file[line])):
			

			if file[line][char] == ";":
				break
			else:
				pFile[line] += file[line][char]
	
	for line in pFile:
		if line == "":
			continue
		else:
			tokFile.append([x.replace(" ", "").replace(",", "") for x in line.split(" ") if x != ""])

	return tokFile

def intToHexStr(num):
	if (num <= 255) and (num >= 0):
		retNum = hex(num).upper()
		if len(retNum) < 4:
			return "0" + retNum[-1:]
		else:
			return retNum[-2:]
	else:
		error("Parsable decimal number is between 0 and 255")

def isHex(num):
	hexChars = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

	for digit in num:
		if digit not in hexChars:
			return False

	return True

def outText(code):
	out = ""
	for i in code:
		out += i[0] + "\n"

	return out