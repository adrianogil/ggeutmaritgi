# 끝말잇기 (Word Chain) CLI Game

A very small, CLI-based Korean word-chain game written in Python. Enter a word
and the game responds with the next word that starts with the last character of
your input. If you can stump the game, you win.

## Features

- Simple terminal gameplay.
- Uses a curated word list from `data/wordlist.txt`.
- One-command launch via a shell alias (see installation notes).

## Requirements

- Python 3.8+ (tested with Python 3).

## Installation

1. Clone the repository.
2. Set the `GGEUTMARITGI_DIR` environment variable to the `src` directory.
3. (Optional) Source the provided alias to run the game with `끝말잇기`.

Example:

```bash
export GGEUTMARITGI_DIR=/path/to/repo/src
source /path/to/repo/src/bashrc.sh
```

## Usage

Run directly:

```bash
python3 /path/to/repo/src/game.py
```

Or using the alias (after sourcing `bashrc.sh`):

```bash
끝말잇기
```

## Rules

- Your word must start with the last character of the previous word.
- If you enter an invalid word, the game ends.
- If the game cannot find a response, you win.

## Project Layout

```
.
├── data/wordlist.txt   # Word list used by the game
└── src
    ├── game.py         # Game logic and CLI loop
    ├── bashrc.sh       # Convenience alias
    └── install.gil     # Install metadata
```
