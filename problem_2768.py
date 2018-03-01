res = []
while True:
    number = int(raw_input())
    if number == 0:
        for x in res:
            print(x)
        exit()
    else:
        res.append(str(((2**(number+1))-1) % 1000000007))