import random
class Enemy:
    def __init__(self, position, health, attack_power):
        self.position = position
        self.health = health
        self.attack_power = attack_power

    def take_damage(self, amount):
        self.health -= amount

    def is_alive(self):
        return self.health > 0
import random

class DungeonCrawler:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player_health = 20
        self.player_pos = (0, 0)  # Starting position
        self.exit_pos = (width - 1, height - 1)  # Exit position
        self.mines = []  # Mines will be placed randomly

    def place_mines(self, num_mines):
        placed_mines = 10
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

        Rules:
        - Use 'W', 'A', 'S', 'D' to move your character around the dungeon.
        - Avoid stepping on mines (M) or you will die instantly!
        - If you "see" a mine, you lose the game!
        - Reach the exit (E) to win the game.
        - Your health is indicated at the top of the screen. (it's not)
        - Good luck and have fun! (lol imagine u win)
        -Oh by the way, get to "E" to win, in case it wasn't obvious
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
                exit()  # End the game if a mine is visible
        
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
            exit()  # End the game if the player wins

        self.display_map()  # Refresh the map after moving

    def start_game(self):
        self.display_rules()  # Display the rules
        self.place_mines(20)  # Place 3 mines
        self.display_map()  # Show the initial map

        while True:
            move = input("Move (WASD or Q to quit): ").upper()
            if move == 'Q':
                print("Thanks for playing!")
                break
            elif move in ['W', 'A', 'S', 'D']:
                self.move_player(move)
            else:
                print("Invalid input! Use W, A, S, D, or Q to quit.")





class Mine:
    def __init__(self, position):
        self.position = position



# Start the game with a 10x10 dungeon
game = DungeonCrawler(10, 10)
game.start_game()
