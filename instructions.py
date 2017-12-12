
REGS = ["A", "B"]

ADD = {("A", "B"):"10",
		("B", "A"):"11"}

SUB = {("A", "B"):"20",
		("B", "A"):"21"}

LDA = {("A", "B"):"30",
		("B", "A"):"31",
		("A", "A"):"32",
		("B", "B"):"33",
		("A", "INT"):"34",
		("B", "INT"):"35"}

LDI = {("A", "INT"):"40",
		("B", "INT"):"41"}

STR = {("A", "B"):"50",
		("B", "A"):"51",
		("A", "A"):"52",
		("B", "B"):"53",
		("INT", "A"):"54",
		("INT", "B"):"55"}

MV = {("A", "B"):"60",
		("B", "A"):"61"}

JMP = {"A":"70",
		"B":"71",
		"INT":"72"}

JMPZ = {"A":"80",
		"B":"81",
		"INT":"82"}

JMPC = {"A":"90",
		"B":"91",
		"INT":"92"}

IN = {"A":"A0",
		"B":"A1"}


OUT = {"A":"B0",
		"B":"B1"}

HLT = "C0"