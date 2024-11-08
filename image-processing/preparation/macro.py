source_code = [
    "MACRO ADD &X,&Y",
    "LOAD &X",
    "ADD &Y",
    "STORE &X",
    "MEND",
    "START",
    "ADD A,B",
    "MACRO SUB $X,$Y",
    "LOAD &X",
    "SUB &Y",
    "STORE &X",
    "END"
]

mnt = {}
mdt = []
macro =False

def process(source):
    for line in source:
        parts = line.split()
        if parts[0] == 'MACRO':
            mnt[parts[1]] = len(mdt)
            macro = True
            mdt.append((parts[1],parts[2]))
            continue
        elif parts[0] == 'MEND':
            macro =False
        elif macro:
            mdt.append(line)
            
            
process(source_code)
print(mdt)
print(mnt)

