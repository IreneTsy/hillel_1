import random
class Chessboard:

        def __init__(self):
        # Створюємо клас шахова дошка і розміщаємо всередині квадрати двох видів

            self.board = [
                    ['░', '█', '░', '█', '░', '█', '░', '█'],
                    ['█', '░', '█', '░', '█', '░', '█', '░'],
                    ['░', '█', '░', '█', '░', '█', '░', '█'],
                    ['█', '░', '█', '░', '█', '░', '█', '░'],
                    ['░', '█', '░', '█', '░', '█', '░', '█'],
                    ['█', '░', '█', '░', '█', '░', '█', '░'],
                    ['░', '█', '░', '█', '░', '█', '░', '█'],
                    ['█', '░', '█', '░', '█', '░', '█', '░']
                ]

            # Визначаємо список фігур для заповнення дошки
            self.kings = ['♕', '♛']
            self.p = ['♖', '♗', '♘', '♙', '♚', '♜', '♝', '♞', '♟']


        def random_placement(self):

            # Перемішуємо всі фігури та обов'язково додаємо двох королів
            h = random.randint(1, len(self.p))
            random_pieces = random.choices(self.p, k=h)
            self.pieces = random_pieces + self.kings

# Запускаємо цикл,який буде додавати по одній фігурі зі списку у  випадкову
            # ячейку, значення якої задано умовою
            while len(self.pieces) > 0:
                r = random.randint(0, (len(self.board) - 1))
                # print(r)
                c = random.randint(0, (len(self.board) - 1))
                # print(c)
                if self.board[r][c] == '█' or '░':
                    self.board[r][c] = self.pieces.pop()

        def print_board(self):
            # Друкуємо карскас дошки та саму дошку построково
            print("  a b c d e f g h")
            print(" +-----------------+")
            for i, row in enumerate(self.board):
                print(f"{8 - i}|{' '.join(row)}|")
            print(" +-----------------+")
            print("\n")


chess = Chessboard()

# Повторюємо виведення таблиці 3 рази
for _ in range(3):
    chess.random_placement()
    chess.print_board()
