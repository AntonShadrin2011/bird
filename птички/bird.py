import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Bird'

class Bird(arcade.Sprite):
    def __init__(self):
        super().__init__('bird.png', scale=1)

    def logika(self):
        self.center_y += self.change_y
        self.change_y -= 1
        if self.bottom < 250:
            self.bottom = 250
        if self.top > 800:
            self.top = 800
        if self.change_y > 0:
            self.angle = 20
        elif self.change_y < 0:
            self.angle = -45
        else:
            self.angle = 0


class Truba(arcade.Sprite):
    def __init__(self):
        super().__init__('pipe.png', scale=0.3)
        self.change_x = 7
    def update(self):
        self.center_x -= self.change_x
        if self.center_x < 3:
            self.center_x = 1350
            self.zapret = False

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bird = Bird()
        self.background = arcade.load_texture('bg.png')
        self.truby = arcade.SpriteList()
        self.score = 0

    def setup(self):
        self.bird.center_y = self.height // 2
        self.bird.center_x = 237
        for i in range(4):
            truba = Truba()
            truba.center_x = 230 * i
            truba.center_y = 177
            self.truby.append(truba)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, height=self.height,
                                      texture=self.background)
        self.bird.draw()
        self.truby.draw()
        arcade.draw_text(f'Очки: {self.score}', 10, 780, arcade.color.WHITE, 18)

    def update(self, delta_time):
        self.bird.logika()
        self.truby.update()


    def on_key_press(self, key, mods):
        if key == arcade.key.SPACE:
            self.bird.change_y = 15


game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()

"""
1. Сделать спавн труб по игреку случайный
2. Подумать и попытаться реализовать верхние трубы
3. Убрать фон у картинок (труб)
4. Добавить звуки
5. Сделать подсчёт очков
6. Задание *: сделать проигрыш, что если мы столкнулись с трубами - отрисовать картинку (game over), нужно только найти её

"""