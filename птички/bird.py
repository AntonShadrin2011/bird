import arcade
import random

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
    def __init__(self,vverx):
        super().__init__('pipe.png', scale=0.3, flipped_vertically=vverx)

        self.change_x = 7
        self.is_passed = False

    def update(self):
        self.center_x -= self.change_x
        if self.right < 0:
            self.left = 800
            self.is_passed = False

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
            truba = Truba(False)
            truba.center_x = 230 * i
            truba.center_y = random.randint(50, 200)
            self.truby.append(truba)

            trubaTop = Truba(True)
            trubaTop.center_x = 230 * i
            trubaTop.center_y = random.randint(730, 880)
            self.truby.append(trubaTop)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(self.width // 2, self.height // 2, self.width, height=self.height, texture=self.background)
        self.bird.draw()
        self.truby.draw()
        arcade.draw_text(f'Очки: {self.score}', 10, 780, arcade.color.WHITE, 18)

    def update(self, delta_time):
        self.bird.logika()
        self.truby.update()
        for pipe in self.truby:
            if not pipe.is_passed and pipe.center_x < self.bird.center_x:
                pipe.is_passed = True
                self.score += 1
        collision = arcade.check_for_collision_with_list(self.bird, self.truby)
        print(collision)

    def on_key_press(self, key, mods):
        if key == arcade.key.SPACE:
            self.bird.change_y = 15

game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
game.setup()
arcade.run()
