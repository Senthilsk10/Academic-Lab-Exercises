import re

def is_alpha_or_digit_or_special(c):
    return c.isalnum() or c in ['[', ']', '.']

def process_file(input_file, intermediate_file, oper_file, key_file):
    # Read input file
    with open(input_file, "r") as fi:
        content = fi.read()
    
    # Process input file to intermediate file
    with open(intermediate_file, "w") as fo:
        for c in content:
            if is_alpha_or_digit_or_special(c):
                fo.write(c)
            else:
                if c == '\n':
                    fo.write("\n\t$\t")
                else:
                    fo.write(f"\n\t{c}\t")
    
    # Read files for further processing
    with open(intermediate_file, "r") as fi, \
         open(oper_file, "r") as fop, \
         open(key_file, "r") as fk:
        
        fop_dict = {}
        for line in fop:
            parts = line.split()
            if len(parts) == 2:
                fop_dict[parts[0]] = parts[1]

        fk_set = set()
        for line in fk:
            parts = line.split()
            if len(parts) > 0:
                fk_set.add(parts[0])
        
        print("\n Lexical Analysis")
        i = 1
        print(f"\n Line: {i}\n")
        i += 1
        
        tokenlist = [] #
        for line in fi:
            tokens = re.split(r'\s+', line.strip())
            tokenlist.append(tokens)
            for token in tokens:
                if token == "$":
                    print(f"\n Line: {i}\n")
                    i += 1
                elif token in fop_dict:
                    print(f"\t{token} : {fop_dict[token]}")
                elif token in fk_set:
                    print(f"\t{token} : Keyword")
                else:
                    if token.isdigit():
                        print(f"\t{token} : Constant")
                    else:
                        print(f"\t{token} : Identifier")
        #print(tokenlist)
# Define file names
input_file = "input.c"
intermediate_file = "inter-py.c"
oper_file = "oper.c"
key_file = "key.c"

# Process the file
process_file(input_file, intermediate_file, oper_file, key_file)
