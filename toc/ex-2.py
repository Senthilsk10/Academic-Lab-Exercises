import re

# Define token patterns and their corresponding types and addresses
token_patterns = [
    (r'\s+', None, None),  # Whitespace (ignored)
    (r'[a-zA-Z_][a-zA-Z_0-9]*', 'VARIABLE', '<1,#address>'),
    (r'[0-9]+', 'NUMBER', '<2,#address>'),
    (r';', 'SEMICOLON', '<3,3>'),
    (r'=', 'ASSIGN', '<4,4>'),
    (r'\+', 'PLUS', '<43,43>'),
    (r'\+=', 'PLUSEQ', '<430,430>'),
    (r'-', 'MINUS', '<45,45>'),
    (r'-=', 'MINUSEQ', '<450,450>'),
    (r'\*', 'MULT', '<42,42>'),
    (r'\*=', 'MULTEQ', '<420,420>'),
    (r'/', 'DIV', '<47,47>'),
    (r'/=', 'DIVEQ', '<470,470>'),
    (r'%', 'MOD', '<37,37>'),
    (r'%=', 'MODEQ', '<370,370>'),
    (r'\^', 'XOR', '<94,94>'),
    (r'\^=', 'XOREQ', '<940,940>')
]

# Compile the token patterns into regex objects
token_regex = [(re.compile(pattern), token_type, address) for pattern, token_type, address in token_patterns]

def lex(input_string):
    position = 0
    tokens = []

    while position < len(input_string):
        match = None
        for token_re, token_type, address in token_regex:
            match = token_re.match(input_string, position)
            if match:
                if token_type:  # If not a whitespace
                    token = match.group(0)
                    if token_type == 'VARIABLE':
                        address = address.replace('#address', hex(id(token)))
                    elif token_type == 'NUMBER':
                        address = address.replace('#address', token)
                    tokens.append((token_type, token, address))
                break
        if not match:
            raise SyntaxError(f"Illegal character: {input_string[position]}")
        else:
            position = match.end(0)

    return tokens


input_string = "x = 10 + y;"
tokens = lex(input_string)
for token in tokens:
    token_type, value, address = token
    print(f"{value} {address}")
