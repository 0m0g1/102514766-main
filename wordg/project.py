import requests
import googletrans
from tabulate import tabulate
from googletrans import Translator


translator = Translator()

class Game():
    def __init__(self):
        self.lang = ""
        self.score = 0

    def menu(self):
        action = input(
        """
        \r#### Wordg Menu ####

        \r>>> Start(s)
        \r>>> Help(h)
        \r>>> List languages(l)
        \r>>> Quit(q)

        \r>>> """).lower().lstrip()
        if action == "s":
            self.start()
            return True
        elif action == "h":
            self.help()
            return True
        elif action == "l":
            self.listall()
        elif action == "q":
            self.quit()
        else:
            print("""
            Invalid action ｡ﾟ･ (>﹏<) ･ﾟ｡
            Valid actions are s, h, l and q
            """)
            if input(">>> "):
                self.menu()
            else:
                self.menu()

    def help(self):
        text = """
        \r#### 0m0g1's Wordg ####

        \rWordg, word guess, is a guessing game.
        \rYou choose a language then the game prompts you with a random word in the chosen language.
        \r(To see a list of available languages press l in the menu)
        \rYour task is to guess the word.
        \rYou have four tries for each word and you are given five words.
        \rAfter two trials the game gives you the first letter of the word as a hint.
        \rAfter three trials it gives you two.
        \rAfter four it gives you three.
        \rAfter five it gives you the whole word.

        \rWarning the game is hard 😀

        \rBest of wishes soldire (￣^￣)ゞ

        \r>>> """.lstrip()
        if input(text):
            self.menu()
        else:
            self.menu()

    def listall(self):
        languages = []
        for lang in googletrans.LANGUAGES:
            languages.append([googletrans.LANGUAGES[lang], lang])
        print(tabulate(languages, headers=["Language", "ISO-639 code (What to input)"], tablefmt="grid"))
        if input("\n>>> "):
            self.menu()
        else:
            self.menu()

    def get_words(self):
        response = requests.get("https://random-word-api.vercel.app/api?words=5")
        if response.status_code == 200:
            return response.json()
        else:
            return False

    def choose_lang(self, lang):
        if lang in googletrans.LANGUAGES:
            self.lang = lang
            return True
        else:
            return False

    def translate_word(self, word):
        try:
            return translator.translate(word, dest=self.lang).text
        except:
            return False

    def test_word(self, word):
        if test := self.translate_word(word):
            for i in range(6):
                if i < 5:
                    print(f'Your word is >>> {test}')
                    if i > 1:
                        try:
                           h = word[i+1]
                           print(f'Hint >>> {word[0:i-1]}')
                        except:
                            print("\n>>> You aren't getting a longer hint for this one ｡ﾟ･ (>﹏<) ･ﾟ｡")
                            print(f'Hint >>> {word[0:len(word)-1]}')
                    if input(">>> ") != word:
                        pass
                    else:
                        self.score += 1
                        print(">>> Correct ٩(^ᴗ^)۶\n")
                        break
                else:
                    print("\nWrong (×﹏×)")
                    print(f'The answer word was {word} ｡ﾟ･ (>﹏<) ･ﾟ｡\n')
                    break

        else:
            stext = ("""
                \rThere was an error translating your words ｡ﾟ･ (>﹏<) ･ﾟ｡
                \rThere might be a network error or you can try using a different language.
                \rA list of available languages can be accessed in the menu by pressing (L).

                \r>>> """)
            if input(stext):
                self.menu()
            else:
                self.menu()

    def retry(self):
        if input("Do you want to retry? o(〃＾▽＾〃)o >>> ").lower in ["y", "yes"]:
            self.start()
        else:
            self.menu()

    def quit(self):
        print("""
        \rGoodbye soldire (ಥ﹏ಥ)\n""")

    def start(self):
        if self.choose_lang(input("Choose a language: ").lower()):
            if words := self.get_words():
                for word in words:
                    self.test_word(word)
                print(f"Your score is {self.score}/{len(words)}.")
                self.score = 0
                self.retry()
            else:
                print("There was an error fetching the words")
                self.menu()
        else:
            stext = ("""
                \rThe language you inputed is not supported ｡ﾟ･ (>﹏<) ･ﾟ｡
                \rA list of available languages can be accessed in the menu by pressing (L).

                \r>>> """)
            if input(stext):
                self.start()
            else:
                self.start()



def main():
    game = Game()
    game.menu()

if __name__ == "__main__":
    main()