import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 300, 600
GRID_SIZE = 30
COLUMNS, ROWS = WIDTH // GRID_SIZE, HEIGHT // GRID_SIZE
WHITE, BLACK, GRAY = (255, 255, 255), (0, 0, 0), (128, 128, 128)

# Shapes and Colors
SHAPES = [
    [[1, 1, 1, 1]],  # I shape
    [[1, 1], [1, 1]],  # O shape
    [[0, 1, 1], [1, 1, 0]],  # S shape
    [[1, 1, 0], [0, 1, 1]],  # Z shape
    [[1, 1, 1], [0, 1, 0]],  # T shape
    [[1, 1, 1], [1, 0, 0]],  # L shape
    [[1, 1, 1], [0, 0, 1]]  # J shape
]
SHAPE_COLORS = [(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0), (128, 0, 128), (255, 165, 0), (0, 0, 255)]

# Game Variables
grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
score = 0
level = 1
speed = 30


class Piece:
    def __init__(self):
        self.shape = random.choice(SHAPES)
        self.color = SHAPE_COLORS[SHAPES.index(self.shape)]
        self.x = COLUMNS // 2 - len(self.shape[0]) // 2
        self.y = 0

    def rotate(self):
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        if not self.collision(new_shape):
            self.shape = new_shape

    def collision(self, shape=None, dx=0, dy=0):
        if shape is None:
            shape = self.shape
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x, new_y = self.x + x + dx, self.y + y + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or (new_y >= 0 and grid[new_y][new_x] != BLACK):
                        return True
        return False

    def lock(self):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    grid[self.y + y][self.x + x] = self.color

    def hard_drop(self):
        while not self.collision(dy=1):
            self.y += 1
        self.lock()


def clear_rows():
    global grid, score, level, speed
    new_grid = [row for row in grid if BLACK in row]
    cleared = ROWS - len(new_grid)
    score += cleared * 100
    if cleared:
        level += 1
        speed = max(10, speed - 2)
    while len(new_grid) < ROWS:
        new_grid.insert(0, [BLACK] * COLUMNS)
    grid = new_grid


def draw_grid(screen):
    for y in range(ROWS):
        for x in range(COLUMNS):
            pygame.draw.rect(screen, grid[y][x], (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE))
    for x in range(COLUMNS + 1):
        pygame.draw.line(screen, GRAY, (x * GRID_SIZE, 0), (x * GRID_SIZE, HEIGHT))
    for y in range(ROWS + 1):
        pygame.draw.line(screen, GRAY, (0, y * GRID_SIZE), (WIDTH, y * GRID_SIZE))


def draw_score(screen):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(text, (10, 10))


def draw_ghost_piece(screen, piece):
    ghost_y = piece.y
    while not piece.collision(dy=ghost_y - piece.y + 1):
        ghost_y += 1
    for y, row in enumerate(piece.shape):
        for x, cell in enumerate(row):
            if cell:
                pygame.draw.rect(screen, GRAY, ((piece.x + x) * GRID_SIZE, ghost_y * GRID_SIZE, GRID_SIZE, GRID_SIZE),
                                 1)


# Main Game Loop
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tetris")
clock = pygame.time.Clock()
piece = Piece()
game_over = False
time_counter = 0


def game_loop():
    global piece, game_over, time_counter, speed
    running = True
    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not piece.collision(dx=-1):
                    piece.x -= 1
                elif event.key == pygame.K_RIGHT and not piece.collision(dx=1):
                    piece.x += 1
                elif event.key == pygame.K_DOWN:
                    if not piece.collision(dy=1):
                        piece.y += 1
                elif event.key == pygame.K_UP:
                    piece.rotate()
                elif event.key == pygame.K_SPACE:
                    piece.hard_drop()
                    clear_rows()
                    piece = Piece()
                    if piece.collision():
                        game_over = True

        if time_counter % speed == 0:
            if not piece.collision(dy=1):
                piece.y += 1
            else:
                piece.lock()
                clear_rows()
                piece = Piece()
                if piece.collision():
                    game_over = True

        draw_grid(screen)
        draw_score(screen)
        draw_ghost_piece(screen, piece)
        for y, row in enumerate(piece.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, piece.color,
                                     ((piece.x + x) * GRID_SIZE, (piece.y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE))

        pygame.display.flip()
        time_counter += 1
        clock.tick(30)

        if game_over:
            running = False
            print("Game Over! Final Score:", score)


game_loop()
pygame.quit()