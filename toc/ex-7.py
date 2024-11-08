class ProductionRule:
    def __init__(self, left, right):
        self.left = left
        self.right = right

rules = [
    ProductionRule('E', 'E+E'),
    ProductionRule('E', 'E-E'),
    ProductionRule('E', 'E*E'),
    ProductionRule('E', 'E/E'),
    ProductionRule('E', 'E^E'),
    ProductionRule('E', '(E)'),
    ProductionRule('E', 'i')
]

def apply_reduction(stack, rule):
    pos = stack.find(rule.right)
    if pos != -1:
        return stack[:pos] + rule.left + stack[pos + len(rule.right):]
    return stack

def parse_expression(expression):
    stack = ""
    expression += '$'  
    i = 0
    while True:
        if i < len(expression):
            stack += expression[i]
            print(f"{stack}\t{expression[i+1:]}\tShift {expression[i]}")
            i += 1

        reduction_made = False
        for rule in reversed(rules):
            new_stack = apply_reduction(stack, rule)
            while new_stack != stack:  
                stack = new_stack
                print(f"{stack}\t{expression[i:]}\tReduce {rule.left}->{rule.right}")
                reduction_made = True
                new_stack = apply_reduction(stack, rule)  

        if i == len(expression) - 1:
            if stack == 'E' and expression[i] == '$':
                print("\nAccepted")
                return
            else:
                print("\nRejected")
                return


input_string = input("\nEnter the Arithmetic Expression End with $: ").strip()
parse_expression(input_string)
