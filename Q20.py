from collections import deque

def is_goal(state):
    return state == "123804765"

def get_moves(state):
    i = state.index("0")
    moves = []
    r, c = divmod(i, 3)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            ni = nr * 3 + nc
            new_state = list(state)
            new_state[i], new_state[ni] = new_state[ni], new_state[i]
            moves.append("".join(new_state))
    return moves

def bfs(start):
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        state, steps = queue.popleft()
        if is_goal(state):
            return steps
        for next_state in get_moves(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, steps + 1))
    return -1

start = "123405678"
steps = bfs(start)
print("Minimum Steps Required:", steps)
