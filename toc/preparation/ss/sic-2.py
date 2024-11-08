INSTRUCTION_SET = {
    'LDA': 0x00, 'LDX': 0x04, 'STA': 0x0C, 'STX': 0x10,
    'ADD': 0x18, 'SUB': 0x1C, 'MUL': 0x20, 'DIV': 0x24
}

intermediate_file = [
    (0x1000, 'COPY', 'START', '1000'),
    (0x1000, 'FIRST', 'LDA', 'FIVE'),
    (0x1003, None, 'ADD', 'BETA'),
    (0x1006, None, 'SUB', 'GAMMA'),
    (0x1009, None, 'STA', 'ALPHA'),
    (0x100C, 'SECOND', 'LDX', 'ALPHA'),
    (0x100F, None, 'STX', 'DELTA'),
    (0x1012, None, 'RESW', '1'),
    (0x1015, None, 'RESB', '5'),
    (0x101A, None, 'END', 'FIRST')
]

# Sample symbol table (from Pass One)
symtab = {
    'COPY': 0x1000,
    'FIRST': 0x1000,
    'SECOND': 0x100C,
    'FIVE': 0x1018,
    'BETA': 0x101B,
    'GAMMA': 0x101E,
    'ALPHA': 0x1021,
    'DELTA': 0x1024
}


def pass_two(source,sym):
    header = None
    end = None
    textrecords = []
    obj_code =[]
    
    for (loctr,label,opcode,operand) in source:
        if opcode == 'START':
            name = label or 'DEFAULT'
            start_add = int(operand,16)
            header = f'H{label:<6}{start_add:06X}{0:06X}'
            continue
        
        if opcode in INSTRUCTION_SET:
            op_hex = INSTRUCTION_SET.get(opcode) <<16
            
            oper_hex = symtab.get(operand,0)
            
            code = op_hex+oper_hex
            
            text = f'{code:06X}'
            textrecords.append(text)
            
        elif opcode in ['RESW','RESB']:
            continue
        
        elif opcode == 'END':
            end_record = f'E{symtab[operand]:06X}'
            
    text_str = f'T{start_add:<06X}{len(textrecords)*3:<02X}'+''.join(textrecords)

    obj_code = header + text_str + end_record
    
    return obj_code

print(pass_two(intermediate_file,symtab))