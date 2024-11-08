class Operation:
    def __init__(self, left, right):
        self.left = left
        self.right = right

# Input number of operations
n = int(input("Enter the Number of Values: "))

# Read operations
ops = [Operation(input("left: "), input("\tright: ")) for _ in range(n)]

# Print Intermediate Code
print("\nIntermediate Code")
for op in ops:
    print(f"{op.left} = {op.right}")

# Dead Code Elimination
pr = []
for i in range(n - 1):
    temp = ops[i].left
    if any(temp in op.right for op in ops):
        pr.append(Operation(ops[i].left, ops[i].right))

pr.append(Operation(ops[n - 1].left, ops[n - 1].right))

# Print after Dead Code Elimination
print("\nAfter Dead Code Elimination\n")
for op in pr:
    print(f"{op.left}\t= {op.right}")

# Common Subexpression Elimination
for m in range(len(pr)):
    tem = pr[m].right
    for j in range(m + 1, len(pr)):
        if pr[j].right in tem:
            t = pr[j].left
            pr[j].left = pr[m].left
            for i in range(len(pr)):
                if t in pr[i].right:
                    a = pr[i].right.index(t)
                    pr[i].right = pr[i].right[:a] + pr[m].left + pr[i].right[a + 1:]

# Print after Common Subexpression Elimination
print("\nEliminate Common Expression")
for op in pr:
    print(f"{op.left}\t= {op.right}")

optimized_pr = []
for i in range(len(pr)):
    if any(op.left == pr[i].left and op.right == pr[i].right for op in optimized_pr):
        continue
    optimized_pr.append(pr[i])

# Print Optimized Code
print("\nOptimized Code")
for op in optimized_pr:
    print(f"{op.left} = {op.right}")
