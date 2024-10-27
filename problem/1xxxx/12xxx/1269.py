n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

ab = a - b
ba = b - a
aba = ab | ba

print(len(aba))
