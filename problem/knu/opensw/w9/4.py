class LoveArrow():
    def __init__(self):
        self.arrows = {}

    def add_arrow(self, name, arrow):
        self.arrows[name] = arrow
    
    def get_couples(self):
        answer = set()
        for i in self.arrows:
            v = self.arrows[i]
            if v in self.arrows and self.arrows[v] == i:
                a = [i, v]
                a.sort()
                answer.add((a[0], a[1]))
        answer = list(answer)
        return answer
    
la = LoveArrow()
la.add_arrow('a', 'b')
la.add_arrow('b', 'c')
la.add_arrow('c', 'b')
print(la.get_couples())