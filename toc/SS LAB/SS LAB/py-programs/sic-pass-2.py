INSTRUCTION_SET = {
    'LDA': 0x00, 'LDX': 0x04, 'STA': 0x0C, 'STX': 0x10,
    'ADD': 0x18, 'SUB': 0x1C, 'MUL': 0x20, 'DIV': 0x24
}

def pass_two_sic_assembler(intermediate_file, symtab):
    object_code = []
    header_record = None
    text_records = []
    end_record = None

    for line in intermediate_file:
        locctr, label, opcode, operand = line
        
       
        if opcode == 'START':
            start_address = int(operand, 16)
            program_name = label or "DEFAULT"
            header_record = f"H{program_name:<6}{start_address:06X}{0:06X}"
            continue
        
        if opcode in INSTRUCTION_SET:
            opcode_hex = INSTRUCTION_SET[opcode] << 16  # shift to 24 bits as 3 bytes
            
            if operand in symtab:
                operand_address = symtab[operand]
            else:
                operand_address = 0  # If operand is not found, use 0 (error case should be handled)

            instruction_obj_code = opcode_hex + operand_address
            
            object_code_hex = f"{instruction_obj_code:06X}"
            
            text_records.append(object_code_hex)
        
        elif opcode == 'RESW' or opcode == 'RESB':
            continue
        
        elif opcode == 'END':
            end_record = f"E{symtab[operand]:06X}"
    
    
    text_record_str = "T{:<06X}{:<02X}".format(start_address, len(text_records) * 3) + ''.join(text_records)

    program_length = locctr - start_address
    header_record = f"H{program_name:<6}{start_address:06X}{program_length:06X}"

    
    with open("object_code.txt", "w") as obj_file:
        obj_file.write(header_record + "\n")
        obj_file.write(text_record_str + "\n")
        obj_file.write(end_record + "\n")

    print("Pass Two Complete. Object code generated.")

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

pass_two_sic_assembler(intermediate_file, symtab)
