def forward_chaining(KB, facts, query):
    inferred = set()
    while True:
        new_inferred = set()
        for rule in KB:
            premises, conclusion = rule
            if all(p in facts for p in premises) and conclusion not in facts:
                new_inferred.add(conclusion)
        if not new_inferred:
            break
        facts |= new_inferred
        inferred |= new_inferred
    return query in facts

KB = [
    ({"A", "B"}, "C"),
    ({"C"}, "D"),
    ({"D"}, "E")
]
facts = {"A", "B"}
query = "E"
print(forward_chaining(KB, facts, query))

def resolution(clause1, clause2):
    for literal in clause1:
        if f"~{literal}" in clause2 or (literal[1:] if literal.startswith("~") else f"~{literal}") in clause2:
            return (clause1 | clause2) - {literal, f"~{literal}"}
    return None

c1 = {"A", "B"}
c2 = {"~A", "C"}
print(resolution(c1, c2))
