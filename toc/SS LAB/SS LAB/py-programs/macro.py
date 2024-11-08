import re

def pass_one(source_code):
    """
    Pass 1 of the macro processor.
    Identifies macro definitions and builds the MNT (Macro Name Table) and MDT (Macro Definition Table).
    """

    mnt = {}  # Macro Name Table
    mdt = []  # Macro Definition Table
    mdtc = 0  # Macro Definition Table Counter
    inside_macro = False
    macro_name = None

    for line in source_code:
        tokens = line.split()
        if not tokens:
            continue
            
        if tokens[0] == "MACRO":
            inside_macro = True
            macro_name = tokens[1] if len(tokens) > 1 else None
            
            if macro_name is not None:
                mnt[macro_name] = {"mdt_index": mdtc, "params": tokens[2:]}  # Collect params
                mdt.append(line)
                mdtc += 1
            else:
                print("Error: Macro name is missing.")
        
        elif tokens[0] == "MEND":
            inside_macro = False
            mdt.append(line)
            mdtc += 1
        elif inside_macro:
            mdt.append(line)
            mdtc += 1
        else:
            pass 

    return mnt, mdt


def pass_two(source_code, mnt, mdt):
    """
    Pass 2 of the macro processor.
    Expands macro calls in the source code.
    """

    expanded_code = []

    for line in source_code:
        if line.startswith("MACRO"):
            continue

        macro_call = re.match(r"(\w+)\s*(.*)", line)
        if macro_call:
            macro_name = macro_call.group(1)
            if macro_name in mnt:
                macro_args = [arg.strip() for arg in macro_call.group(2).split(",")]
                param_names = mnt[macro_name]["params"]
                mdt_index = mnt[macro_name]["mdt_index"]

                for i in range(mdt_index + 1, len(mdt)):
                    if mdt[i].startswith("MEND"):
                        break
                    expanded_line = mdt[i]
                    for param, arg in zip(param_names, macro_args):
                        expanded_line = expanded_line.replace(param, arg)
                    expanded_code.append(expanded_line)
            else:
                expanded_code.append(line)  
        else:
            expanded_code.append(line)

    return expanded_code

source_code = [
    "MACRO ADD &X, &Y",  # Macro definition with name
    "LOAD &X",
    "ADD &Y",
    "STORE &X",
    "MEND",
    "START",
    "ADD A, B",  # Macro call
    "END"
]


mnt, mdt = pass_one(source_code)
expanded_code = pass_two(source_code, mnt, mdt)
print("MNT:", mnt)
print("MDT:", mdt)
print("Expanded Code:", expanded_code)