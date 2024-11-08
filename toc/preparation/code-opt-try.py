class Operation:
    def __init__(self,left,right):
        self.left =left
        self.right = right
        
def print_ops(ops,title):
    print(title)
    for op in ops:
        print(f"{op.left} = {op.right}")
n = int(input("enter number of expression : "))
ops = [Operation(input("enter left side: "),input("enter right side: ")) for _ in range(n)]

print_ops(ops,"inter")

# dead code elimination
pr = []
for i in range(n-1):
    temp = ops[i].left
    if any(temp in op.right for op in ops):# if the vairable doesnot needed in other expression or right side
        pr.append(Operation(ops[i].left,ops[i].right))

pr.append(ops[-1])
print_ops(pr,'dead code')

#sub expression elimination

sub = {} #store previous expression for matching
opt = [] #store final result

for op in pr:
    temp = op.right
    if temp in sub:# if right expression in map then assign key
        opt.append(Operation(op.left,sub[temp]))
    else:#else assign as usual
        sub[temp] = op.left
        opt.append(op)

print_ops(opt,"optimized")