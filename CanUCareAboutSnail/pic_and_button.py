from pygame import *
import colors
font.init()
main_window = display.set_mode((500,800))
class Picture(sprite.Sprite):
    def __init__(self, path_to_pic:str, pic_size:set, position:set, rect_color = None):
        super().__init__()
        self.transformed = transform.scale(image.load(path_to_pic), pic_size)
        self.rect = self.transformed.get_rect()
        self.pos = position
        self.max_x = self.pos[0] + self.rect[2]
        self.max_y = self.pos[1] + self.rect[3]
        if isinstance(rect_color, type(None)):
            self.rect_color = colors.green
        else:
            self.rect_color = rect_color

    def change_rect_color(self, value): # for pics
        if isinstance(value, bool):
            if value: return colors.red
            return colors.green
        if value >= 7: return colors.green
        elif value >= 4: return colors.yellow
        else: return colors.red
    def check_click(self, mouse):
        if self.rect.collidepoint(mouse):
            print(True)
    def update(self):
        main_window.blit(self.transformed, self.pos)

class Button:
    def __init__(self, text:str, position:set, fontName = None, size = None, color = None):
        """ In position first is width, then height """

        if isinstance(fontName, type(None)):
            self.fontName = "Corbel"
        else:
            self.fontName = fontName
        if isinstance(size, type(None)):
            self.size = 45
        else:
            self.size = size
        if isinstance(color, type(None)):
            self.buttonColor = colors.white
        else:
            self.buttonColor = color
        self.sizedFont = font.SysFont(self.fontName, self.size)
        self.fin_button = self.sizedFont.render(text, 1, self.buttonColor)
        self.rect = self.fin_button.get_rect()
        self.pos = position
        self.max_x = self.pos[0] + self.rect[2]
        self.max_y = self.pos[1] + self.rect[3]
    
    def draw_rect(self, rect_color):
        draw.rect(main_window, rect_color, [self.pos, self.rect[2:4]])

    def update(self):
        main_window.blit(self.fin_button, self.pos)
 
def intro_buttons():
    btn_start_game = Button("Початок гри", (152,320))
    btn_guide = Button("Керівництво", (150, 380))
    btn_exit_game = Button("Вихід", (215, 440))
    btn_birth = Button("Народження", (250, 265))
    return [btn_start_game, btn_guide, btn_exit_game, btn_birth] 

def pic_init():
    heart_image = Picture("image\\buttons\\heart.png", (80,80), (35, 135))
    make_me_clear_image = Picture("image\\buttons\\water_drops.png", (80,80), (275,135))
    want_eat_image = Picture("image\\buttons\\cookie.png", (100,95), (145, 130))
    game_image = Picture("image\\buttons\\game.png", (80,80), (385, 135))
    sleep_image = Picture("image\\buttons\\sleep.png", (80,80), (385, 243))
    return [heart_image, make_me_clear_image, want_eat_image, game_image, sleep_image]