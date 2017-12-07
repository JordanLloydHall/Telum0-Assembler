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

	totalCode = []

	text = False
	data = False
	bss = False

	file = helper.process(file)

	for line in file:
		if line[0] == "SECTION":
			if len(line) != 2:
				error("Section only takes 1 operand")
			else:
				if line[1] == ".TEXT":



	return ""

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Please add a file to be assembled.")
		quit()
	elif len(sys.argv) < 3:
		print("Please add a name for the assembled file.")
		quit()
	else:
		open(sys.argv[2], "w").write(evaluate(open(sys.argv[1], "r").read()))