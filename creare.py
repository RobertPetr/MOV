file = input("Introduceti fisierul: ")

f = open(file)
p = f.read()
f.close()

poz = p.find(".global")
et_start = p[1+p.find(' ', poz): p.find('\n', poz)].strip() + ":"
etichete = [et_start]
keyword_dict = {
    "mov": 1,
    "movl": 1,
    "lea": 2,
    "int": 0xFFFE,
    "call": 0xFFFF,
    "add": 3,
    "addl": 3,
    "sub": 4,
    "subl": 4,
    "push": 5,
    "pushl": 5,
    "pop": 6,
    "popl": 6,
    "cmp": 7,
    "jmp": 0xFF00,
    "jl": 0xFF01,
    "je": 0xFF02,
    "jle": 0xFF03,
    "jg": 0xff04,
    "jge": 0xFF05,
    "jne": 0xFF06,
    "ja": 0xFF07,
    "jb": 0xFF08,
    "jae": 0xFF09,
    "jbe": 0xFF0A,
    "xor": 8,
    "xorl": 8,
    "and": 9,
    "andl": 9,
    "or": 10,
    "orl": 10,
    "not": 11,
    "notl": 11,
    "inc": 12,
    "incl": 12,
    "dec": 13,
    "decl": 13,
    "imul": 14,
    "idivl": 15,
    "idiv": 15,
    "shll": 16,
    "shl": 16,
    "sal": 16,
    "sall": 16,
    "shrl": 17,
    "shr": 17,
    "sar": 17,
    "sarl": 17
}

c = p[9+len(et_start)+poz:]
c = c.split("\n")
t = []
for linie in c:
    linie = linie[:linie.find(";")].strip()
    if linie[-1] == ":":
        etichete.append(linie)
        continue
    com = linie.split()
    if com[0] not in keyword_dict:
        print(f"{com[0]} nu e recunoscut")
        exit(1)
    op = keyword_dict[com[0]]
    if (op & 0xFF00) == 0xFF00:
        t.append((op, com[1:]))
    else:
        