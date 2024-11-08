class Production:
    def __init__(self,left,right):
        self.right = right
        self.left = left
        
rules = [
    Production('E', 'E+E'),
    Production('E', '(E)'),
    Production('E', 'E/E'),
    Production('E', 'E*E'),
    Production('E', 'a'),
    Production('E', 'b')
]

expression = 'a+b*(b*a)'
stack = ''
i = 0
while True:
    if i < len(expression):
        ch = expression[i]
        stack += ch
        i+=1
        print(f'{stack}\t {expression[i:]} shift')
        
    reduction_made = False
    for rule in rules:
        if rule.right in stack:
            stack = stack.replace(rule.right,rule.left)
            print(f'{stack}\t {expression[i:]} reduce')
            reduction_made = True
            break
            
        
    if not reduction_made:
        if i==len(expression) and stack==rules[0].left:
            print('accepted')
            break
        if i==len(expression):
            print('not accepted')
        
