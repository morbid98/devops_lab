n, m = input().split()
# n=number of integers to check
# m=number of integers in A and B
inp = input().split()
A = input().split()
B = input().split()
happiness = len(set(A) & set(inp))
happiness -= len(set(B) & set(inp))
print(happiness)
