from ctypes import resize
import pyglet
import string
from pyglet import shapes
import random

window = pyglet.window.Window(width=1280, height=720, caption="Jogo da Forca")
logo = image = pyglet.resource.image("resources/icon.png")
window.set_icon(logo)


class Game:
    def __init__(self, correct_word):

        self.wrong = 0

        self.tried = []

        self.correct_word = correct_word.lower()

        self.word = ["_" for letter in self.correct_word]

        self.background = pyglet.resource.image("resources/background.png")

        self.word_label = None
        self.tried_label = None

        self.__update_label()

    def draw_hang(self):
        x = window.width // 2 - 300
        y = window.height // 2 - 120

        self.hang = pyglet.graphics.Batch()

        self.__hang_1 = shapes.Line(x, y, x, y + 300, width=5, batch=self.hang)
        self.__hang_2 = shapes.Line(
            x, y + 300, x + 100, y + 300, width=5, batch=self.hang
        )
        self.__hang_3 = shapes.Line(
            x + 100, y + 300, x + 100, y + 270, width=5, batch=self.hang
        )

        self.hang.draw()

    def draw_hangman(self):
        x = window.width // 2 - 200
        y = window.height // 2 + 120

        self.hangman = pyglet.graphics.Batch()

        if self.wrong > 0:
            self.__head = shapes.Circle(
                x, y, 30, color=(255, 255, 255), batch=self.hangman
            )

        if self.wrong > 1:
            self.__body = shapes.Line(x, y, x, y - 120, width=5, batch=self.hangman)

        if self.wrong > 2:
            self.__arm_1 = shapes.Line(
                x, y - 50, x - 40, y - 100, width=5, batch=self.hangman
            )

        if self.wrong > 3:
            self.__arm_2 = shapes.Line(
                x, y - 50, x + 40, y - 100, width=5, batch=self.hangman
            )

        if self.wrong > 4:
            self.__leg_1 = shapes.Line(
                x, y - 120, x - 40, y - 200, width=5, batch=self.hangman
            )

        if self.wrong > 5:
            self.__leg_2 = shapes.Line(
                x, y - 120, x + 40, y - 200, width=5, batch=self.hangman
            )

        self.hangman.draw()

    def __update_label(self):
        self.word_label = pyglet.text.Label(
            " ".join(self.word),
            font_name="Config Rounded Bold",
            font_size=56,
            x=window.width // 2,
            y=window.height // 2 - 120,
        )

        self.tried_label = pyglet.text.Label(
            " ".join(list(self.tried)),
            font_name="Config Rounded Bold",
            font_size=48,
            color=(255, 46, 52, 255),
            x=window.width // 2,
            y=window.height // 2 - 220,
            anchor_x="center",
            anchor_y="center",
        )

    def press(self, key):
        if self.wrong <= 5:
            found = False
            for i in range(len(self.correct_word)):
                if self.correct_word[i] == key:
                    self.word[i] = key
                    found = True

            if not found:
                if key not in self.tried:
                    self.tried.append(key)
                self.wrong += 1

            self.__update_label()

    def run(self):
        self.background.blit(0, 0)
        self.draw_hang()
        self.draw_hangman()
        self.word_label.draw()
        self.tried_label.draw()
        # self.counter_label.draw()


selected_word = ""
with open("resources/words.txt") as file:
    possible = []
    for word in file.read().split("\n"):
        possible.append(word)

    selected_word = possible[random.randint(0, len(possible) - 1)]


game = Game(selected_word)


@window.event
def on_draw():
    window.clear()
    game.run()


@window.event
def on_key_press(symbol, modifiers):
    if chr(symbol) in string.ascii_lowercase:
        game.press(chr(symbol))


if __name__ == "__main__":
    pyglet.app.run()
