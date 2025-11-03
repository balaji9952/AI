from queue import PriorityQueue

def a_star(start, goal, graph, h):
    open_set = PriorityQueue()
    open_set.put((0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]
    while not open_set.empty():
        current = open_set.get()[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        for neighbor, cost in graph[current]:
            temp_g = g_score[current] + cost
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + h[neighbor]
                open_set.put((f_score[neighbor], neighbor))
    return None

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 2, 'F': 1, 'G': 0}
path = a_star('A', 'G', graph, h)
print("Path:", path)
