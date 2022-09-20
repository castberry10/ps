a = []
b = []
a = map(int, input().split())
b = map(int, input().split())
suma = 0
sumb= 0

for i in a:
    suma += i
for i in b:
    sumb += i
if suma >= sumb:
    print(suma)
else:
    print(sumb)