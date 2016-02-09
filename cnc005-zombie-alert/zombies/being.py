from random import randrange, choice


def change_loc(cur, max_loc):
    if cur == 0:
        return 1
    elif cur + 1 == max_loc:
        return cur - 1
    else:
        return choice([cur + 1, cur -1])

def is_next_to(x, y):
    return abs(x - y) < 2

class Being:
    def __init__(self, max_location):
        self.identity = "H"
        self._max_location = max_location
        self._x = -1
        self._y = -1

    @property
    def max_location(self):
        return self._max_location

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def reveal(self):
        return self.identity

    def zombify(self):
        self.identity = "Z"

    def locate(self):
        self._x = randrange(0, self._max_location)
        self._y = randrange(0, self._max_location)

    def move(self):
        pick = choice([0,1])
        if pick == 0:
            self._x = change_loc(self._x, self.max_location)
        else:
            self._y = change_loc(self._y, self.max_location)

    def move_toward(self, targets):
        target = self.close(targets)

        if target != (-1,-1):
            self.set_at(target[0], target[1])
        else:
            self.move()

    def at(self, x, y):
        return self._x == x and self._y == y

    def set_at(self, x, y):
        self._x = x
        self._y = y

    def close(self, beings):
        for being in beings:
            if (being.x == self._x and is_next_to(being.y, self._y)) or (being.y == self._y and is_next_to(being.x, self._x)):
                return (being.x, being.y)
        return (-1, -1)

