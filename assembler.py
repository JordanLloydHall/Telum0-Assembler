import sys
import helper
from instructions import *

inst = {}



def error(e):
	print("Error raised by assembler:", e)
	quit()

def evaluate(file):
	tBlock = []
	dBlock = []
	bBlock = []

	addressDefs = {}
	constDefs = {}
	totalCode = []

	text = False
	data = False
	bss = False

	file = helper.process(file)

	for line in file:
		if line[0] == "SECTION":
			if len(line) != 2:
				error("Section only takes 1 operand.")
			else:
				text, data, bss = False, False, False
				if line[1] == ".TEXT":
					text = True

				elif line[1] == ".DATA":
					data = True

				elif line[1] == ".BSS":
					bss = True
				else:
					error("Section type not recognised.")

		elif text == True:
			if line[0] == "ADD":
				if len(line) != 3:
					error("An add operation requires 2 operands.")
				else:
					if (line[1] in REGS) and (line[2] in REGS):
						tBlock.append([ADD[(line[1], line[2])]])
					else:
						error("Add operations can only interact with registers.")

			elif line[0] == "SUB":
				if len(line) != 3:
					error("A sub operation requires 2 operands.")
				else:
					if (line[1] in REGS) and (line[2] in REGS):
						tBlock.append([SUB[(line[1], line[2])]])
					else:
						error("Sub operations can only interact with registers.")

			elif line[0] == "LDA":
				if len(line) != 3:
					error("An lda operation requires 2 operands.")
				else:
					if (line[1] in REGS) and (line[2] in REGS):
						tBlock.append([LDA[(line[1], line[2])]])
					elif (line[1] in REGS):
						tBlock.append([LDA[(line[1], "INT")]])
						tBlock.append([line[2]])
					else:
						error("Lda operations require registers or memory addresses.")

			elif line[0] == "LDI":
				if len(line) != 3:
					error("An ldi operation requires 2 operands.")
				else:
					if (line[1] in REGS) and (line[2].isdigit()):
						tBlock.append([LDI[(line[1], "INT")]])
						tBlock.append([helper.intToHexStr(int(line[2]))])
					else:
						error("Ldi operations require a register and an integer.")

			elif line[0] == "STR":
				if len(line) != 3:
					error("An str operation requires 2 operands.")
				else:
					if (line[1] in REGS) and (line[2] in REGS):
						tBlock.append([LDA[(line[1], line[2])]])
					elif (line[2] in REGS):
						tBlock.append([STR[("INT", line[2])]])
						tBlock.append([line[1]])
					else:
						error("Str operations require registers or memory addresses.")

			elif line[0] == "MV":
				if len(line) != 3:
					error("An mv operation requires 2 operands.")
				else:
					if (line[1] in REGS) and (line[2] in REGS):
						tBlock.append([MV[(line[1], line[2])]])
					else:
						error("Mv operations can only interact with registers.")

			elif line[0] == "JMP":
				if len(line) != 2:
					error("A jmp operation requires 1 operand.")
				else:
					if line[1] in REGS:
						tBlock.append([JMP[(line[1])]])
					else:
						tBlock.append([JMP["INT"]])
						tBlock.append([line[1]])

			elif line[0] == "JMPZ":
				if len(line) != 2:
					error("A jmpz operation requires 1 operand.")
				else:
					if line[1] in REGS:
						tBlock.append([JMPZ[(line[1])]])

					else:
						tBlock.append([JMPZ["INT"]])
						tBlock.append([line[1]])

			elif line[0] == "IN":
				if len(line) != 2:
					error("An in operation requires 1 operand.")
				else:
					if line[1] in REGS:
						tBlock.append([IN[line[1]]])
					else:
						error("In operations can only interact with registers.")

			elif line[0] == "OUT":
				if len(line) != 2:
					error("An out operation requires 1 operand.")
				else:
					if line[1] in REGS:
						tBlock.append([OUT[line[1]]])
					else:
						error("Out operations can only interact with registers.")

			elif line[0] == "HLT":
				tBlock.append([HLT])

			else:
				if len(line) != 1:
					print("Command found not acceptable.")
				else:
					tBlock.append(["addressDef",line[0]])

		elif data == True:

			if len(line) != 2:
				error("Data variables must only have 2 arguments.")
			else:
				if line[1].isdigit():
					dBlock.append([line[0], line[1]])
				else:
					error("Variables must only contain data.")

		else:
			error("Instruction block not specified.")

	for inst in range(len(tBlock)):
		try:
			if (len(tBlock[inst]) == 2) and (tBlock[inst][0] == "addressDef"):
				if tBlock[inst][1] not in addressDefs:
					address = tBlock[inst][1]
					tBlock.pop(inst)
					addressDefs[address] = helper.intToHexStr(inst+2)
				else:
					error("Found address def that was already stated.")
		except:
			break


	if "_START" not in addressDefs:
		error("Assembly program must have start definition.")

	for const in range(len(dBlock)):
		if dBlock[const][0] not in constDefs:
			constDefs[dBlock[const][0]] = helper.intToHexStr(const+2+len(tBlock))

	for inst in range(len(tBlock)):
		if (not helper.isHex(tBlock[inst][0])) or (len(tBlock[inst][0]) > 2):
			if tBlock[inst][0] in constDefs:
				tBlock[inst][0] = constDefs[tBlock[inst][0]]

	print(len(tBlock))

	for inst in range(len(tBlock)):
		if (not helper.isHex(tBlock[inst][0])) and (tBlock[inst][0] in addressDefs):
			tBlock[inst][0] = addressDefs[tBlock[inst][0]]


	print(len(tBlock))

	totalCode.append(["72"])
	totalCode.append([addressDefs["_START"]])
	for inst in tBlock:
		totalCode.append(inst)
	for const in dBlock:
		totalCode.append([helper.intToHexStr(int(const[1]))])

	retText = helper.outText(totalCode)

	return retText

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Please add a file to be assembled.")
		quit()
	elif len(sys.argv) < 3:
		print("Please add a name for the assembled file.")
		quit()
	else:
		open(sys.argv[2], "w").write(evaluate(open(sys.argv[1], "r").read()))