from robot import *


class LabyBug:
    """The laby bug
    solves the labyrinths in the game named [Laby](https://wiki.ubuntu.com/Edubuntu/AppGuides/laby) 
    import refers to this file: [robot.py](https://github.com/sgimenez/laby/blob/master/data/mods/python/lib/robot.py)
    """

    def __init__(self):
        self.orientations = {
            0: 'N',
            1: 'W',
            2: 'S',
            3: 'E'}
        self.inv_orientations = {v: k for k, v in list(
            self.orientations.items())}
        self.look_map = {
            0: 'void',
            1: 'wall',
            2: 'stone',
            3: 'web',
            4: 'exit'}
        self.inv_look_map = {v: k for k, v in list(self.look_map.items())}
        self.current_position = (0, 0)
        # at start, the bug face North
        self.current_orientation = self.inv_orientations['N']
        self.has_stone = False
        # grid keys are the coordinates (like current_position)
        self.grid = dict()  # for possible dict values see look_map
        # at start, the bug stands on void
        self.grid[self.current_position] = self.inv_look_map['void']
        self.visited = set()
        self.visited.add(self.current_position)
        self.escaped = False

    def get_state(self):
        result = 'current_position:' + str(self.current_position) + ';'
        result += 'current_orientation:' + str(self.current_orientation) + ';'
        result += 'has_stone:' + str(self.has_stone) + ';'
        result += 'escaped:' + str(self.escaped) + ';'
        result += 'grid:' + str(self.grid) + ';'
        result += 'visited:' + str(self.visited) + ';'
        return result

    def orientation_to_left(self, o):
        return (o + 1) % 4

    def orientation_to_right(self, o):
        return (o - 1) % 4

    def turn_left(self):
        left()
        self.current_orientation = self.orientation_to_left(
            self.current_orientation)

    def turn_right(self):
        right()
        self.current_orientation = self.orientation_to_right(
            self.current_orientation)

    # lr is left or right; fb is forward or backward
    def coords_diff_in_direction(self, lr, fb):
        assert ((lr == 0 and fb in (1, -1)) or (lr in (1, -1) and fb == 0))
        if self.current_orientation == 0:  # 'N'
            result = (fb, -1 * lr)
        elif self.current_orientation == 1:  # 'W'
            result = (-1 * lr, -1 * fb)
        elif self.current_orientation == 2:  # 'S'
            result = (-1 * fb, lr)
        elif self.current_orientation == 3:  # 'E'
            result = (lr, fb)
        return result

    def get_coords_diff(self, d):
        return tuple([sum(x) for x in zip(self.current_position, d)])

    def coords_forward(self):
        return self.get_coords_diff(self.coords_diff_in_direction(0, 1))

    def coords_backward(self):
        return self.get_coords_diff(self.coords_diff_in_direction(0, -1))

    def coords_left(self):
        return self.get_coords_diff(self.coords_diff_in_direction(1, 0))

    def coords_right(self):
        return self.get_coords_diff(self.coords_diff_in_direction(-1, 0))

    def no_need_peek(self):
        return (self.coords_forward() in list(self.grid.keys())
        and self.coords_backward() in list(self.grid.keys())
        and self.coords_left() in list(self.grid.keys())
        and self.coords_right() in list(self.grid.keys()))

    def init_to_grid(self, key):
        if not key in self.grid:
            self.grid[key] = look()

    def peek_around(self):
        if self.no_need_peek():
            return
        for i in range(4):
            self.init_to_grid(self.coords_forward())
            self.turn_left()

    def turn(self):
        self.peek_around()
        seen_forward = self.look_map[self.grid[self.coords_forward()]]
        seen_left = self.look_map[self.grid[self.coords_left()]]
        seen_right = self.look_map[self.grid[self.coords_right()]]
        seen_backward = self.look_map[self.grid[self.coords_backward()]]

        if (seen_forward == 'exit'):
            return
        elif (seen_left == 'exit'):
            self.turn_left()
            return
        elif (seen_right == 'exit'):
            self.turn_right()
            return
        elif (seen_backward == 'exit'):
            self.turn_left()
            self.turn_left()
            return
        elif ((seen_forward in ('void', 'stone')
            and not self.coords_forward() in self.visited)
        or (seen_forward == 'web' and self.has_stone)):
            return
        elif (seen_left in ('void', 'stone')
            and not self.coords_left() in self.visited) \
        or (seen_left == 'web' and self.has_stone):
            self.turn_left()
            return
        elif (seen_right in ('void', 'stone')
            and not self.coords_right() in self.visited) \
        or (seen_right == 'web' and self.has_stone):
            self.turn_right()
            return
        elif seen_forward in ('void', 'stone') \
        or (seen_forward == 'web' and self.has_stone):
            return
        elif seen_left in ('void', 'stone') \
        or (seen_left == 'web' and self.has_stone):
            self.turn_left()
            return
        elif seen_right in ('void', 'stone') \
        or (seen_right == 'web' and self.has_stone):
            self.turn_right()
            return
        elif (seen_backward in ('void', 'stone')) \
        or (seen_backward == 'web' and self.has_stone):
            self.turn_left()
            self.turn_left()
            return

    def handle_stone(self):
        self.turn_left()
        if self.grid[self.coords_forward()] == self.inv_look_map['void']:
            drop()
            self.grid[self.coords_forward()] = self.inv_look_map['stone']
            self.has_stone = False
            self.turn_right()
            return
        self.turn_right()
        self.turn_right()
        if self.grid[self.coords_forward()] == self.inv_look_map['void']:
            drop()
            self.grid[self.coords_forward()] = self.inv_look_map['stone']
            self.has_stone = False
            self.turn_left()
            return
        self.turn_right()
        if self.grid[self.coords_forward()] == self.inv_look_map['void']:
            drop()
            self.grid[self.coords_forward()] = self.inv_look_map['stone']
            self.has_stone = False
            self.turn_left()
            self.turn_left()
            return
        self.turn_left()
        self.turn_left()
        return

    def go(self):
        self.peek_around()
        seen = self.look_map[self.grid[self.coords_forward()]]
        if seen == 'exit':
            if self.has_stone:
                self.handle_stone()
            escape()
            self.escaped = 1
        if seen == 'void':
            forward()
            self.current_position = self.coords_forward()
            self.visited.add(self.current_position)
        elif seen == 'stone':
            if self.has_stone:
                self.handle_stone()
            take()
            self.grid[self.coords_forward()] = self.inv_look_map['void']
            self.has_stone = True
            self.go()
        elif seen == 'web':
            if self.has_stone:
                drop()
                take()
                self.grid[self.coords_forward()] = self.inv_look_map['void']
                self.go()


def solve():
    bug = LabyBug()
    while not bug.escaped:
        bug.turn()
        say('state after turn:' + bug.get_state())
        bug.go()
        say('state after go:' + bug.get_state())


solve()
