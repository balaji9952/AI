def is_valid_color(region, color, assignment, neighbors):
    for neighbor in neighbors[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(assignment, regions, colors, neighbors):
    if len(assignment) == len(regions):
        return assignment
    region = [r for r in regions if r not in assignment][0]
    for color in colors:
        if is_valid_color(region, color, assignment, neighbors):
            assignment[region] = color
            result = backtrack(assignment, regions, colors, neighbors)
            if result:
                return result
            del assignment[region]
    return None

regions = ['A', 'B', 'C', 'D']
neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
solution = backtrack({}, regions, colors, neighbors)
print("Map Coloring:", solution)
