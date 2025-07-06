Here’s a breakdown of what each line or block does so you can understand and learn from it:

🧩 Drag and drop lines and change their orientation.

## 🎮 Features

- Click to add horizontal line
- Click and drag to move lines
- Use arrow keys to rotate:
  - ▶️ Right: Rotate clockwise
  - ◀️ Left: Rotate counter-clockwise
- 🗑️ Backspace: Delete selected line
- 📸 Press `S` to save a screenshot

## 🧠 Line Directions

- `horizontal` — →
- `vertical` — ↓
- `diagonal_down` — ↘️
- `diagonal_up` — ↗️

## 📦 Requirements

- Python 3.x
- Pygame

### Import & Initialization

```
import pygame
import sys

```

Imports the `pygame` module for graphics and `sys` for exiting the program.

```
pygame.init()

```

### Constants & Setup

```
GRID_SIZE = 10
CELL_SIZE = 120
WINDOW_WIDTH = GRID_SIZE * CELL_SIZE
WINDOW_HEIGHT = GRID_SIZE * CELL_SIZE

```

1. Sets up a 10x10 grid, with each cell being 120 pixels square.
2. Calculates the window dimensions accordingly.
```
WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
RED = (255, 0, 0)

```

3. Defines RGB color values.

```
FPS = 60
LINE_LENGTH = CELL_SIZE

INTERPRETATION:

1. Sets the frame rate to 60 frames per second.
2. Each line is as long as a cell.

```

4. Pygame Window Setup

```
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Lines Puzzle")
clock = pygame.time.Clock()

INTERPRETATION:

1. Creates the window, sets the title, and initializes the clock to control the frame rate.

```

5. A list of all possible orientations.

```
DIRECTIONS = ['horizontal', 'diagonal_down', 'vertical', 'diagonal_up']

```

6. Storing lines data as a list:

```
match_lines = []
selected_line = None
is_dragging = False

INTERPRETATION:

1. Tracks which line is selected.
2. Tracks whether the mouse is dragging a line
```

### Drawing Functions

1. Draws the vertical and horizontal lines of the grid.

```
def draw_grid():

```

2. Looping all lines:

```
def draw_lines():

INTERPRETATION:

1. Loops through all lines and draws them according to their orientation.
2. Highlights selected lines in red.
```

3. Interaction Logic

```
def get_line_at_cell(grid_x, grid_y, strict=True):

INTERPRETATION:
1. Determines if a line exists at the clicked grid location.
2. If `strict=True`, also checks proximity to the actual line based on mouse position.
```


### Main Game Loop

1. The main game loop runs continuously until the window is closed.

```
while True:

```

2. Clears screen and redraws grid and line each frame.

```
screen.fill(WHITE)
draw_grid()
draw_lines()

```

3. Handles user input events (quit, mouse, keyboard):

```
for event in pygame.event.get():
```

### Mouse Events

1. Mouse click event:

```
if event.type == pygame.MOUSEBUTTONDOWN:

INTERPRETATION:

On mouse click:

1. Detects which cell was clicked.
2. If clicked on a line → select it.
3. Otherwise, add a new horizontal line.
```

2. Mouse Dragging Event:

```
if event.type == pygame.MOUSEBUTTONUP:

INTERPRETATION:

1. Ends dragging when mouse is released.
```

3. While Dragging Event

```
if event.type == pygame.MOUSEMOTION and is_dragging:

INTERPRETATION:

1. While dragging, Update the line's grid position to follow the mouse.
```

### Keyboard Events

```
if event.type == pygame.KEYDOWN and selected_line is not None:

```

1. When a key is pressed:
	a. **Right Arrow** → rotate clockwise
	b. **Left Arrow** → rotate counter-clockwise
	c. **Backspace** → delete line
	d. **S Key** → save the screen as an image

2. Display and Frame rate:

```
pygame.display.flip()
clock.tick(FPS)

INTERPRETATION:

1. Updates the display and limits the frame rate.
```



## License

This project is licensed under the [MIT License](./LICENSE).

