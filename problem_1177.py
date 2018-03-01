try:
    while True:
        entry = raw_input()
        if len(entry) > 0:
            if entry == '0':
                exit()
            if entry.split()[0] == '0':
                exit()
            divisor = int(entry.split()[0])
            string = entry.split()[1]
            answer = ""
            dividendo = len(string) / divisor
            while len(string) > 0:
                aux = string[:dividendo][::-1]
                answer += aux
                string = string[dividendo:]
            print(answer)
except EOFError:
    exit()