from collections import deque

def is_solvable(state):
    inv = 0
    nums = [int(i) for i in state if i != '0']
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                inv += 1
    return inv % 2 == 0

def bfs(start, goal):
    moves = {'0': [(1, 3)], '1': [(0, 2, 4)], '2': [(1, 5)], '3': [(0, 4, 6)], '4': [(1, 3, 5, 7)], '5': [(2, 4, 8)], '6': [(3, 7)], '7': [(4, 6, 8)], '8': [(5, 7)]}
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        state, depth = queue.popleft()
        if state == goal:
            return depth
        pos = state.index('0')
        for move in moves[str(pos)][0]:
            new_state = list(state)
            new_state[pos], new_state[move] = new_state[move], new_state[pos]
            new_state = ''.join(new_state)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, depth + 1))
    return -1

start = "724506831"
goal = "123456780"
if is_solvable(start):
    print("Minimum steps:", bfs(start, goal))
else:
    print("This puzzle is not solvable")
