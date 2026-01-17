import json
import os


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

        while True:
            player_word = input(f"{next_prompt}\n>").strip()

            if player_word == "":
                print("Game Over!")
                return

            if last_word and player_word[0] != last_word["word"][-1]:
                print("Game Over!")
                return

            self.describe_word(player_word)

            next_word = self.find_word(player_word)
            if not next_word:
                print("You win!")
                return

            print(f"Game: {next_word['word']}")
            print(f"Meaning: {next_word['meaning']}")

            last_word = next_word
            next_prompt = next_word["word"]


game = Game()
game.play()
