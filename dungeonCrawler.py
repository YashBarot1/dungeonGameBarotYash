import random
import sys

# Check if on Windows or Unix-based system
try:
    import msvcrt  # Windows-specific
    WINDOWS = True
except ImportError:
    import curses  # Unix-based
    WINDOWS = False

class DungeonCrawler:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player_health = 20
        self.player_pos = (0, 0)  # Starting position
        self.exit_pos = (width - 1, height - 1)  # Exit position
        self.mines = []  # Mines will be placed randomly

    def place_mines(self, num_mines):
        placed_mines = 0
        while placed_mines < num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            position = (x, y)
            # Ensure mines do not overlap with the player or exit
            if position != self.player_pos and position != self.exit_pos:
                if position not in self.mines:
                    self.mines.append(position)
                    placed_mines += 1

    def display_rules(self):
        print("""
        Welcome to the Dungeon Crawler Game!
        The entire field is full of fog, you have limited vision. 
        Rules:
        - Use 'W', 'A', 'S', 'D' to move your character around the dungeon.
        - Avoid stepping on mines (M) or you will die instantly!
        - If you "see" a mine, you lose the game! (unfair but so is life)
        - Reach the exit (E) to win the game.
        - Good luck and have fun! (lol imagine you actually win)
        """)

    def display_map(self):
        revealed_map = [['#' for _ in range(self.width)] for _ in range(self.height)]
        
        # Reveal the player's position
        player_x, player_y = self.player_pos
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                x, y = player_x + dx, player_y + dy
                if 0 <= x < self.width and 0 <= y < self.height:
                    revealed_map[y][x] = '.'
        
        revealed_map[player_y][player_x] = 'P'  # Player position
        exit_x, exit_y = self.exit_pos
        revealed_map[exit_y][exit_x] = 'E'  # Exit position
        
        # Check for mines in the visible area and end the game if visible
        for mine in self.mines:
            mx, my = mine
            if abs(mx - player_x) <= 1 and abs(my - player_y) <= 1:
                print(f"Warning! You see a mine at position ({mx}, {my})! Game Over.")
                sys.exit()  # End the game if a mine is visible
        
        # Display the mines (even if they are hidden)
        for mine in self.mines:
            mx, my = mine
            if revealed_map[my][mx] == '.':
                revealed_map[my][mx] = 'M'  # Mark the mine
        
        # Print the map
        for row in revealed_map:
            print(" ".join(row))
        print()

    def move_player(self, direction):
        x, y = self.player_pos
        if direction == 'W' and y > 0:
            y -= 1
        elif direction == 'A' and x > 0:
            x -= 1
        elif direction == 'S' and y < self.height - 1:
            y += 1
        elif direction == 'D' and x < self.width - 1:
            x += 1
        else:
            print("Invalid move!")
            return

        self.player_pos = (x, y)

        # Check if the player reached the exit
        if self.player_pos == self.exit_pos:
            print("Congratulations! You have escaped the dungeon!")
            sys.exit()  # End the game if the player wins

        self.display_map()  # Refresh the map after moving

    def get_key(self):
        if WINDOWS:
            return msvcrt.getch().decode('utf-8').upper()
        else:
            # Use curses to get real-time input on Unix-based systems
            return self.screen.getkey().upper()

    def start_game(self):
        self.display_rules()  # Display the rules
        self.place_mines(15)  # Place 15 mines
        self.display_map()  # Show the initial map

        if not WINDOWS:
            curses.wrapper(self.game_loop)  # Use curses for Unix-based systems
        else:
            self.game_loop()

    def game_loop(self, screen=None):
        if not WINDOWS:
            self.screen = screen  # Initialize screen for Unix-based systems
            self.screen.nodelay(True)  # Non-blocking input

        while True:
            move = self.get_key()
            if move == 'Q':
                print("Thanks for playing!")
                break
            elif move in ['W', 'A', 'S', 'D']:
                self.move_player(move)
            else:
                print("Invalid input! Use W, A, S, D, or Q to quit.")
game = DungeonCrawler(10,10)
game.start_game()
