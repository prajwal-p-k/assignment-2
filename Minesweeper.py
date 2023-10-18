import random

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = set(random.sample(range(width * height), mines))
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = set()

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def neighbors(self, x, y):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                if self.in_bounds(x + dx, y + dy):
                    yield x + dx, y + dy

    def count_mines_near(self, x, y):
        return sum(1 for nx, ny in self.neighbors(x, y) if (ny * self.width + nx) in self.mines)

    def reveal(self, x, y):
        if not self.in_bounds(x, y) or (x, y) in self.revealed:
            return

        self.revealed.add((x, y))

        if (y * self.width + x) in self.mines:
            self.board[y][x] = 'X'
            return

        count = self.count_mines_near(x, y)
        if count:
            self.board[y][x] = str(count)
        else:
            self.board[y][x] = ' '
            for nx, ny in self.neighbors(x, y):
                self.reveal(nx, ny)

    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print()

    def play(self):
        while True:
            self.print_board()
            x, y = map(int, input("Enter x and y coordinates (x y): ").split())
            self.reveal(x, y)
            if (y * self.width + x) in self.mines:
                print("Boom! You hit a mine!")
                break
            elif len(self.revealed) == self.width * self.height - len(self.mines):
                self.print_board()
                print("Congratulations! You won!")
                break


if __name__ == "__main__":
    game = Minesweeper()
    game.play()
