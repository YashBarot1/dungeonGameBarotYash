# dungeonGameBarotYash
Sure! Here's a simple README for your Dungeon Crawler game:

---

# Dungeon Crawler Game

## Overview
Welcome to **Dungeon Crawler**, a terminal-based adventure game where your goal is to navigate through a dungeon, avoid deadly mines, and escape to safety! Will you be able to reach the exit without stepping on a mine? Only time will tell!

## Features
- **Movement**: Use `W`, `A`, `S`, `D` to move up, left, down, and right.
- **Mines**: Mines are placed randomly around the dungeon. If you step on one, it's game over!
- **Exit**: Your goal is to reach the exit located at the bottom-right corner of the dungeon.
- **Game Over Condition**: If you "see" a mine within your view, the game ends immediately.
- **Win Condition**: Reach the exit to win the game.

## Installation

1. Clone the repository or download the code to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the game by executing the Python script:

    ```bash
    python dungeon_crawler.py
    ```

## Gameplay

1. When the game starts, you'll be placed at the top-left corner of the dungeon.
2. The dungeon is a grid, and you will see a map of the dungeon as you move around.
3. **Mines**: Mines are randomly placed throughout the dungeon. If you move into a space with a mine, you lose the game.
4. **Exit**: The exit is located at the bottom-right corner. If you reach it, you win!

## Controls

- `W`: Move Up
- `A`: Move Left
- `S`: Move Down
- `D`: Move Right
- `Q`: Quit the game

## Example

```
Welcome to the Dungeon Crawler Game!

Rules:
- Use 'W', 'A', 'S', 'D' to move your character around the dungeon.
- Avoid stepping on mines (M) or you will die instantly!
- If you "see" a mine, you lose the game!
- Reach the exit (E) to win the game.
- Your health is indicated at the top of the screen.
- Good luck and have fun!

Move (WASD or Q to quit):
```

### Sample Map:
```
# # # # # # # # # #
# P . . . . . . . E
# # # # # # # # # #
```

- `P` is your current position (Player).
- `E` is the exit.
- `.` are open spaces.
- `#` are walls.
- `M` (if visible) are mines.

## License
This project is open-source and available under the MIT License.

---

Feel free to customize it further or add any additional details!
