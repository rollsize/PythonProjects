from pygame import *
import colors
from pic_and_button import *
import os
window_size = (500, 800)
background = transform.scale(image.load("image\gackground.png"), (window_size))
main_window = display.set_mode(window_size)

def show_guide():
    btn_to_intro = Button("До меню", (30, 700))
    btn_next_guide = Button("Наступний", (270, 670))
    btn_prev_guide = Button("Попередній", (260, 730))
    slides = []
    for i in range(5):
        slides.append(Picture(f"image\slides\slide{i+1}.png", (500, 800), (0,0)))
    guide = True
    slide_index = 0
    while guide:
        for ev in event.get():
            if ev.type == QUIT:
                os._exit(0)
            elif ev.type == MOUSEBUTTONDOWN:
                mouses = mouse.get_pos()
                if (mouses[0] >= btn_to_intro.pos[0] and mouses[0] <= btn_to_intro.max_x) and (mouses[1] >= btn_to_intro.pos[1] and mouses[1] <= btn_to_intro.max_y):
                    guide = False
                if (mouses[0] >= btn_next_guide.pos[0] and mouses[0] <= btn_next_guide.max_x) and (mouses[1] >= btn_next_guide.pos[1] and mouses[1] <= btn_next_guide.max_y):
                    if slide_index != len(slides)-1:
                        slide_index += 1
                    else:
                        guide = False
                if (mouses[0] >= btn_prev_guide.pos[0] and mouses[0] <= btn_prev_guide.max_x) and (mouses[1] >= btn_prev_guide.pos[1] and mouses[1] <= btn_prev_guide.max_y):
                    if slide_index >= 1:
                        slide_index -= 1
        main_window.blit(background, (0,0))
        slides[slide_index].update()
        btn_to_intro.draw_rect(colors.blue)
        btn_to_intro.update()
        btn_next_guide.draw_rect(colors.blue)
        btn_next_guide.update()
        btn_prev_guide.draw_rect(colors.blue)
        btn_prev_guide.update()
        display.update()
        time.delay(33)