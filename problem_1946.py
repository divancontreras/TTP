CONST_PARALLELOGRAM = [[False, True, True],
                       [True, True, True],
                       [True, True, False]]

def check_blocked(x,y):
    global flag_blocked
    try:
        if (type(aux_mat[x][y - 1]) == int and type(aux_mat[x + 1][y - 1]) == int):
            flag_blocked = True
            return True
    except:
        pass
    try:
        if (type(aux_mat[x + 1][y]) == int and (type(aux_mat[x + 1][y - 1])) == int):
            flag_blocked = True
            return True
    except:
        pass
    try:
        if (type(aux_mat[x - 1][y]) == int and type(aux_mat[x - 1][y + 1]) == int):
            flag_blocked = True
            return True
    except:
        pass
    try:
        if (type(aux_mat[x][y + 1]) == int and (type(aux_mat[x - 1][y + 1])) == int):
            flag_blocked = True
            return True
    except:
        pass


def check_adjacent(x, y, prev_val, new = False):
    global flag_blocked
    count_adjacent = 0
    # if not checked[x][y] and aux_mat[x][y] == 2 and not new:
    #     flag_blocked = True
    #     return
    if not(checked[x][y]) or new:
        checked[x][y] = True
        if type(aux_mat[x][y]) == int:
            aux_mat[x][y] = prev_val
        if prev_val == 1 :
            prev_val = 2
        elif prev_val == 2 :
            prev_val = 1
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                try:
                    if CONST_PARALLELOGRAM[x-i][y-j]:
                        if (i >= 0 and i < len(aux_mat)) and (j >= 0 and j < len(aux_mat[0]) and grid[i][j] != "."):
                            count_adjacent += 1
                            if count_adjacent == 2:
                                if len(grid) > 1:
                                    if check_blocked(x,y):
                                        return
                                else:
                                    if type(aux_mat[x][y-1]) == int and type(aux_mat[x][y+1]) == int:
                                        pass
                                    else:
                                        flag_blocked = True
                                        pass
                            elif count_adjacent >2:
                                flag_blocked = True
                                return
                            if aux_mat[x][y] == 2 and aux_mat[i][j] == 2:
                                flag_blocked = True
                            check_adjacent(i, j, prev_val)
                except:
                    pass

def set_blocked(x,y):
    global flag_blocked
    aux_mat[x][y] = 3
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            try:
                if CONST_PARALLELOGRAM[x - i][y - j]:
                    if (i >= 0 and i < len(aux_mat)) and (j >= 0 and j < len(aux_mat[0]) and grid[i][j] != "."):
                        if type(aux_mat[i][j]) == int and aux_mat[i][j] < 3:
                                set_blocked(i, j)
            except:
                pass

    flag_blocked = False

def create_aux():
    global checked
    global aux_mat
    checked = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
    aux_mat = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
    for x in range(len(checked)):
        for y in range(len(checked[x])):
            checked[x][y] = False
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == ".":
                aux_mat[x][y] = "."
            elif grid[x][y] == "*":
                aux_mat[x][y] = 0
            elif grid[x][y] == "I":
                aux_mat[x][y] = 2


def convert():
    for x in range(len(aux_mat)):
        for y in range(len(aux_mat[x])):
            if aux_mat[x][y] == 0:
                aux_mat[x][y] = "F"
            elif aux_mat[x][y] == 1:
                aux_mat[x][y] = ")"
            elif aux_mat[x][y] == 2:
                aux_mat[x][y] = "("
            elif aux_mat[x][y] == 3:
                aux_mat[x][y] = "B"
try:
    while True:
        checked = []
        flag_blocked = False
        aux_mat = []
        entry = str(raw_input()).split()
        if len(entry) > 0:
            R = int(entry[0])
            C = int(entry[1])
            if R < 1:
                exit()
            if C >= 0:
                grid = []
                for x in range(R):
                    grid.append(list(raw_input()[:C]))
                create_aux()
                for x in range(R):
                    for y in range(C):
                            flag_blocked = False
                            if grid[x][y] == "I" and aux_mat[x][y] != 3:
                                check_adjacent(x, y, 2, True)
                                if flag_blocked:
                                    set_blocked(x, y)
                convert()
                print("")
                print('\n'.join([''.join(['{:1}'.format(item) for item in row])
                                 for row in aux_mat]))
            else:
                exit()
except EOFError:
    exit()