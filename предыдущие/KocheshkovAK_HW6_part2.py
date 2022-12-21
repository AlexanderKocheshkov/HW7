atoms = list()
molekuls = 0
with open("Input.txt") as f:
    for line in f:
        atoms.append(int(line))
f.close()
c, h, o = int(atoms[0]), int(atoms[1]), int(atoms[2])

if (c == 2) and (h == 6) and (o ==1):
    molekuls = 1
elif (c > 2) and (h > 6) and (o > 1):
    print("opa")
    while c >= 2 and h >= 6 and o >= 1:
        molekuls += 1
        c -= 2
        h -= 6
        o -= 1
else:
    molekuls = "Ни одной!:("

print(molekuls)
molekuls = "Молекул спирта: " + str(molekuls)
f = open("Output.txt", "w")
f.write(molekuls)
f.close()
