INSTRUCTION_SET = {
    'LDA': 0x00, 'LDX': 0x04, 'STA': 0x0C, 'STX': 0x10, 
    'ADD': 0x18, 'SUB': 0x1C, 'MUL': 0x20, 'DIV': 0x24
}

inter = [
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

sym = {'FIRST': 0x1000, 'ALPHA': 0x100c, 'BETA': 0x100f}


def pass_two(inter,sym):
    object_code = []
    header = ''
    end = ''
    text = ''
    text_records = []
    text_str = ''
    start = None
    for line in inter:
        loc,label,opcode,operand = line
        
        if opcode == 'START':
            name = label or 'DEFAULT'
            start = int(operand,16)
            header = f'H{name:<6}{start:06X}'
            # print(header)
            continue
        
        if opcode in INSTRUCTION_SET:
            opcode_hex = INSTRUCTION_SET[opcode] <<16
            if operand in sym:
                operand_hex = sym[operand]
            else:
                operand_hex = 0
                
            
            text = opcode_hex+operand_hex
            text = f'{text:06X}'
            
            text_records.append(text)
        elif opcode in ['RESW','RESB']:
            continue
        elif opcode == 'END':
            print(operand,opcode)
            end = f'E{sym[operand]:06X}'
            # print(end)
        text_str = 'T'+''.join(text_records)
    
    with open('object_code.txt','w') as f:
        f.write(header+'\n')
        f.write(text_str+'\n')
        f.write(end)

    
    
            
pass_two(inter,sym)