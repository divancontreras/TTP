import heapq
class Grupo():
    def __init__(self, grupo_vacas):
        self.grupo_vacas = grupo_vacas.split()
        self.grupo_vacas.sort()
        self.repeticiones = 0

    def check_group(self, grupo_vacas):
        grupo_vacas = grupo_vacas.split()
        grupo_vacas.sort()
        for x in range(3):
            if not self.grupo_vacas[x] == grupo_vacas[x]:
                return False
        self.repeticiones += 1
        return True

list = []

try:
    numero_horas = raw_input()
    for i in range(int(numero_horas)):
        grupo_vacas = raw_input()
        if(len(list) == 0):
            first_group = Grupo(grupo_vacas)
            first_group.repeticiones = 1
            list.append(first_group)
        else:
            found = False
            for group in list:
                if group.check_group(grupo_vacas):
                    found = True
                    break
            if not found:
                new_group = Grupo(grupo_vacas)
                new_group.repeticiones = 1
                list.append(new_group)
    highest = 0
    for x in list:
        if x.repeticiones > highest:
            highest = x.repeticiones
    print(highest)
except EOFError:
    exit