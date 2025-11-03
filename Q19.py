import itertools

letters = ('B', 'A', 'S', 'E', 'L', 'G', 'M')
for perm in itertools.permutations(range(10), len(letters)):
    assign = dict(zip(letters, perm))
    if assign['B'] == 0 or assign['G'] == 0:
        continue
    BASE = assign['B']*1000 + assign['A']*100 + assign['S']*10 + assign['E']
    BALL = assign['B']*1000 + assign['A']*100 + assign['L']*10 + assign['L']
    GAMES = assign['G']*10000 + assign['A']*1000 + assign['M']*100 + assign['E']*10 + assign['S']
    if BASE + BALL == GAMES:
        print("Solution Found:")
        print(assign)
        print(f"{BASE} + {BALL} = {GAMES}")
        break
