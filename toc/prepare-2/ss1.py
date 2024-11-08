INSTRUCTION_SET = {
    'LDA': 0x00, 'LDX': 0x04, 'STA': 0x0C, 'STX': 0x10, 
    'ADD': 0x18, 'SUB': 0x1C, 'MUL': 0x20, 'DIV': 0x24
}

def process_line(line):
    parts = line.split()
    print(parts)
    if len(parts) == 3:
        label,opcode,operand = parts
    elif len(parts) == 2:
        label = None
        opcode,operand = parts
    else:
        raise SyntaxError('invalid instruiction')
    return label,opcode,operand


def pass_one(source):
    loc = 0
    intermediate = []
    symtab = {}
    
    for line in source:
        label,opcode,operand = process_line(line)
        
        if opcode == 'START':
            loc = int(operand)
            intermediate.append((loc,label,opcode,operand))
            continue
        
        if label:
            if label in symtab:
                raise ValueError('duplicate entry for label')
            symtab[label] = loc 
        
        if opcode in INSTRUCTION_SET:
            loc += 3
        elif opcode == 'RESW':
            loc += 3*int(operand)
        elif opcode == 'RESB':
            loc += int(operand)
        elif opcode == 'END':
            
            break
        
        intermediate.append((loc,label,opcode,operand))
        
    return symtab,intermediate


source = open('program.asm','r').readlines()
sym,inter = pass_one(source)

print('sym',sym)
print('inter',inter)