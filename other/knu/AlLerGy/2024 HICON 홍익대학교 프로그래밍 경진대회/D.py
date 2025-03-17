import re
import sys

input = sys.stdin.readline

MOD = 10**9 + 7

t = int(input().strip())
for _ in range(t):
    data = input().strip()
    
    vowel_count = sum(ch in 'aoieu' for ch in data)
    if vowel_count == 0:
        print(-1)
        continue
    tokens = re.split('[aoeiu]', data)
    
    middle_chunks = tokens[1:-1]
    
    ways = 1
    for chunk in middle_chunks:
        ways = (ways * (len(chunk) + 1)) % MOD
    
    print(ways % MOD)
