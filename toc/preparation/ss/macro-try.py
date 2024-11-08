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
expanded_code = []

def process_macro(lines):
    mac_def = False
    for line in lines:
        tokens = line.split()
        
        if tokens[0] == 'MACRO':
            mnt[tokens[1]] = len(mdt)
            mdt.append((tokens[1],tokens[2].split(',')))
            mac_def = True
        elif tokens[0] == 'MEND':
            mac_def = False
        elif mac_def:
            mdt.append(line)
        elif tokens[0] in mnt:
            index = mnt[tokens[0]]
            params = tokens[1].split(',')
            expand_macro(index,params)
        else:
            expanded_code.append(line)
            
    print(mnt,mdt)
    print('expanded: ',expanded_code)
            
def expand_macro(index,params):
    macro_name,m_params = mdt[index]
    param_map = {m_params[i] : params[i] for i in range(len(params))}

    # print(param_map)
    for i in range(index+1, len(mdt)):
        line = mdt[i]
        if line.startswith('MACRO') or line.startswith('MEND'):
            continue
        for param,args in param_map.items():
            print('line: ',line)
            print('param',param,'args',args)
            line = line.replace(param,args)
            print('replaced',line)
        expanded_code.append(line)
    
    # print(expanded_code)
    
    
process_macro(source_code)            