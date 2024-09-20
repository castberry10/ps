n = int(input())
data = dict()

data['Algorithm'] = '204'
data['DataAnalysis'] = '207'
data['ArtificialIntelligence'] = '302'
data['CyberSecurity'] = 'B101'
data['Network'] = '303'
data['Startup'] = '501'
data['TestStrategy'] = '105'

for i in range(n):
    a = input()
    print(data[a])