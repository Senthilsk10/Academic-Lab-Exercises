import re

# Define token patterns and their corresponding types and addresses
token_patterns = [
    (r'\s+', None, None),  # Whitespace (ignored)
    (r'if', 'IF', '<1,1>'),
    (r'[a-zA-Z_][a-zA-Z_0-9]*', 'VARIABLE', '<2,#address>'),
    (r'[0-9]+', 'NUMBER', '<3,#address>'),
    (r';', 'SEMICOLON', '<4,4>'),
    (r'\(', 'LPAREN', '<5,0>'),
    (r'\)', 'RPAREN', '<5,1>'),
    (r'\{', 'LBRACE', '<6,0>'),
    (r'\}', 'RBRACE', '<6,1>'),
    (r'>=', 'GTE', '<620,620>'),
    (r'>', 'GT', '<62,62>'),
    (r'<=', 'LTE', '<600,600>'),
    (r'<', 'LT', '<60,60>'),
    (r'!=', 'NEQ', '<330,330>'),
    (r'!', 'NOT', '<33,33>'),
    (r'==', 'EQ', '<610,610>'),
    (r'=', 'ASSIGN', '<61,61>'),
]

# Compile the token patterns into regex objects
token_regex = [(re.compile(pattern), token_type, address) for pattern, token_type, address in token_patterns]
# print(token_regex)
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

# Example usage
#input_string = "if (x >= 10) { y = 20; }"
input_string = input("enter the input string")

tokens = lex(input_string)
for token in tokens:
    token_type, value, address = token
    print(f"{value} {address}")
