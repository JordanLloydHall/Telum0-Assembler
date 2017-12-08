
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
