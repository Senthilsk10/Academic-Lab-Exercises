# Source code
source_code = [
    "MACRO ADD &X,&Y",
    "LOAD &X",
    "ADD &Y",
    "STORE &X",
    "MEND",
    "START",
    "ADD A,B",
    "END"
]

mnt = {}
mdt = []


def process_macros(source_code):
    is_macro_def = False  
    macro_name = ""       
    
    for line in source_code:
        tokens = line.split()
        if tokens[0] == "MACRO":
            is_macro_def = True
            macro_name = tokens[1]
            mnt[macro_name] = len(mdt)  
            params = tokens[2].split(',')
            # print(tokens)
            mdt.append((macro_name, params))  
        elif tokens[0] == "MEND":
            is_macro_def = False
        elif is_macro_def:
            mdt.append(line)
        elif tokens[0] in mnt:
            macro_start = mnt[tokens[0]]
            macro_params = tokens[1].split(',')
            


process_macros(source_code)

print("Macro Name Table (MNT):", mnt)
print("Macro Definition Table (MDT):", mdt)

