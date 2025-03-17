def intToFizz(i):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
tof = False

for n in range(3):
    i = input()
    if not tof and i not in ("Fizz", "Buzz", "FizzBuzz"):

        intToFizz(int(i) + (3-n))
        tof = True