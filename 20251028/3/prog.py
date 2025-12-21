import sys

class Maze:
    def __init__(self, N):
        self.N = N
        self.horizontal_walls = set()
        self.vertical_walls = set()

        for x in range(N):
            for y in range(N):
                if x < N - 1:
                    self.horizontal_walls.add((x, y, x + 1, y))
                if y < N - 1:
                    self.vertical_walls.add((x, y, x, y + 1))

    def _get_walls_between(self, x0, y0, x1, y1):
        if x0 == x1 and abs(y0 - y1) == 1:
            y_min, y_max = min(y0, y1), max(y0, y1)
            return [(x0, y_min, x0, y_max)]
        elif y0 == y1 and abs(x0 - x1) == 1:
            x_min, x_max = min(x0, x1), max(x0, x1)
            return [(x_min, y0, x_max, y0)]
        return []

    def __setitem__(self, key, value):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]

        if x0 != x1 and y0 != y1:
            return

        dx = 1 if x1 > x0 else -1 if x1 < x0 else 0
        dy = 1 if y1 > y0 else -1 if y1 < y0 else 0

        x, y = x0, y0

        while (x != x1 or y != y1):
            next_x = x + dx if dx != 0 else x
            next_y = y + dy if dy != 0 else y

            walls = self._get_walls_between(x, y, next_x, next_y)

            for wall in walls:
                xa, ya, xb, yb = wall

                if xa == xb:
                    if value == "·":
                        if (xa, ya, xb, yb) in self.vertical_walls:
                            self.vertical_walls.remove((xa, ya, xb, yb))
                    elif value == "█":
                        if (xa, ya, xb, yb) not in self.vertical_walls:
                            self.vertical_walls.add((xa, ya, xb, yb))
                else:
                    if value == "·":
                        if (xa, ya, xb, yb) in self.horizontal_walls:
                            self.horizontal_walls.remove((xa, ya, xb, yb))
                    elif value == "█":
                        if (xa, ya, xb, yb) not in self.horizontal_walls:
                            self.horizontal_walls.add((xa, ya, xb, yb))

            x, y = next_x, next_y

    def __getitem__(self, key):
        x0, y0, x1, y1 = key[0], key[1].start, key[1].stop, key[2]

        visited = set()
        queue = [(x0, y0)]

        while queue:
            x, y = queue.pop(0)

            if (x, y) == (x1, y1):
                return True

            if (x, y) in visited:
                continue

            visited.add((x, y))

            if x > 0 and (x - 1, y, x, y) not in self.horizontal_walls:
                queue.append((x - 1, y))
            if x < self.N - 1 and (x, y, x + 1, y) not in self.horizontal_walls:
                queue.append((x + 1, y))
            if y > 0 and (x, y - 1, x, y) not in self.vertical_walls:
                queue.append((x, y - 1))
            if y < self.N - 1 and (x, y, x, y + 1) not in self.vertical_walls:
                queue.append((x, y + 1))

        return False

    def __str__(self):
        result = []

        result.append("█" * (2 * self.N + 1))

        for x in range(self.N):
            row = ["█"]
            for y in range(self.N):
                row.append("·")
                if y < self.N - 1:
                    if (x, y, x, y + 1) in self.vertical_walls:
                        row.append("█")
                    else:
                        row.append("·")

            row.append("█")
            result.append("".join(row))

            if x < self.N - 1:
                wall_row = ["█"]
                for y in range(self.N):
                    if (x, y, x + 1, y) in self.horizontal_walls:
                        wall_row.append("█")
                    else:
                        wall_row.append("·")
                    wall_row.append("█")

                wall_row[-1] = "█"
                result.append("".join(wall_row))

        result.append("█" * (2 * self.N + 1))

        transposed = [''.join(row) for row in zip(*result)]
        return '\n'.join(transposed)

exec(sys.stdin.read())