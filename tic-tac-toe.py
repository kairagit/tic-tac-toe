import tkinter as tk
import threading
import platform

players = {1: "X", 2: "O"}
board = [[" " for _ in range(3)] for _ in range(3)]
turn = 1
moves = 0
game_over = False

if platform.system() == "Windows":
    import winsound

    tick_sound = lambda: threading.Thread(
        target=lambda: winsound.Beep(1200, 80)
    ).start()

    def winning_sound():
        def melody():
            for f in [523, 659, 784, 1047]:
                winsound.Beep(f, 150)

        threading.Thread(target=melody).start()

else:
    tick_sound = lambda: threading.Thread(
        target=lambda: print('\a', end='', flush=True)
    ).start()

    def winning_sound():
        def melody():
            for _ in range(6):
                print('\a', end='', flush=True)

        threading.Thread(target=melody).start()



root = tk.Tk()
root.title("🍃 Nature Tic Tac Toe 🍃")
root.geometry("450x500")
root.configure(bg="#E0F7FA")

status = tk.Label(
    root,
    text="Player 1 (X) Turn",
    font=("Comic Sans MS", 16, "bold"),
    bg="#E0F7FA",
    fg="#2E7D32"
)
status.pack(pady=10)

canvas = tk.Canvas(
    root,
    width=450,
    height=450,
    bg="#E0F7FA",
    highlightthickness=0
)
canvas.pack()


for r in range(3):
    for c in range(3):
        x = c * 150 + 75
        y = r * 150 + 75

        canvas.create_oval(
            x - 65, y - 65,
            x + 65, y + 65,
            fill="#C8E6C9",
            outline="#81C784",
            width=3
        )


line_color = "#388E3C"

canvas.create_line(
    150, 0, 150, 450,
    width=5,
    fill=line_color
)

canvas.create_line(
    300, 0, 300, 450,
    width=5,
    fill=line_color
)

canvas.create_line(
    0, 150, 450, 150,
    width=5,
    fill=line_color
)

canvas.create_line(
    0, 300, 450, 300,
    width=5,
    fill=line_color
)


def click_event(event):
    global turn, moves, game_over

    if game_over:
        return

    c = event.x // 150
    r = event.y // 150

    if board[r][c] != " ":
        return

    tick_sound()

    color = "#2E7D32" if turn == 1 else "#1B5E20"

    canvas.create_text(
        c * 150 + 75,
        r * 150 + 75,
        text=players[turn],
        font=("Helvetica", 48, "bold"),
        fill=color
    )

    board[r][c] = players[turn]
    moves += 1

  
    win_patterns = [
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    ]

    for pattern in win_patterns:

        if all(
            board[i][j] == players[turn]
            for i, j in pattern
        ):
            status.config(
                text=f"🎉 Player {turn} ({players[turn]}) wins!",
                fg="#1B5E20"
            )

            game_over = True

    
            (r1, c1), (r2, c2), (r3, c3) = pattern

            canvas.create_line(
                c1 * 150 + 75,
                r1 * 150 + 75,
                c3 * 150 + 75,
                r3 * 150 + 75,
                width=6,
                fill="#FFD700"
            )

            winning_sound()
            return


    if moves == 9:
        status.config(
            text="Draw!",
            fg="#33691E"
        )

        game_over = True
        return
    turn = 2 if turn == 1 else 1

    status.config(
        text=f"Player {turn} ({players[turn]}) Turn",
        fg="#2E7D32"
    )
canvas.bind("<Button-1>", click_event)

# Starts GUI loop
root.mainloop()
