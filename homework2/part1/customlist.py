from copy import copy


class CustomList(list):

    def __init__(self, obj = None):
        if obj != None:
            super().__init__(obj)
        else:
            super().__init__()
        
    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return self < other or self == other

    def __gt__(self, other):
        return sum(self) > sum(other)
    
    def __ge__(self, other):
        return self > other or self == other
    
    def __eq__(self, other):
        return sum(self) == sum(other)

    def __add__(self, other):
        res = CustomList(copy(self))
        tmp = copy(other)
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
        res = CustomList(copy(self))
        tmp = copy(other)
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
        res = CustomList(copy(self))
        tmp = copy(other)
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
        res = CustomList(copy(self))
        tmp = copy(other)
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
