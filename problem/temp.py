n = int(input())
s = input()
a = 0
for i in s:
    if i == "a" or i == "o" or i == "e" or i == "i" or i == "u":
        a += 1
print(a)