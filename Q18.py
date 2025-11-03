def backward_chaining(KB, query):
    if query in KB:
        return True
    for rule in KB:
        if query in KB[rule]:
            if all(backward_chaining(KB, premise) for premise in rule):
                return True
    return False

KB = {
    ('Rain',): ['WetGrass'],
    ('Sprinkler',): ['WetGrass'],
    ('WetGrass',): ['Slippery']
}

query = 'Slippery'
print("Result:", backward_chaining(KB, query))
