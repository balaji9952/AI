def is_valid(assignment, var, value, constraints):
    for (a, b) in constraints:
        if b == var and a in assignment and assignment[a] == value:
            return False
        if a == var and b in assignment and assignment[b] == value:
            return False
    return True

def backtrack(variables, domains, constraints, assignment):
    if len(assignment) == len(variables):
        return assignment
    var = [v for v in variables if v not in assignment][0]
    for value in domains[var]:
        if is_valid(assignment, var, value, constraints):
            assignment[var] = value
            result = backtrack(variables, domains, constraints, assignment)
            if result:
                return result
            del assignment[var]
    return None

variables = ['A', 'B', 'C']
domains = {'A': [1, 2, 3], 'B': [1, 2, 3], 'C': [1, 2, 3]}
constraints = [('A', 'B'), ('B', 'C'), ('A', 'C')]
solution = backtrack(variables, domains, constraints, {})
print("Solution:", solution)
