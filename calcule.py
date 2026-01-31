def offsetTabel():
    return "offset: .long " + " ".join([str(b * 4 * 256) for b in range(256)])

def formatareTabel(nume, T):
    rez = str(nume) + ": .long"
    for linie in T:
        rez = rez + " " + " ".join(str(x) for x in linie)
    return rez

tabelAdunare = []
for a in range(0, 256):
    tabelAdunare.append([(a + b) &0x1FF for b in range(0, 256)])
tabelAdunare = formatareTabel("tabelAdunare", tabelAdunare)

tabelAdunareCuCarry = []
for a in range(0, 256):
    tabelAdunareCuCarry.append([(a + b + 1) &0x1FF for b in range(0, 256)])
tabelAdunareCuCarry = formatareTabel("tabelAdunareCuCarry", tabelAdunareCuCarry)

tabelScadere = []
for a in range(0, 256):
    tabelScadere.append([(a - b) &0xFF for b in range(0, 256)])
tabelScadere = formatareTabel("tabelScadere", tabelScadere)

tabelScadereCuCarry = []
for a in range(0, 256):
    tabelScadereCuCarry.append([(a - b - 1) &0xFF for b in range(0, 256)])
tabelScadereCuCarry = formatareTabel("tabelScadereCuCarry", tabelScadereCuCarry)

tabelAnd = []
for a in range(0, 256):
    tabelAnd.append([(a & b) &0xFF for b in range(0, 256)])
tabelAnd = formatareTabel("tabelAnd", tabelAnd)

tabelOr = []
for a in range(0, 256):
    tabelOr.append([(a | b) &0xFF for b in range(0, 256)])
tabelOr = formatareTabel("tabelOr", tabelOr)

tabelXor = []
for a in range(0, 256):
    tabelXor.append([(a ^ b) &0xFF for b in range(0, 256)])
tabelXor = formatareTabel("tabelXor", tabelXor)


tabelIsZero = "tabelIsZero: .long " + " ".join(["1"] + ["0"] * 0xFFFE)
tabelIsFFFF = "tabelIsFFFF: .long " + " ".join(["0"] * 0xFFFE + ["1"])

tabelCarryAdd = formatareTabel("tabelCarryAdd", [[str((a+b)>>8) for b in range(0, 255)] for a in range(0, 255)])
tabelCarryAddCuCarry = formatareTabel("tabelCarryAddCuCarry",
        [[str((a+b + 1)>>8) for b in range(0, 255)] for a in range(0, 255)])

tabelCarrySub = formatareTabel("tabelCarrySub", [["1" if a < b else "0" for b in range(0, 255)] for a in range(0, 255)])
tabelCarrySubCuCarry = formatareTabel("tabelCarrySubCuCarry",
        [["1" if a < b + 1 else "0" for b in range(0, 255)] for a in range(0, 255)])

tabeDec = [str((a-1) & 0xFFFF) for a in range(0, 0xFFFF)]
tabeDec = "tabeDec: .long " + " ".join(tabeDec)

with open("tabele", "w") as g:
    output = "\n".join([offsetTabel(), tabelIsFFFF, tabelIsZero, tabelAdunare, tabelAdunareCuCarry, tabelCarryAdd,
    tabelCarryAddCuCarry, tabelAnd, tabelOr, tabelScadere, tabelScadereCuCarry,
    tabelCarrySub, tabelCarrySubCuCarry, tabelXor]) + "\n"
    g.write(output)