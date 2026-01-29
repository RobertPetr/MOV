def offsetTabel():
    return "offset: .long " + " ".join([str(b * 4 * 256) for b in range(256)])

def formatareTabel(nume, T):
    rez = str(nume) + ": .long"
    for linie in T:
        rez = rez + " " + " ".join(str(x) for x in linie)
    return rez

tabelAdunare = []
for a in range(0, 256):
    tabelAdunare.append([(a + b) &0xFF for b in range(0, 256)])
tabelAdunare = formatareTabel("tabelAdunare", tabelAdunare)

tabelInmultire = []
for a in range(0, 256):
    tabelInmultire.append([(a + b) &0xFF for b in range(0, 256)])
tabelInmultire = formatareTabel("tabelInmultire", tabelInmultire)

tabelScadere = []
for a in range(0, 256):
    tabelScadere.append([(a - b) &0xFF for b in range(0, 256)])
tabelScadere = formatareTabel("tabelScadere", tabelScadere)

tabelImpartire = []
for a in range(0, 256):
    tabelImpartire.append([(a // b) &0xFF if b != 0 else 0xFFFFFFFF for b in range(0, 256)])
tabelImpartire = formatareTabel("tabelImpartire", tabelImpartire)

tabelModulo = []
for a in range(0, 256):
    tabelModulo.append([(a % b) &0xFF if b != 0 else 0xFFFFFFFF for b in range(0, 256)])
tabelModulo = formatareTabel("tabelModulo", tabelModulo)

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

tabelMod10 = [str(a % 10) for a in range(0, 0xFFFF)]
tabelMod10 = "tabelMod10: .long " + " ".join(tabelMod10)

tabelCMP = []
for a in range(0, 256):
    tabelCMP.append([0 if a < b else (1 if a == b else 2) for b in range(0, 256)])
tabelCMP = formatareTabel("tabelCMP", tabelCMP)

tabeInc = [str((a+1) & 0xFFFF) for a in range(0, 0xFFFF)]
tabeInc = "tabeInc: .long " + " ".join(tabeInc)

tabeDec = [str((a-1) & 0xFFFF) for a in range(0, 0xFFFF)]
tabeDec = "tabeDec: .long " + " ".join(tabeDec)

with open("tabele", "w") as g:
    output = "\n".join([offsetTabel(), tabelAdunare, tabeDec, tabeInc,
    tabelAnd, tabelCMP, tabelImpartire, tabelInmultire, tabelMod10, tabelModulo, tabelOr,
    tabelScadere, tabelXor])
    g.write(output)