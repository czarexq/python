# 🐍 Snake v2.0

> _Classic Snake game built with Python & Pygame._

A fully playable Snake game with score tracking, sound effects, multiple food spawns and a win condition — built while learning Python.

---

## 🎮 How to play

Use the **arrow keys** to control the snake. Eat food to grow and increase your score. Reach **30 points** to win!

| Key            | Action     |
| -------------- | ---------- |
| ⬆️ Arrow Up    | Move up    |
| ⬇️ Arrow Down  | Move down  |
| ⬅️ Arrow Left  | Move left  |
| ➡️ Arrow Right | Move right |

---

## ✨ Features

- 5 food pieces on the map at once
- Score counter displayed on screen
- 🔊 Chomp sound effect on eat
- Wall collision — hit the wall and it's over
- Self collision — run into yourself and it's over
- 🏆 Win screen at 30 points

---

## 📁 Project structure

```
snake/
├── main.py        # Game loop & logic
├── snake.py       # Snake rendering
├── food.py        # Food generation & rendering
├── settings.py    # Constants (screen size, colors, FPS)
└── chomp.wav      # Eat sound effect
```

---

## 🚀 Getting started

1. Make sure Python and Pygame are installed
2. Install Pygame if needed:

```
pip install pygame
```

3. Run the game:

```
python main.py
```

---

## 🛠️ Tech stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pygame](https://img.shields.io/badge/Pygame-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

---

_Made with 💙 while learning Python_
