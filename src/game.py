import json
import os
import readline
import sys


class Game:
    def __init__(self):
        self.wordlist_file = os.path.join(
            os.environ["GGEUTMARITGI_DIR"], "..", "data", "wordlist.json"
        )
        self.load_wordlist()

    def load_wordlist(self):
        with open(self.wordlist_file, "r", encoding="utf-8") as f:
            wordlist_entries = json.load(f)

        self.wordlist = wordlist_entries
        self.word_meanings = {entry["word"]: entry["meaning"] for entry in wordlist_entries}

    def find_word(self, word):
        last_char = word[-1]
        for entry in self.wordlist:
            if entry["word"][0] == last_char:
                return entry
        return None

    def describe_word(self, word):
        meaning = self.word_meanings.get(word)
        if meaning:
            print(f"Meaning: {meaning}")
        else:
            print("Meaning: (unknown)")

    def play(self):
        next_prompt = "끝말잇기"
        last_word = None
        exit_commands = {"quit", "exit", "q"}
        help_text = (
            "Type a Korean word that starts with the last character of the previous word.\n"
            "Press Enter on an empty line or type 'q', 'quit', or 'exit' to leave the game."
        )

        print("Welcome to 끝말잇기 (word chain game)!")
        print("Rules: Each word must start with the last character of the previous word.")
        print(help_text)

        while True:
            sys.stdout.write(f"{next_prompt}\n> ")
            sys.stdout.flush()
            player_word = sys.stdin.readline().strip()

            if player_word == "":
                print("Game Over!")
                return

            lower_word = player_word.lower()
            if lower_word in exit_commands:
                print("Goodbye!")
                return

            if lower_word in {"help", "h", "?"}:
                print(help_text)
                continue

            if last_word and player_word[0] != last_word["word"][-1]:
                print("That word does not start with the correct character.")
                print("Tip: Use the last character of the previous word.")
                print("Game Over!")
                return

            self.describe_word(player_word)

            next_word = self.find_word(player_word)
            if not next_word:
                print("Great job! I couldn't find a word to continue.")
                print("You win!")
                return

            print(f"Game: {next_word['word']}")
            print(f"Meaning: {next_word['meaning']}")

            last_word = next_word
            next_prompt = next_word["word"]


game = Game()
game.play()
