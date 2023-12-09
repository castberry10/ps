import numpy
dataset = set()

a, b = 0, 0
while True:
    while True:
        c = numpy.random.randint(1, 10001)
        if c in dataset:
            pass
        else:
            break
    print('? A', c, flush=True)
    resp = int(input())
    if resp == 1:
        a = c
        break
    else:
        dataset.add(c)
dataset = set()
while True:
    while True:
        c = numpy.random.randint(1, 10001)
        if c in dataset:
            pass
        else:
            break
    print('? B', c, flush=True)
    resp = int(input())
    if resp == 1:
        b = c
        break
    else:
        dataset.add(c)
print('!', a + b)