INSTRUCTION_SET = {
    'LDA': 0x00, 'LDX': 0x04, 'STA': 0x0C, 'STX': 0x10, 
    'ADD': 0x18, 'SUB': 0x1C, 'MUL': 0x20, 'DIV': 0x24
}

def prosce(line):
    part=line.split()
    if len(part) == 3:
        label,opcode,operand=part
    elif len(part) == 2:
        label=None
        opcode,operand=part
    else:
        raise SyntaxError('lable not found')
    return label,opcode,operand

def pass_one(source):
    lac=0
    intermediate=[]
    symtab={}
    for line in source:
        label,opcode,operand=prosce(line)
        if opcode=='START':
            lac=int(operand)
            intermediate.append((lac,label,opcode,operand))
            continue
        if label:
            if label in symtab:
                raise SyntaxError('dublicate entry')
            label[symtab]=lac
        if opcode in INSTRUCTION_SET:
            lac +=3
        elif opcode=='RESW':
            lac +=3*int(operand)
        elif opcode=='RESB':
            lac +=int(operand)
        elif opcode=='END':
            break
        intermediate.append((lac,label,opcode,operand))
    return lac,label,opcode,operand
source=open('D:\python\toc\preparation\program.asm','r').readlines()
sym,inter=pass_one(source)
print(inter)
print(sym)
        
    
    