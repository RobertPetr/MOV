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

tabelCMP = []
for a in range(0, 256):
    tabelCMP.append([0 if a < b else (1 if a == b else 2) for b in range(0, 256)])
tabelCMP = formatareTabel("tabelCMP", tabelCMP)

tabelIsZero = "tabelIsZero: .long " + " ".join(["1"] + ["0"] * 0xFFFE)
tabelIsFFFF = "tabelIsFFFF: .long " + " ".join(["0"] * 0xFFFE + ["1"])

tabeInc = [str((a+1) & 0xFFFF) for a in range(0, 0xFFFF)]
tabeInc = "tabeInc: .long " + " ".join(tabeInc)

tabelCarryAdd = formatareTabel("tabelCarryAdd", [[str((a+b)>>8) for b in range(0, 255)] for a in range(0, 255)])
tabelCarryAddCuCarry = formatareTabel("tabelCarryAddCuCarry",
        [[[str((a+b + 1)>>8) for b in range(0, 255)] for a in range(0, 255)])

tabelCarryAdd = formatareTabel("tabelCarryAdd", [[str((a+b)>>8) for b in range(0, 255)] for a in range(0, 255)])
tabelCarryAddCuCarry = formatareTabel("tabelCarryAddCuCarry",
        [[[str((a+b + 1)>>8) for b in range(0, 255)] for a in range(0, 255)])

tabeDec = [str((a-1) & 0xFFFF) for a in range(0, 0xFFFF)]
tabeDec = "tabeDec: .long " + " ".join(tabeDec)

with open("tabele", "w") as g:
    output = "\n".join([offsetTabel(), tabelIsFFFF, tabelIsZero, tabelAdunare, tabelAdunareCuCarry, tabeDec,
    tabeInc, tabelAnd, tabelCMP, tabelOr, tabelScadere, tabelScadereCuCarry, tabelXor]) + "\n"
    g.write(output)