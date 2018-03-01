def is_subsequence(subsequence, encrypted):
    word = ""
    for x in subsequence:
        for i, y in enumerate(encrypted):
            if x == y:
                word += x
                encrypted = encrypted[i+1:]
                break
    if subsequence == word:
        return True
    else:
        return False

try:
    while True:
        entry = raw_input()
        if len(entry.split()) == 2:
            if is_subsequence(entry.split()[0], entry.split()[1]):
                print("Yes")
            else:
                print("No")
        else:
            pass
except EOFError:
    exit()