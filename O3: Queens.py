class EQ:
    def __init__(self, queens=None):
        if queens is None:
            self.queens = 8 * [-1]
        else:
            self.queens = queens

    def get(self, i):
        return self.queens[i]

    def set(self, i, j):
        self.queens[i] = j

    def isSolved(self):
        return self.queens.count(-1) == 0 and self.is_valid_placement()

    def is_valid_placement(self):
        for i in range(8):
            for j in range(i + 1, 8):
                if (
                    self.queens[i] == self.queens[j]
                    or abs(self.queens[i] - self.queens[j]) == j - i
                ):
                    return False
        return True

    def printBoard(self):
        if not self.isSolved():
            print("Queens are not correctly placed.")
        else:
            for i in range(8):
                row = "|"
                for j in range(8):
                    if self.queens[i] == j:
                        row += "X|"
                    else:
                        row += " |"
                print(row)

def main():
    board1 = EQ()
    board1.set(0, 2)
    board1.set(1, 4)
    board1.set(2, 7)
    board1.set(3, 1)
    board1.set(4, 0)
    board1.set(5, 3)
    board1.set(6, 6)
    board1.set(7, 5)

    print("Is board1 a correct eight queen placement?", board1.isSolved())

    board2 = EQ([0, 4, 7, 5, 2, 6, 1, 3])

    if board2.isSolved():
        print("Eight queens are placed correctly in board2")
        board2.printBoard()
    else:
        print("Eight queens are placed incorrectly in board2")

if __name__ == "__main__":
    main()