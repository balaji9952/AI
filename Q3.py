import itertools

def solve():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)
    for perm in itertools.permutations(digits, len(letters)):
        s, e, n, d, m, o, r, y = perm
        if s == 0 or m == 0:
            continue
        send = s * 1000 + e * 100 + n * 10 + d
        more = m * 1000 + o * 100 + r * 10 + e
        money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
        if send + more == money:
            return send, more, money
    return None

res = solve()
if res:
    print("SEND:", res[0])
    print("MORE:", res[1])
    print("MONEY:", res[2])
else:
    print("No solution")
