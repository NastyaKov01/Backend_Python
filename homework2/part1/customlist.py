"""CustomList class description"""
from copy import copy


class CustomList(list):
    """List class that allows to add and subtract list elementwise"""

    def __init__(self, obj=None):
        if obj is not None:
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
        for i, _ in enumerate(res):
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
        for i, _ in enumerate(res):
            res[i] -= tmp[i]
        return res

    def __radd__(self, other):
        res = CustomList(copy(other))
        tmp = copy(self)
        dif = len(res) - len(tmp)
        if dif < 0:
            for i in range(-dif):
                res.append(0)
        elif dif > 0:
            for i in range(dif):
                tmp.append(0)
        for i, _ in enumerate(res):
            res[i] += tmp[i]
        return res

    def __rsub__(self, other):
        res = CustomList(copy(other))
        tmp = copy(self)
        dif = len(res) - len(tmp)
        if dif < 0:
            for i in range(-dif):
                res.append(0)
        elif dif > 0:
            for i in range(dif):
                tmp.append(0)
        for i, _ in enumerate(res):
            res[i] -= tmp[i]
        return res
