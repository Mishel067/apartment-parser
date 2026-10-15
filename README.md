# Tic-Tac-Toe 🎮

A classic console-based **Tic-Tac-Toe** game with a computer opponent, built in Python.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
|  **AI Opponent** | Play against a computer that makes random moves |
| 🔄 **Turn Order** | Choose whether you go first (❌) or second (⭕) |
| 🎨 **Emoji Board** | Clean visual display using ⬜ ❌ ⭕ |
| 📊 **Game Counter** | Tracks how many matches you've played |
| 💬 **Random Phrases** | Different welcome messages each game |
| ✅ **Input Validation** | Handles invalid coordinates and occupied cells |
| 🧹 **Auto-Clear Console** | Keeps the screen tidy between moves |
| 🏆 **Win/Draw Detection** | Instant recognition of game outcomes |

---

## 🚀 Getting Started

### Requirements
- **Python 3.x**
- **No external dependencies** – uses only standard library:
  - `random`
  - `time`
  - `os`

### Installation
```bash
# 1. Clone or download the file
git clone <repository-url>

# 2. Navigate to the directory
cd tic-tac-toe

# 3. Run the game
python tic_tac_toe.py
```

---

## 🎮 How to Play

### Starting the Game
```
Hello! Would you like to play?
> yes

The game begins

Will you go first (X) or second (O)?(1 or 2)
> 1
```

### Making a Move
```
It's your turn, you're Xs
Enter the row and column number
> 2 3
```
**Format:** `row column` (numbers from **1 to 3**)

### Game Flow
1. Board displays with empty cells (⬜)
2. Players alternate placing marks
3. Game ends when:
   - **3 in a row** → Win! 🎉
   - **All cells filled** → Draw! 
4. Choose to play again or exit

---

## 📋 Controls Reference

| Input | Action |
|-------|--------|
| `yes` / `no` | Start or quit the game |
| `1` | Go first (play as ❌) |
| `2` | Go second (play as ⭕) |
| `row col` (e.g., `1 3`) | Place your mark |

---

## 🎯 Board Example

```
⬜⬜⬜
❌⬜
⬜⭕⬜
```

**Legend:**
| Symbol | Meaning |
|--------|---------|
| ⬜ | Empty cell |
| ❌ | Player (1) |
| ⭕ | Computer (2) |

---

## 🛠 Technical Details

| Property | Value |
|----------|-------|
| **Language** | Python 3 |
| **Platform** | Cross-platform (Windows, macOS, Linux) |
| **Dependencies** | None (standard library only) |
| **AI Logic** | Random move selection |
| **Board Size** | 3×3 grid |
| **Console Clear** | `cls` (Windows) / `clear` (Unix) |

### Code Structure
```
tic_tac_toe.py
├── show_field()        # Display the game board
├── ask_for_game()      # Prompt to start/restart
├── who_goes_first()    # Player chooses turn order
├── user_input()        # Handle player moves
├── computer_move()     # Generate computer moves
├── check_result()      # Check win/draw conditions
├── clear_console()     # Clear screen
└── main_game()         # Main game loop
```

---

## 📄 Game Rules

1. **Win Condition:** 3 matching symbols in a row (horizontal, vertical, or diagonal)
2. **Draw Condition:** All 9 cells filled with no winner
3. **Invalid Move:** Cell already occupied or coordinates out of range
4. **Turn Order:** 
   - Player 1 = ❌ (X)
   - Player 2 =  (O)

---

##  Known Limitations

- ️ Computer uses **random moves** (not strategic AI)
- ⚠️ Recursion limit may trigger after ~1000 invalid inputs
- ⚠️ No undo move feature

---

## 📄 License

**Free to use, modify, and distribute.**  
Feel free to fork and improve! 🍴

---

##  Acknowledgments

- Built with ❤️ using **Python**
- Emoji support for modern terminals
- Inspired by the classic pen-and-paper game

---

> **Made by [Your Name]**  
> *Have fun and may the best player win!* 🏆

---

## 📞 Contact

Found a bug? Have a suggestion? Feel free to open an issue or submit a pull request!

```bash
# Report issues at:
github.com/yourusername/tic-tac-toe/issues
```

---

**Enjoy the game!** 🎮✨