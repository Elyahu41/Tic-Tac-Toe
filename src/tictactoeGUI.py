
import tkinter as tk
import random
import time

SCREEN_WIDTH_AND_HEIGHT = "600x600"
HEIGHT = 600
WIDTH = 600


class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.root = tk.Tk()
        self.resetGame = False
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg='#f0f0f0')
        self.root.title("Tic Tac Toe")
        self.root.geometry(SCREEN_WIDTH_AND_HEIGHT)
        self.root.resizable(0, 0)
        self.root.configure(background='#f0f0f0')
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.bind("<Button-1>", self)
        self.draw_board()
        self.canvas.create_text(300, 20, text="Tic Tac Toe", font=("Helvetica", 20))
        self.canvas.create_text(300, 380, text="Click to play", font=("Helvetica", 20))

    def on_closing(self):
        self.root.destroy()
        exit()

    def draw_board(self):
        self.canvas.pack()
        self.canvas.create_line(200, 0, 200, 600, fill='black')  # vertical line left
        self.canvas.create_line(400, 0, 400, 600, fill='black')  # vertical line right
        self.canvas.create_line(0, 200, 600, 200, fill='black')  # horizontal line top
        self.canvas.create_line(0, 400, 600, 400, fill='black')  # horizontal line bottom

    def __call__(self, event):
        self.canvas.delete("all")
        self.draw_board_from_board(self.board)
        if self.resetGame:
            self.resetGame = False
            return
        if self.draw_x(event.x, event.y) and not self.check_win() and not self.check_full() and not self.check_lose():
            self.draw_board_from_board(self.board)
            random.seed(time.time())
            x = random.randint(0, 2)
            y = random.randint(0, 2)
            if self.board[x][y] == " " and self.board[x][y] != "X":
                self.board[x][y] = "O"
                self.draw_board_from_board(self.board)
                if self.check_lose():
                    self.canvas.create_text(300, 300, text="You Lose!", font=("Helvetica", 20), fill='red')
                    self.canvas.create_text(300, 340, text="Click to play again", font=("Helvetica", 20), fill='red')
                    self.reset()
            else:
                while self.board[x][y] != " " or self.board[x][y] == "X":
                    x = random.randint(0, 2)
                    y = random.randint(0, 2)
                    if self.check_full() or self.check_win() or self.check_lose():
                        break
                if not (self.check_full() or self.check_win() or self.check_lose()):
                    self.board[x][y] = "O"
                self.draw_board_from_board(self.board)
                if self.check_lose():
                    self.canvas.create_text(300, 300, text="You Lose!", font=("Helvetica", 20), fill='red')
                    self.canvas.create_text(300, 340, text="Click to play again", font=("Helvetica", 20), fill='red')
                    self.reset()
        elif self.check_lose():
            self.draw_board_from_board(self.board)
            self.canvas.create_text(300, 300, text="You Lose!", font=("Helvetica", 20), fill='red')
            self.canvas.create_text(300, 340, text="Click to play again", font=("Helvetica", 20), fill='red')
            self.reset()
        elif self.check_win():
            self.draw_board_from_board(self.board)
            self.canvas.create_text(300, 300, text="You win!", font=("Helvetica", 20), fill='green')
            self.canvas.create_text(300, 380, text="Click to play again", font=("Helvetica", 20), fill='green')
            self.reset()
        elif self.check_full():
            self.draw_board_from_board(self.board)
            self.canvas.create_text(300, 300, text="Draw!", font=("Helvetica", 20), fill='blue')
            self.canvas.create_text(300, 340, text="Click to play again", font=("Helvetica", 20), fill='blue')
            self.reset()

    def draw_x(self, x, y):
        char = "X"
        char_played = False

        if x < 200:  # left
            if y < 200:  # top
                if self.board[0][0] != "O" and self.board[0][0] != "X":
                    self.board[0][0] = char
                    char_played = True
            elif y < 400:  # middle
                if self.board[0][1] != "O" and self.board[0][1] != "X":
                    self.board[0][1] = char
                    char_played = True
            else:  # bottom
                if self.board[0][2] != "O" and self.board[0][2] != "X":
                    self.board[0][2] = char
                    char_played = True
        elif x < 400:  # middle
            if y < 200:  # top
                if self.board[1][0] != "O" and self.board[1][0] != "X":
                    self.board[1][0] = char
                    char_played = True
            elif y < 400:  # middle
                if self.board[1][1] != "O" and self.board[1][1] != "X":
                    self.board[1][1] = char
                    char_played = True
            else:  # bottom
                if self.board[1][2] != "O" and self.board[1][2] != "X":
                    self.board[1][2] = char
                    char_played = True
        else:  # right
            if y < 200:  # top
                if self.board[2][0] != "O" and self.board[2][0] != "X":
                    self.board[2][0] = char
                    char_played = True
            elif y < 400:  # middle
                if self.board[2][1] != "O" and self.board[2][1] != "X":
                    self.board[2][1] = char
                    char_played = True
            else:  # bottom
                if self.board[2][2] != "O" and self.board[2][2] != "X":
                    self.board[2][2] = char
                    char_played = True

        return char_played

    def draw_board_from_board(self, board):
        self.canvas.delete("all")
        self.draw_board()
        for i in range(3):
            for j in range(3):
                if board[i][j] == "X":
                    self.canvas.create_line(i * 200, j * 200, (i + 1) * 200, (j + 1) * 200, fill='black')
                    self.canvas.create_line((i + 1) * 200, j * 200, i * 200, (j + 1) * 200, fill='black')
                elif board[i][j] == "O":
                    self.canvas.create_oval(200 * i, 200 * j, 200 * (i + 1), 200 * (j + 1), fill='black')

    def check_full(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    return False
        return True

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == "X" and self.board[i][1] == "X" and self.board[i][2] == "X":
                return True
            elif self.board[0][i] == "X" and self.board[1][i] == "X" and self.board[2][i] == "X":
                return True
        if self.board[0][0] == "X" and self.board[1][1] == "X" and self.board[2][2] == "X":
            return True
        elif self.board[0][2] == "X" and self.board[1][1] == "X" and self.board[2][0] == "X":
            return True
        return False

    def check_lose(self):
        for i in range(3):
            if self.board[i][0] == "O" and self.board[i][1] == "O" and self.board[i][2] == "O":
                return True
            elif self.board[0][i] == "O" and self.board[1][i] == "O" and self.board[2][i] == "O":
                return True
        if self.board[0][0] == "O" and self.board[1][1] == "O" and self.board[2][2] == "O":
            return True
        elif self.board[0][2] == "O" and self.board[1][1] == "O" and self.board[2][0] == "O":
            return True
        return False

    def reset(self):
        self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.resetGame = True


if __name__ == "__main__":
    game = TicTacToe()
    game.root.mainloop()
