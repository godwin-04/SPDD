ST = []
LT = []
lc = 0
SOURCE_FILE = "input.txt"
pseudo = ["START", "END", "USING"]
BT = []
MOT = [
    ("LDA", 1, 3),
    ("STA", 2, 3),
    ("ADD", 3, 3),
    ("SUB", 4, 3),
    ("MUL", 5, 3),
    ("DIV", 6, 3),
    ("JMP", 7, 3),
]
POT = [
    ("START", 1),
    ("END", 2),
    ("DC", 3),
    ("DS", 4)
]

with open(SOURCE_FILE, "r") as f:
    for line in f:
        line = line.rstrip()
        # print(line)
        # print("***")
        tokens = line.split("\t")
        # print(tokens)
        l = 0
        c = "R"
        if tokens[1] == "USING":
            y = tokens[-1].split(",")
            if y[0] == "*":
                BT.append((y[1], lc))
            else:
                BT.append((y[1], y[0]))
        if tokens[1] == "EQU":
            c = "A"
        if tokens[1] not in pseudo:
            if tokens[1][-1] == "R":
                lc += 2
                l = 2
            else:
                lc += 4
                l = 4
        else:
            l = 1
        if tokens[0] != "-" and tokens[0] != "":
            ST.append((tokens[0], lc, l, c))
        x = tokens[-1].split(",")
        # print(x)
        if x[-1][0] == "=":
            LT.append((x[-1][1:], lc, l, c))

print("MOT")
print()
for i in MOT:
    for j in i:
        print(j, "\t", end="")
    print()
print("-------------------------------------")
print("POT")
print()
for i in POT:
    for j in i:
        print(j, "\t", end="")
    print()
print("-------------------------------------")
print("SYMBOL TABLE")
print("\nsymbol, value, length, relocation")
for i in ST:
    for j in i:
        print(j, "\t", end="")
    print()
print("-------------------------------------")
print("\nLITERAL TABLE")
print("\nliteral, value, length, relocation")
for i in LT:
    for j in i:
        print(j, "\t", end="")
    print()
print("-------------------------------------")
print("\nBASE TABLE")
print("\nBase, value")
for i in BT:
    for j in i:
        print(j, "\t", end="")
    print()
