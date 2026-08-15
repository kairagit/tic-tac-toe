Tic Tac Toe
A desktop Tic-Tac-Toe game developed in Python with an interactive graphical user interface, sound effects, turn management, win detection, and draw detection.

Features
Interactive 3×3 Tic-Tac-Toe board
Two-player gameplay: Player 1 (X) and Player 2 (O)
Graphical user interface using Tkinter
Click-based game interaction
Automatic winner detection
Winning-line animation
Draw detection
Turn indicator
Sound effects for moves and winning
Nature-inspired visual design

tech used
Python
Tkinter— GUI development
Threading— sound execution
Platform— operating-system detection for sound handling

game logic
The game maintains a 3×3 board and alternates turns between Player X and Player O.
After every move, the program:
1. Checks whether the selected cell is empty.
2. Places the player's symbol.
3. Checks all possible winning combinations.
4. Displays a winning message and highlights the winning combination if a player wins.
5. Checks for a draw if all nine cells are occupied.
6. Switches to the other player's turn if the game continues.

sound
The game provides sound feedback when a player makes a move and when a player wins.
The program uses different sound methods depending on the operating system.

requirements to run

Python 3.x
Tkinter



B.Tech — Instrumentation & Control Engineering

