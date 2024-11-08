source =  open("program.asm",'r').readlines()
instruction = {
    'LDA': 0x00, 'LDX': 0x04, 'STA': 0x0C, 'STX': 0x10, 
    'ADD': 0x18, 'SUB': 0x1C, 'MUL': 0x20, 'DIV': 0x24
}

def process_line(line):
    parts = line.split()
    if len(parts) == 3:
        label,opcode,operand = parts
    if len(parts) == 2:
        opcode,operand = parts
        label = None
    
    return label,opcode,operand

def pass_one(source,start_address = 1000):
    loc = 0
    symtab = {}
    intermediate = []
    
    for line in source:
        label,opcode,operand = process_line(line)
        
        if opcode == 'START':
            loc = int(operand,16)
            intermediate.append((loc,label,opcode,operand))
            continue
            
        if label:
            if label in symtab:
                raise ValueError('duplicate variable')
            symtab[label] = loc
            
        intermediate.append((loc,label,opcode,operand))
        
        if opcode in instruction or opcode == 'WORD':
            loc += 3
        elif opcode == "RESW":
            loc += 3* int(operand)
        elif opcode == 'RESB':
            loc += int(operand)
        elif opcode == "END":
            break
            
    return intermediate,symtab


inter,sym = pass_one(source)

print(inter)
print(sym) 
