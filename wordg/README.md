# **WORDG**
#### **Video Demo**:  <URL HERE>
#### **Description**:
WordG is short for word guess.
It is a game in which the player is given 5 random words in a language of his/her own chosing and is required to then guess what the word might be.
The game was written in 2023 using python by `0m0g1` on instagram as a final project for the cs50p course.

### **APIs**
Wordg uses two apis which inlude:-
- The google translate API
- The random word API - <https://random-word-api.vercel.app/>

#### a) Google translate API
The google translate API is used by a method of the class `Game`, `translate_word(word)` to translate the word to be tested into the language the use inputed.

#### b) Random words API
TherRandom words API is used by a method of the class `Game`, `get_words()` fetch the five random words which the player is going to be tested.
The method returns a list of the five words.

### **Libraries**
Libraries used in wordg include:-
- googletrans
- tabulate

To use the libraries simply type `pip install library-name` in the terminal.

#### a) Googletrans library
The google translate API is used by a method of the class `Game`, `translate_word(word)` to translate the word to be tested into the language the use inputed.

To install type `pip install googletrans` in your terminal.

#### b) Tabulate library
The Random words API is used by a method of the class `Game`, `help()`to organise a list of the supported languages into a more pleasing tabular format.

To install simply `pip install tabulate` in your terminal.

### **How to play**
When the player runs the code he will be met with a menu with five options:-
- Start (s)
- Help (h)
- List languages (l)
- Quit (q)

The player is to input the letter in the brackets into the `>>> ` sign to choose the action he/she wants to take, for example `>>> s` for start.

#### Start
After pressing `s` in the `>>>` sign this will start the game.
The user will be met with a prompt to choose the language from which he wants to guess words from. Here the user is to type the language's `ISO-639 code`.
A list of the supported languages can be found by pressing `L` in the menu.


After choosing a language the user will be prompted by a random word from the language and should now proceed to guess what the word is in english. The user now has five attemps for each word. The users guesses are inputed where the `>>> ` sign is.

After two failed attempts the user is prompted `hints` by revealing the first letter of the word. After three failed attemps the user is prompted a hint with two letters and after four a hint with three letters.

Finally if the user gets the word he/she is prompted `>>> Correct ٩(^ᴗ^)۶` and their score is updated. Otherwise they are prompted with the correct answer.Next the player is given the next word.

#### Help
In the help menu you will be prompted about the game and what it entails.

#### List
In list all languages, all languages supported by google translate and their ISO-639 code are listed in a tabular format using the tabulate library.

#### Quite
This quites the game

### **Classes**
The game has only once class called `Game` which has methods that implement all of the features of the game.

#### a) Menu
This method prints out the menu for the game with the options
- `Start`
- `Help`
- `List languages`
- `Quite`

The actions can be accessed by inputing s, h, l or q respectively.

#### b) Help
This method prints out instructions on how to play the game and what its about

#### c) Retry
This method asks the user if they want to continue playing the game or to quit

#### d) Choose_lang(code)
This method changes the language which the test is going to test on. The function takes an argument lang which should be the `ISO-639` code for the language. It returns `True` if the language is supported and returns `False` if it's not.

The codes for the supported languages are listed in the menu by inputing `L`.

#### e) Translate_word(word)
This method takes an argument word and translates it into the players specified language using the google translate library.

### Possible improvements
- Designig a UI for the game
- Implimenting a levels feature
- Implementing storage for the users data
- Add a hint feature to hint the last letter of a word
- Allow users to customize the number of words they want to be tested on
- Make tests for senteces

### How to use
1. Download a text editor like `Visual Studio Code`
2. Install the python interprator
3. Clone the games code from the github repository
4. Type `pip install googletrans` in the terminal
5. Type `pip install tabulate` in the terminal
6. Run the code