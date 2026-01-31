file = input("Introduceti fisierul: ")

f = open(file)
p = f.read()
f.close()

poz = p.find(".global")
et_start = p[1+p.find(' ', poz): p.find('\n', poz)].strip() + ":"
etichete = [(0, et_start)]
keyword_dict = {
    "mov": 1,
    "movl": 1,
    "lea": 0xAA02,
    "int": 0xFFFE,
    "call": 0xFFFF,
    "add": 3,
    "addl": 3,
    "sub": 4,
    "subl": 4,
    "push": 0xAA05,
    "pushl": 0xAA05,
    "pop": 0xAA06,
    "popl": 0xAA06,
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
    "imul": 0xAA14,
    "idivl": 0xAA15,
    "idiv": 0xAA15,
    "shll": 16,
    "shl": 16,
    "sal": 16,
    "sall": 16,
    "shrl": 17,
    "shr": 17,
    "sar": 17,
    "sarl": 17
}

def MOV(operanzi):
    return f"mov {operanzi[0]}, {operanzi[1]}"

def LEA(operanzi):
    pass

def ADD(operanzi):
    # trebuie "calculat" array-uri de pointeri la etapa de init
    return f"""mov Carry, 0
    mov Zero, 1
    mov eax, add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]}, bl


    mov eax, add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 1, bl

    mov eax, add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 2, bl

    mov eax, add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_add8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 3, bl
    """

def SUB(operanzi):
    # trebuie "calculat" array-uri de pointeri la etapa de init
    return f"""mov Carry, 0
    mov Zero, 1
    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]}, bl


    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 1, bl

    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 2, bl

    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 3, bl
    """

def CMP(operanzi):
    # trebuie "calculat" array-uri de pointeri la etapa de init
    return f"""mov Carry, 0
    mov Zero, 1
    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl


    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl


    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl


    mov eax, sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    
    mov bl, al

    mov eax, carry_sub8[BYTE Carry]
    mov eax, [eax + BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    mov Carry, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl
    """
def AND(operanzi):
    # trebuie "calculat" array-uri de pointeri la etapa de init
    return f"""mov Carry, 0
    mov Zero, 1
    mov eax, and8[BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]}, bl


    mov eax, and8[BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 1, bl

    mov eax, and8[BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 2, bl

    mov eax, and8[BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 3, bl
    """

def OR(operanzi):
    # trebuie "calculat" array-uri de pointeri la etapa de init
    return f"""mov Carry, 0
    mov Zero, 1
    mov eax, or8[BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]}, bl


    mov eax, or8[BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 1, bl

    mov eax, or8[BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 2, bl

    mov eax, or8[BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 3, bl
    """
def XOR(operanzi):
    # trebuie "calculat" array-uri de pointeri la etapa de init
    return f"""mov Carry, 0
    mov Zero, 1
    mov eax, xor8[BYTE {operanzi[1]}]
    mov eax, [eax + BYTE {operanzi[0]}]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]}, bl


    mov eax, xor8[BYTE {operanzi[1]} + 1]
    mov eax, [eax + BYTE {operanzi[0]} + 1]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 1, bl

    mov eax, xor8[BYTE {operanzi[1]} + 2]
    mov eax, [eax + BYTE {operanzi[0]} + 2]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 2, bl

    mov eax, xor8[BYTE {operanzi[1]} + 3]
    mov eax, [eax + BYTE {operanzi[0]} + 3]
    mov al, [eax]
    
    mov bl, al

    mov eax, is_zero[bl]
    mov edx, and8[Zero]
    mov edx, [edx + eax]
    mov Zero, dl

    mov BYTE {operanzi[0]} + 3, bl
    """

c = p[9+len(et_start)+poz:]
c = c.split("\n")
t = []
Flags = {
    "ZF": 0,
    "CF": 0,
    "OF": 0,
    "SF": 0,
}
for i, linie in enumerate(c):
    if linie.find(";") != -1:
        linie = linie[:linie.find(";")].strip()
    else:
        linie = linie.strip()
    if linie[-1] == ":":
        etichete.append((i, linie))
        continue
    com = linie.split()
    if com[0] not in keyword_dict:
        print(f"{com[0]} nu e recunoscut")
        exit(1)
    op = keyword_dict[com[0]]
    t.append((op, [x.replace(',', '') for x in com[1:]]))

codul = []
for op in t:
    
# avem toate liniile categorizate