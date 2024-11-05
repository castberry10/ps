class NumberSet():
    def __init__(self):
        self.numbers = []
    
    def add_number(self, number):
        self.numbers.append(number)

    def get_pairs(self):
        pairs = []
        for i in range(len(self.numbers)):
            for j in range(i+1, len(self.numbers)):
                pairs.append((self.numbers[i], self.numbers[j])) 
        return pairs
a = NumberSet()
a.add_number(1)
a.add_number(2)
a.add_number(3)
a.add_number(4)
a.add_number(5)
print(a.get_pairs())