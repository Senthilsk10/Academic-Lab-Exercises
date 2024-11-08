INSTRUCTION_SET = {
    'LDA': 0x00, 'LDX': 0x04, 'STA': 0x0C, 'STX': 0x10, 
    'ADD': 0x18, 'SUB': 0x1C, 'MUL': 0x20, 'DIV': 0x24
}

def process_line(line):
    parts = line.split()
    if len(parts) == 3:  
        label, opcode, operand = parts
    elif len(parts) == 2:  
        label = None
        opcode, operand = parts
        
    elif len(parts) == 1:  # opcode only
        label = None
        opcode = parts[0]
        operand = None
    else:
        raise SyntaxError("Invalid instruction format")
    return label, opcode, operand

def pass_one_sic_assembler(source_code, start_address=0):
    locctr = start_address
    intermediate_file = []
    symtab = {}
    
    for line in source_code:
        line = line.strip()
        
        if line.startswith("."):
            continue
        
        label, opcode, operand = process_line(line)
        
        
        if opcode == 'START':
            locctr = int(operand, 16)  
            intermediate_file.append((locctr, label, opcode, operand))
            continue

        
        if label:
            if label in symtab:
                raise ValueError(f"Duplicate symbol: {label}")
            symtab[label] = locctr

        
        intermediate_file.append((locctr, label, opcode, operand))

        
        if opcode in INSTRUCTION_SET:
            locctr += 3  
        elif opcode == 'WORD':
            locctr += 3
        elif opcode == 'RESW':
            locctr += 3 * int(operand) 
        elif opcode == 'RESB':
            locctr += int(operand) 
        elif opcode == 'END':
            break
        else:
            raise ValueError(f"Invalid opcode: {opcode}")
    
    return intermediate_file, symtab


source_code = None
with open('program.asm','r') as f:
    source_code = f.readlines()

intermediate_file, symtab = pass_one_sic_assembler(source_code)


with open("intermediate.txt", "w") as int_file:
    for entry in intermediate_file:
        locctr, label, opcode, operand = entry
        int_file.write(f"{locctr:04X}  {label or ''}  {opcode}  {operand or ''}\n")

with open("symtab.txt", "w") as symtab_file:
    for symbol, address in symtab.items():
        symtab_file.write(f"{symbol}  {address:04X}\n")

print("Pass One Complete. Intermediate file and SYMTAB created.")
