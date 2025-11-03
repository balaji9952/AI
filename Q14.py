def wumpus_model_checking(kb, query):
    for symbol in kb:
        if symbol == query and kb[symbol]:
            return True
    return False

kb = {
    "B11": True,
    "P12": True,
    "W13": False,
    "B21": True,
    "P22": False,
    "W23": True
}

query = "W23"
result = wumpus_model_checking(kb, query)
print("Wumpus Present:", result)
