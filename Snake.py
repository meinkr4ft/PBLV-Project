from enum import Enum, auto
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 20
COLUMN_COUNT = 20

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 30
HEIGHT = 30

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 2

# Do the math to figure out oiur screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN + 30

SNAKE_COLOR = arcade.color.GREEN

class Direction(Enum):
    RIGHT = auto()
    LEFT = auto()
    UP = auto()
    DOWN = auto()

velocity = Direction.RIGHT


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def setSquare(self, column, row, squarenumber, color):
        width = WIDTH // 3
        height = HEIGHT // 3
        x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 6 + squarenumber % 3 * width
        y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 6 + (2 - squarenumber // 3) * height
        arcade.draw_rectangle_filled(x, y, width, height, color)

    def setSnakeElement(self, column, row, start, end):
        self.setSquare(column, row, 4, SNAKE_COLOR)
        #if start ==

    def __init__(self, width, height):
        """
        Set up the application.
        """

        super().__init__(width, height)

        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)


        # Draw initial snake


    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

        self.setSquare(15,3, 0, arcade.color.RED)

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist
        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0


def main():

    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()