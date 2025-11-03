from queue import PriorityQueue

def memory_bounded_a_star(graph, start, goal, h):
    open_set = PriorityQueue()
    open_set.put((h[start], start))
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    while not open_set.empty():
        _, current = open_set.get()
        if current == goal:
            return g_score[current]
        for neighbor, cost in graph[current]:
            temp_g = g_score[current] + cost
            if temp_g < g_score.get(neighbor, float('inf')):
                g_score[neighbor] = temp_g
                open_set.put((temp_g + h[neighbor], neighbor))
    return None

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 4), ('E', 2)],
    'C': [('F', 5)],
    'D': [('G', 1)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 2, 'F': 1, 'G': 0}
cost = memory_bounded_a_star(graph, 'A', 'G', h)
print("Best Path Cost:", cost)
