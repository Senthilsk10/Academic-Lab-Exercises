ip_ptr = 0

def advance():
    global ip_ptr
    ip_ptr += 1

def e():
    print("\n\tE  -> T E'")
    t()
    e_prime()

def e_prime():
    if ip_ptr < len(input_string) and input_string[ip_ptr] == '+':
        print("\n\tE' -> + T E'")
        advance()
        t()
        e_prime()
    else:
        print("\n\tE' -> ε")

def t():
    print("\n\tT  -> F T'")
    f()
    t_prime()

def t_prime():
    if ip_ptr < len(input_string) and input_string[ip_ptr] == '*':
        print("\n\tT' -> * F T'")
        advance()
        f()
        t_prime()
    else:
        print("\n\tT' -> ε")

def f():
    if ip_ptr < len(input_string) and input_string[ip_ptr] in ('i', 'j'):
        print("\n\tF  -> id")
        advance()
    elif ip_ptr < len(input_string) and input_string[ip_ptr] == '(':
        advance()
        e()
        if ip_ptr < len(input_string) and input_string[ip_ptr] == ')':
            advance()
            print("\n\tF  -> (E)")
        else:
            print("\n\tSyntax Error: Missing ')'")
            exit(1)
    else:
        print("\n\tSyntax Error: Invalid symbol in F")
        exit(1)

print("\n\tGRAMMAR WITHOUT RECURSION")
print("\n\tE  -> T E'\n\tE' -> + T E'/ε\n\tT  -> F T'\n\tT' -> * F T'/ε\n\tF  -> (E)/id")
input_string = input("\n\tEnter the Input Symbol: ")

print("\n\tSequence of Production Rules")
e()
