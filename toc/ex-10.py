import re

class Register:
    def __init__(self):
        self.var = ""
        self.alive = False

def get_register(var, registers):
    for i in range(10):
        if not registers[i].alive:
            registers[i].var = var
            registers[i].alive = True
            return i
    return -1

def get_var(exp):
    match = re.match(r"([a-zA-Z]+)", exp)
    return match.group(0) if match else ""

def process_code(lines):
    registers = [Register() for _ in range(10)]

    for line in lines:
        line = re.sub(r'\s*([+\-*/])\s*', r' \1 ', line)
        parts = line.split()

        if len(parts) < 5:
            continue

        var1 = get_var(parts[2])
        operator = parts[3]
        var2 = get_var(parts[4])
        result = parts[0]

        reg1 = get_register(var1, registers)
        reg2 = get_register(var2, registers)
        reg_result = get_register(result, registers)

        if reg1 != -1:
            print(f"Mov R{reg1}, {var1}")
        if reg2 != -1:
            print(f"Mov R{reg2}, {var2}")

        if operator == '+':
            print(f"Add R{reg1}, R{reg2}")
        elif operator == '-':
            print(f"Sub R{reg1}, R{reg2}")
        elif operator == '*':
            print(f"Mul R{reg1}, R{reg2}")
        elif operator == '/':
            print(f"Div R{reg1}, R{reg2}")

        if reg_result != -1:
            print(f"Mov R{reg_result}, R{reg1}")

        if reg1 != -1:
            registers[reg1].alive = False
        if reg2 != -1:
            registers[reg2].alive = False

lines = []
line = ''
while line != 'exit':
    line = input()
    lines.append(line)

process_code(lines)
