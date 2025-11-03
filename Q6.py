def fits(word, slot):
    if len(word) != len(slot):
        return False
    for w, s in zip(word, slot):
        if s != '_' and s != w:
            return False
    return True

def csp_crossword(words, slots):
    assignment = {}
    for i, slot in enumerate(slots):
        for word in words:
            if fits(word, slot):
                assignment[f"Slot{i+1}"] = word
                words.remove(word)
                break
    return assignment

words = ["CAT", "DOG", "BAT", "RAT", "COW"]
slots = ["C_T", "D_G", "_AT"]
solution = csp_crossword(words, slots)
print("Crossword Solution:", solution)
