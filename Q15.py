def minimax(depth, node_index, is_max, scores, h):
    if depth == h:
        return scores[node_index]
    if is_max:
        return max(minimax(depth + 1, node_index * 2, False, scores, h),
                   minimax(depth + 1, node_index * 2 + 1, False, scores, h))
    else:
        return min(minimax(depth + 1, node_index * 2, True, scores, h),
                   minimax(depth + 1, node_index * 2 + 1, True, scores, h))

import math
scores = [3, 5, 6, 9, 1, 2, 0, -1]
h = math.log(len(scores), 2)
best_score = minimax(0, 0, True, scores, int(h))
print("The Optimal Value is:", best_score)
