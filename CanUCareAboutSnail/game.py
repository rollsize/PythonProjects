from pygame import *
from pic_and_button import *
import colors
from random import randint, randrange
import time as t
class Block(sprite.Sprite):
    def __init__(self, speed:int, pos_x:int, pos_y:int, color:set, size:set):
        super().__init__()
        self.image = Surface(size)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.max_x = self.rect.x + self.rect[2]
        self.max_y = self.rect.y + self.rect[3]
        self.color = color
        self.speed = speed
        self.image.fill(self.color)
        self.color_index = colors.blocks.index(self.color)

    def _change_color(self):
        if self.color_index == len(colors.blocks)-1 and self.color_index >= 0:
            self.color_index -= 1
        elif self.color_index >= 0:
            self.color_index += 1
        self.color = colors.blocks[self.color_index]
        self.image.fill(self.color)

    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            if self.color_index == good_block:
                global total_amount
                total_amount += 2
                self._change_color()
            else:
                global lifes
                lifes -= 1

    def update(self):
        self.rect.x += self.speed
        if self.rect.x > 470 or self.rect.x < 0:
            self.rect.x = randint(70, 400)
            self.speed = -self.speed
            rand = randint(0, 1)
            if rand == 1:
                self._change_color()
        

def start():
    global good_block, lifes, total_amount
    window_size = (500, 800)
    background = transform.scale(image.load("image\gackground.png"), (window_size))
    main_window = display.set_mode(window_size)
    bad_block = 1 # Индекс красного блока в colors
    good_block = 0 # Индекс зеленого блока в colors
    total_amount = 0 # Заработано
    lifes = 3 # количетсво жизней
    blocks = sprite.Group()
    for i in range(5):
        blocks.add(Block(randint(3,7), randrange(70, 400, 10), randint(50, 500), colors.blocks[bad_block], (randint(30, 57), randint(30, 57))))
    for i in range(5):
        blocks.add(Block(randint(3,7), randrange(70, 400, 10), randint(50, 500), colors.blocks[good_block], (randint(30, 57), randint(30, 57))))
    game = True
    start_time = t.time()
    while game and lifes >= 1:
        if t.time() - start_time >= 35:
            game = False
        for ev in event.get():
            if ev.type == QUIT:
                game = False
            elif ev.type == MOUSEBUTTONDOWN:
                for i in blocks:
                    i.check_click(ev.pos)
        btn_total_amount = Button("Заробив: " + str(total_amount), (20, 700))
        btn_lifes = Button("Життів: " + str(lifes), (300, 700))
        main_window.blit(background, (0,0))
        btn_total_amount.draw_rect(colors.blue)
        btn_total_amount.update()
        btn_lifes.draw_rect(colors.blue)
        btn_lifes.update()
        blocks.update()
        blocks.draw(main_window)
        display.update()
        time.delay(33)
    return total_amount