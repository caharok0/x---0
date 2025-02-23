import pygame 
import sys

X_IMAGE_PATH = "kiwi.jpg" 
O_IMAGE_PATH = "utena.jpg"

pygame.init()



WIDTH, HEIGHT = 600, 600 
LINE_WIDTH = 10 
BOARD_ROWS = 3 
BOARD_COLS = 3 
SQUARE_SIZE = WIDTH // BOARD_COLS 
WHITE = (255, 255, 255) 
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Хрестики-Нулики") 
screen.fill(WHITE)

board = [['' for _ in range(BOARD_COLS)] 
         for _ in range(BOARD_ROWS)]

X_IMAGE = pygame.image.load(X_IMAGE_PATH) 
O_IMAGE = pygame.image.load(O_IMAGE_PATH) 
X_IMAGE = pygame.transform.scale(X_IMAGE, (SQUARE_SIZE, SQUARE_SIZE)) 
O_IMAGE = pygame.transform.scale(O_IMAGE, (SQUARE_SIZE, SQUARE_SIZE))

def draw_lines(): 
    for row in range(1, BOARD_ROWS): 
        pygame.draw.line(screen, BLACK, (0, row * SQUARE_SIZE), (WIDTH, row * SQUARE_SIZE), LINE_WIDTH) 
    for col in range(1, BOARD_COLS): 
        pygame.draw.line(screen, BLACK, (col * SQUARE_SIZE, 0), (col * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def draw_figures(board): 
    for row in range(BOARD_ROWS): 
        for col in range(BOARD_COLS): 
            if board[row][col] == 'X': 
                screen.blit(X_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE)) 
            elif board[row][col] == 'O': 
                screen.blit(O_IMAGE, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def check_winner(board): 
    for row in board: 
        if row.count(row[0]) == BOARD_COLS and row[0] != '': 
            return row[0] 
    for col in range(BOARD_COLS): 
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '': 
            return board[0][col] 
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '': 
        return board[0][0] 
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '': 
        return board[0][2] 
    return None

def is_board_full(board): 
    for row in board: 
        if '' in row: 
            return False 
    return True

def main(): board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)] 
player = 'X' 
running = True 
x_wins, o_wins = 0, 0 
draw_lines()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            if board[row][col] == '':
                board[row][col] = player
                winner = check_winner(board)
                if winner:
                    if winner == 'X':
                        x_wins += 1
                    else:
                        o_wins += 1
                    print(f"Хрестики = {x_wins}, Нулики = {o_wins}")
                    board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
                elif is_board_full(board):
                    print("Нічия! Перезапуск гри.")
                    board = [['' for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
                player = 'O' if player == 'X' else 'X'
    
    screen.fill(WHITE)
    draw_lines()
    draw_figures(board)
    pygame.display.update()

pygame.quit()
sys.exit()

if name == "main": main()