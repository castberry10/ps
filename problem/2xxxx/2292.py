data = int(input())
set_ = 1

for i in range(1000000000):
    if data == 1:
        print(1)
        break
    if data <= set_:
        print(i)
        break
    set_ += 6 * i