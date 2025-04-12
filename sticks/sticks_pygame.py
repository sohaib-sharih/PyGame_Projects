import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = 10
CELL_SIZE = 120
WINDOW_WIDTH = GRID_SIZE * CELL_SIZE
WINDOW_HEIGHT = GRID_SIZE * CELL_SIZE
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
RED = (255, 0, 0)
FPS = 60
LINE_LENGTH = CELL_SIZE

# Set up screen
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Lines Puzzle")
clock = pygame.time.Clock()

# Rotation states
DIRECTIONS = ['horizontal', 'diagonal_down', 'vertical', 'diagonal_up']

# Lines data
match_lines = []

# State
selected_line = None
is_dragging = False

# --- Drawing Functions --- #
def draw_grid():
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))

def draw_lines():
    for i, line in enumerate(match_lines):
        x, y, direction = line
        top_left_x = x * CELL_SIZE
        top_left_y = y * CELL_SIZE

        color = RED if selected_line == i else (255, 100, 100)

        if direction == 'horizontal':
            pygame.draw.line(
                screen, color,
                (top_left_x, top_left_y),
                (top_left_x + CELL_SIZE, top_left_y),
                4
            )
        elif direction == 'vertical':
            pygame.draw.line(
                screen, color,
                (top_left_x, top_left_y),
                (top_left_x, top_left_y + CELL_SIZE),
                4
            )
        elif direction == 'diagonal_down':
            center_x = top_left_x + CELL_SIZE // 2
            center_y = top_left_y + CELL_SIZE // 2
            pygame.draw.line(
                screen, color,
                (center_x - LINE_LENGTH // 2, center_y - LINE_LENGTH // 2),
                (center_x + LINE_LENGTH // 2, center_y + LINE_LENGTH // 2),
                4
            )
        elif direction == 'diagonal_up':
            center_x = top_left_x + CELL_SIZE // 2
            center_y = top_left_y + CELL_SIZE // 2
            pygame.draw.line(
                screen, color,
                (center_x - LINE_LENGTH // 2, center_y + LINE_LENGTH // 2),
                (center_x + LINE_LENGTH // 2, center_y - LINE_LENGTH // 2),
                4
            )

def get_line_at_cell(grid_x, grid_y, strict=True):
    for i, (x, y, direction) in enumerate(match_lines):
        if x == grid_x and y == grid_y:
            if not strict:
                return i
            # Check if multiple lines exist on same cell with different orientations
            # Only select if mouse click is near the actual line
            mouse_x, mouse_y = pygame.mouse.get_pos()
            cell_px = x * CELL_SIZE
            cell_py = y * CELL_SIZE

            if direction == 'horizontal' and abs(mouse_y - cell_py) < 10:
                return i
            elif direction == 'vertical' and abs(mouse_x - cell_px) < 10:
                return i
            elif "diagonal" in direction:
                return i  # basic catch for now
    return None


# --- Main Loop --- #
while True:
    screen.fill(WHITE)
    draw_grid()
    draw_lines()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = mouse_x // CELL_SIZE
            grid_y = mouse_y // CELL_SIZE

            clicked_index = get_line_at_cell(grid_x, grid_y)

            # Only select line if click is actually on the line
            if clicked_index is not None:
                selected_line = clicked_index
                is_dragging = True
            else:
                # Add a new horizontal line at that position
                match_lines.append([grid_x, grid_y, 'horizontal'])
                selected_line = len(match_lines) - 1


        if event.type == pygame.MOUSEBUTTONUP:
            is_dragging = False

        if event.type == pygame.MOUSEMOTION and is_dragging and selected_line is not None:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            grid_x = mouse_x // CELL_SIZE
            grid_y = mouse_y // CELL_SIZE
            match_lines[selected_line][0] = grid_x
            match_lines[selected_line][1] = grid_y

        # Rotate selected line
        if event.type == pygame.KEYDOWN and selected_line is not None:
            line = match_lines[selected_line]
            dir_index = DIRECTIONS.index(line[2])

            if event.key == pygame.K_RIGHT:
                line[2] = DIRECTIONS[(dir_index + 1) % len(DIRECTIONS)]

            elif event.key == pygame.K_LEFT:
                line[2] = DIRECTIONS[(dir_index - 1) % len(DIRECTIONS)]

            # Delete line
            elif event.key == pygame.K_BACKSPACE:
                match_lines.pop(selected_line)
                selected_line = None

            # Save as image
            elif event.key == pygame.K_s:
                pygame.image.save(screen, "puzzle_snapshot.png")
                print("📸 Puzzle saved as 'puzzle_snapshot.png'")

    pygame.display.flip()
    clock.tick(FPS)
