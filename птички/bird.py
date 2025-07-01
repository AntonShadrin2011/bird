import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
SCREEN_TITLE = 'Bird'

class Bird(arcade.Sprite):
    def fff(self):
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
        super().__init__(os.path.join('/Users/anton/PycharmProjects/PythonProject/птички', 'pipe.png'), scale=1)

    def logika(self):
        self.center_x -= 2


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bird = Bird()
        self.background = arcade.load_texture(
            os.path.join('/Users/anton/PycharmProjects/PythonProject/птички', 'bg.png'))
        self.truby = arcade.SpriteList()
        self.score = 0

    def setup(self):
        self.bird.center_y = self.height // 2
        self.bird.center_x = 237
        for i in range(4):
            truba = Truba()
            truba.center_x = 800 + i * 300
            truba.center_y = 250
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
        for tube in self.truby:
            if tube.right < self.bird.left and not hasattr(tube, 'passed'):
                tube.passed = True
                self.score += 1

    def on_key_press(self, key, mods):
        if key == arcade.key.SPACE:
            self.bird.change_y = 15


game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()