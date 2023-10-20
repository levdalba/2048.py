import turtle
import random


window = turtle.Screen()
window.title("2048")
window.setup(600, 600)
window.tracer(0)

board_size = 4
board = [[0] * board_size for _ in range(board_size)]

tile_colors = {
    0: "#CDC1B4",
    2: "#EEE4DA",
    4: "#EDE0C8",
    8: "#F2B179",
    16: "#F59563",
    32: "#F67C5F",
    64: "#F65E3B",
    128: "#EDCF72",
    256: "#EDCC61",
    512: "#EDC850",
    1024: "#EDC53F",
    2048: "#EDC22E",
}

font = ("Arial", 20, "bold")

tile_size = 100

game_board = turtle.Turtle()
game_board.hideturtle()
game_board.penup()
game_board.speed(0)


def draw_board():
    for i in range(board_size):
        for j in range(board_size):
            x = (j - board_size / 2) * tile_size
            y = (board_size / 2 - i) * tile_size
            draw_tile(x, y, board[i][j])


def draw_tile(x, y, value):
    game_board.goto(x, y)
    game_board.pendown()
    game_board.begin_fill()
    game_board.fillcolor(tile_colors.get(value, "#000000"))
    for _ in range(4):
        game_board.forward(tile_size - 5)
        game_board.right(90)
    game_board.end_fill()
    game_board.penup()
    if value > 0:
        game_board.goto(x + tile_size / 2, y - tile_size / 2)
        game_board.write(value, align="center", font=font)


def add_initial_tile():
    add_tile()


def add_tile():
    empty_cells = [
        (i, j) for i in range(board_size) for j in range(board_size) if board[i][j] == 0
    ]
    if empty_cells:
        i, j = random.choice(empty_cells)
        board[i][j] = 2 if random.random() < 0.9 else 4


def move_up():
    move("up")


def move_down():
    move("down")


def move_left():
    move("left")


def move_right():
    move("right")


def move(direction):
    for _ in range(board_size):
        if direction == "up":
            up_moving()
        elif direction == "down":
            down_moving()
        elif direction == "left":
            left_moving()
        elif direction == "right":
            move_single_direction_right()
    add_tile()
    draw_board()


def up_moving():
    for j in range(board_size):
        for i in range(1, board_size):
            if board[i][j] == 0:
                continue
            k = i
            while k > 0 and board[k - 1][j] == 0:
                board[k - 1][j] = board[k][j]
                board[k][j] = 0
                k -= 1
            if k > 0 and board[k - 1][j] == board[k][j]:
                board[k - 1][j] *= 2
                board[k][j] = 0


def down_moving():
    for j in range(board_size):
        for i in range(board_size - 2, -1, -1):
            if board[i][j] == 0:
                continue
            k = i
            while k < board_size - 1 and board[k + 1][j] == 0:
                board[k + 1][j] = board[k][j]
                board[k][j] = 0
                k += 1
            if k < board_size - 1 and board[k + 1][j] == board[k][j]:
                board[k + 1][j] *= 2
                board[k][j] = 0


def left_moving():
    for i in range(board_size):
        for j in range(1, board_size):
            if board[i][j] == 0:
                continue
            k = j
            while k > 0 and board[i][k - 1] == 0:
                board[i][k - 1] = board[i][k]
                board[i][k] = 0
                k -= 1
            if k > 0 and board[i][k - 1] == board[i][k]:
                board[i][k - 1] *= 2
                board[i][k] = 0


def move_single_direction_right():
    for i in range(board_size):
        for j in range(board_size - 2, -1, -1):
            if board[i][j] == 0:
                continue
            k = j
            while k < board_size - 1 and board[i][k + 1] == 0:
                board[i][k + 1] = board[i][k]
                board[i][k] = 0
                k += 1
            if k < board_size - 1 and board[i][k + 1] == board[i][k]:
                board[i][k + 1] *= 2
                board[i][k] = 0


def check_win():
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 2048:
                return True
    return False


def check_moves_left():
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 0:
                return True
            if i > 0 and board[i][j] == board[i - 1][j]:
                return True
            if j > 0 and board[i][j] == board[i][j - 1]:
                return True
    return False


def main():
    add_initial_tile()
    draw_board()

    window.listen()
    window.onkey(move_up, "Up")
    window.onkey(move_down, "Down")
    window.onkey(move_left, "Left")
    window.onkey(move_right, "Right")

    while True:
        window.update()

        if check_win():
            print("You won!")
            break

        if not check_moves_left():
            print("Game over!")
            break


if __name__ == "__main__":
    main()
