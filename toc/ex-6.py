class ProductionRule:
    def __init__(self, left, right):
        self.left = left
        self.right = right
    
rules = [
    ProductionRule('E', 'E+E'),
    ProductionRule('E', 'E/E'),
    ProductionRule('E', 'E*E'),
    ProductionRule('E', 'a'),
    ProductionRule('E', 'b')
]
stack = ""
input_string = input("\nEnter the input string: ").strip()
i = 0
while True:

    if i < len(input_string):
        ch = input_string[i]
        i += 1
        stack += ch
        print(f"{stack}\t{input_string[i:]}\tShift {ch}")
    reduction_made = False
    for rule in rules:
        while rule.right in stack:
            stack = stack.replace(rule.right, rule.left, 1)
            print(f"{stack}\t{input_string[i:]}\tReduce {rule.left}->{rule.right}")
            reduction_made = True
    if not reduction_made:
        if stack == rules[0].left and i == len(input_string):
            print("\nAccepted")
            break
        if i == len(input_string):
            print("\nNot Accepted")
            break


