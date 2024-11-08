# E  -> T E'
# E' -> + T E'/ε
# T  -> F T'
# T' -> * F T'/ε
# F  -> (E)/id

ptr = 0
expression = input('enter a expression : ')

def advance():
    global ptr 
    ptr += 1
    
def e():
    print("E  -> T E'")
    t()
    e_prime()
    
def t():
    print("T  -> F T'")
    f()
    t_prime()
    
def f():
    if ptr<len(expression) and expression[ptr] in ('i','j'):
        print("F  -> id")
        advance()
    else:
        print('invalid syntax')
        exit(1)
        
def t_prime():
    if ptr<len(expression) and expression[ptr]=='*':
        print("T' -> * F T'")
        advance()
        f()
        t_prime()
    else:
        print("T' -> ε")

def e_prime():
    if ptr<len(expression) and expression[ptr]=='+':
        print("E' -> + T E'")
        advance()
        t()
        e_prime()
    else:
        print("E' -> ε")

e()