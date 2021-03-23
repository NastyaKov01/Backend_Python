from copy import deepcopy


class CustomList(list):

    def __init__(self, obj = None):
        if obj != None:
            super().__init__(obj)
        else:
            super().__init__()
        
    def __lt__(self, other):
        print(sum(self), sum(other))
        return sum(self) < sum(other)

    def __eq__(self, other):
        print(sum(self), sum(other))
        return sum(self) == sum(other)

    def __add__(self, other):
        res = CustomList(deepcopy(self))
        tmp = deepcopy(other)
        dif = len(self) - len(other)
        if dif < 0:
            for i in range(-dif):
                res.append(0)
        elif dif > 0:
            for i in range(dif):
                tmp.append(0)
        for i in range(len(res)):
            res[i] += tmp[i]
        return res

    def __sub__(self, other):
        res = CustomList(deepcopy(self))
        tmp = deepcopy(other)
        dif = len(self) - len(other)
        if dif < 0:
            for i in range(-dif):
                res.append(0)
        elif dif > 0:
            for i in range(dif):
                tmp.append(0)
        for i in range(len(res)):
            res[i] -= tmp[i]
        return res

    def __radd__(other, self):
        res = CustomList(deepcopy(self))
        tmp = deepcopy(other)
        dif = len(self) - len(other)
        if dif < 0:
            for i in range(-dif):
                res.append(0)
        elif dif > 0:
            for i in range(dif):
                tmp.append(0)
        for i in range(len(res)):
            res[i] += tmp[i]
        return res

    def __rsub__(other, self):
        res = CustomList(deepcopy(self))
        tmp = deepcopy(other)
        dif = len(self) - len(other)
        if dif < 0:
            for i in range(-dif):
                res.append(0)
        elif dif > 0:
            for i in range(dif):
                tmp.append(0)
        for i in range(len(res)):
            res[i] -= tmp[i]
        return res

