from pygame import *
import os
import random
import math
import time as t
import colors, player, savefile, game, guide 
from pic_and_button import *
font.init()

window_size = (500, 800) #w, h
img_background = os.path.join(os.getcwd(), "image\gackground.jpg")
background = transform.scale(image.load(img_background), (window_size))
main_window = display.set_mode(window_size)
display.set_caption("Can u care about Snail?")

def snail_birth():
    btn_birth = Button("Народження", (150, 380))    
    birth = True
    while birth:
        for ev in event.get():
            if ev.type == QUIT:
                os._exit(0)
            elif ev.type == MOUSEBUTTONDOWN:
                mouses = mouse.get_pos()
                if (mouses[0] >= btn_birth.pos[0] and mouses[0] <= btn_birth.max_x) and (mouses[1] >= btn_birth.pos[1] and mouses[1] <= btn_birth.max_y):
                    global my_snail
                    my_snail.logica_coins -= 50
                    birth = False
        main_window.blit(background, (0,0))
        btn_birth.draw_rect(colors.blue)
        btn_birth.update()
        display.update()
        time.delay(33)

def you_sure(about:str): #Уверен или нет
    if type(about) == str:
        coins = {
            "sleep": "2",
            "clear": "5",
            "heal": "15",
            "game": "0"
        }
        cash = Button(coins[about] + " коінів", (180, 320))
    else:
        cash = Button(str(about.cost) + " коінів", (180, 320))
    btn_question = Button("Це коштуватиме тобі:", (45, 265))
    btn_t = Button("Так", (150, 380))
    btn_n = Button("Ні", (270, 380))
    must_draw_question = True
    while must_draw_question:
        for ev in event.get():
            if ev.type == QUIT:
                os._exit(0)
            if ev.type == MOUSEBUTTONDOWN:
                mouses = mouse.get_pos()
                if (mouses[0] >= btn_t.pos[0] and mouses[0] <= btn_t.max_x) and (mouses[1] >= btn_t.pos[1] and mouses[1] <= btn_t.max_y):
                    is_must_draw_question = False
                    return True
                # нет
                if (mouses[0] >= btn_n.pos[0] and mouses[0] <= btn_n.max_x) and (mouses[1] >= btn_n.pos[1] and mouses[1] <= btn_n.max_y):
                    is_must_draw_question = False
                    return False
        main_window.blit(background, (0,0))
        btn_question.draw_rect(colors.eat_color)
        btn_question.update()
        btn_t.draw_rect(colors.blue)
        btn_n.draw_rect(colors.blue)
        btn_t.update()
        btn_n.update()
        cash.update()
        display.update()
        time.delay(33)

def intro_menu():
    menu = True
    btn_start_game, btn_guide, btn_exit_game, btn_birth = intro_buttons()
    while menu:
        for ev in event.get():
            if ev.type == QUIT:
                os._exit(0)
            
            if ev.type == MOUSEBUTTONDOWN:
                mouses = mouse.get_pos()
                if (mouses[0] >= btn_exit_game.pos[0] and mouses[0] <= btn_exit_game.max_x) and (mouses[1] >= btn_exit_game.pos[1] and mouses[1] <= btn_exit_game.max_y):
                    os._exit(0)
                if (mouses[0] >= btn_guide.pos[0] and mouses[0] <= btn_guide.max_x) and (mouses[1] >= btn_guide.pos[1] and mouses[1] <= btn_guide.max_y):
                    guide.show_guide()
                if (mouses[0] >= btn_start_game.pos[0] and mouses[0] <= btn_start_game.max_x) and (mouses[1] >= btn_start_game.pos[1] and mouses[1] <= btn_start_game.max_x):
                    global my_snail
                    savefile_data = savefile.get_saved_data()
                    my_snail = player.Snail(*savefile_data)
                    if not os.path.exists("data\snailsave.txt"):
                        snail_birth()
                    game_loop()

        main_window.blit(background, (0,0))

        btn_start_game.draw_rect(colors.blue)
        btn_guide.draw_rect(colors.blue)
        btn_exit_game.draw_rect(colors.blue)
        btn_start_game.update()
        btn_guide.update()
        btn_exit_game.update()

        display.update()
        time.delay(33)

def is_or_isnt(value: bool): # Да или нет
    if value: return "Так"
    return "Ні"

def show_stat_window(dead = None):
    if isinstance(dead, type(None)):
        btn_close_stat = Button("До гри", (200, 650))
    else:
        btn_close_stat = None
        btn_dead = Button("Равлик помер", (120, 600))
        btn_again = Button("До меню", (160, 650))
    btn_logica_coins = Button("Коіни: " + str(my_snail.logica_coins), (150, 135))
    btn_snail_years = Button("Вік равлика: " + str(my_snail.years), (120, 200))
    btn_snail_hungry = Button("Наскільки ситий: " + str(my_snail.hungry), (75, 265))
    btn_is_snail_ill = Button("Хворий: " + is_or_isnt(my_snail.is_ill), (150, 330))
    btn_is_snail_dirty = Button("Грязний: " + is_or_isnt(my_snail.is_dirty), (150, 395))
    btn_is_snail_sick = Button("Хоче спати: " + is_or_isnt(my_snail.is_sick), (120, 460))
    show_stat = True
    while show_stat:
        for ev in event.get():
            if ev.type == QUIT:
                if not isinstance(btn_close_stat, type(None)): # Если не умер, то сейв
                    savefile.save_data(my_snail.give_data_to_save())
                else:
                    savefile.delete_file() #Если умер - удалить
                os._exit(0)

            if ev.type == MOUSEBUTTONDOWN:
                mouses = mouse.get_pos()
                if not isinstance(btn_close_stat, type(None)):
                    if (mouses[0] >= btn_close_stat.pos[0] and mouses[0] <= btn_close_stat.max_x) and (mouses[1] >= btn_close_stat.pos[1] and mouses[1] <= btn_close_stat.max_y):
                        show_stat = False
                else:
                    if (mouses[0] >= btn_again.pos[0] and mouses[0] <= btn_again.max_x) and (mouses[1] >= btn_again.pos[1] and mouses[1] <= btn_again.max_y):
                        savefile.delete_file() # Удаляем файл и идём в меню
                        show_stat = False

        main_window.blit(background, (0,0))
        btn_logica_coins.draw_rect(colors.eat_color)
        btn_snail_years.draw_rect(colors.eat_color)
        btn_snail_hungry.draw_rect(colors.eat_color)
        btn_is_snail_ill.draw_rect(colors.eat_color)
        btn_is_snail_dirty.draw_rect(colors.eat_color)
        btn_is_snail_sick.draw_rect(colors.eat_color)
        btn_snail_years.update()
        btn_logica_coins.update()
        btn_snail_hungry.update()
        btn_is_snail_ill.update()
        btn_is_snail_dirty.update()
        btn_is_snail_sick.update()
        if not isinstance(btn_close_stat, type(None)):
            btn_close_stat.draw_rect(colors.blue)
            btn_close_stat.update()
        else:
            btn_again.draw_rect(colors.blue)
            btn_again.update()
            btn_dead.draw_rect(colors.blue)
            btn_dead.update()
        display.update()
        time.delay(33)
    
def game_loop():
    global my_snail
    my_snail_image = Picture(my_snail.image, (300, 270), (200, 320))
    heart_image, make_me_clear_image, want_eat_image, game_image, sleep_image = pic_init() # Инициализация *_image (pic_and_button)
    btn_show_statistic = Button("Статистика", (15, 700))
    btn_back_to_menu = Button("До меню", (260, 700))
    cake, cherry, pancakes = player.init_eat()
    cake_image = Picture(cake.image, (70,70), (85, 240))
    cherry_image = Picture(cherry.image, (70,70), (165, 240))
    pancakes_image = Picture(pancakes.image, (70,70), (245, 240))
    is_must_draw_eat = False
    start_msg_time, start_time = 0, t.time() # Начало показа мсг от улитки, начальное время для года и сытости
    day_night_time = t.time() # День/ночь
    is_game = True
    while is_game:

        main_window.blit(background, (0,0))
        for ev in event.get():
            if ev.type == QUIT:
                savefile.save_data(my_snail.give_data_to_save()) # Сохранение
                os._exit(0)
            elif ev.type == MOUSEBUTTONDOWN: # Если кликаем на кнопки
                mouses = mouse.get_pos()
                # В меню
                if (mouses[0] >= btn_back_to_menu.pos[0] and mouses[0] <= btn_back_to_menu.max_x) and (mouses[1] >= btn_back_to_menu.pos[1] and mouses[1] <= btn_back_to_menu.max_y):
                    is_game = False
                    savefile.save_data(my_snail.give_data_to_save())
                # Статистика
                if (mouses[0] >= btn_show_statistic.pos[0] and mouses[0] <= btn_show_statistic.max_x) and (mouses[1] >= btn_show_statistic.pos[1] and mouses[1] <= btn_show_statistic.max_y):
                    show_stat_window()

                if (mouses[0] >= want_eat_image.pos[0] and mouses[0] <= want_eat_image.max_x) and (mouses[1] >= want_eat_image.pos[1] and mouses[1] <= want_eat_image.max_y):
                    if is_must_draw_eat:
                        is_must_draw_eat = False
                    else:
                        is_must_draw_eat = True
                # Играть
                if (mouses[0] >= game_image.pos[0] and mouses[0] <= game_image.max_x) and (mouses[1] >= game_image.pos[1] and mouses[1] <= game_image.max_y):
                    if you_sure("game"):
                        my_snail.logica_coins += game.start()
                # Спать
                if (mouses[0] >= sleep_image.pos[0] and mouses[0] <= sleep_image.max_x) and (mouses[1] >= sleep_image.pos[1] and mouses[1] <= sleep_image.max_y):
                    if you_sure("sleep"):
                        start_msg_time = t.time()
                        my_snail.sleep()
                # Убраться
                if (mouses[0] >= make_me_clear_image.pos[0] and mouses[0] <= make_me_clear_image.max_x) and (mouses[1] >= make_me_clear_image.pos[1] and mouses[1] <= make_me_clear_image.max_y):
                    if you_sure("clear"):
                        start_msg_time = t.time()
                        my_snail.make_me_clear()
                # Вылечить
                if (mouses[0] >= heart_image.pos[0] and mouses[0] <= heart_image.max_x) and (mouses[1] >= heart_image.pos[1] and mouses[1] <= heart_image.max_y):
                    if you_sure("heal"):
                        start_msg_time = t.time()
                        my_snail.heal_me()
                #Поесть
                if (mouses[0] >= cake_image.pos[0] and mouses[0] <= cake_image.max_x) and (mouses[1] >= cake_image.pos[1] and mouses[1] <= cake_image.max_y):
                    if you_sure(cake):
                        start_msg_time = t.time()
                        my_snail.eat(cake)
                if (mouses[0] >= cherry_image.pos[0] and mouses[0] <= cherry_image.max_x) and (mouses[1] >= cherry_image.pos[1] and mouses[1] <= cherry_image.max_y):
                    if you_sure(cherry):
                        start_msg_time = t.time()
                        my_snail.eat(cherry)
                if (mouses[0] >= pancakes_image.pos[0] and mouses[0] <= pancakes_image.max_x) and (mouses[1] >= pancakes_image.pos[1] and mouses[1] <= pancakes_image.max_y):
                    if you_sure(pancakes): 
                        start_msg_time = t.time()
                        my_snail.eat(pancakes)

        my_snail_image.update()
        if my_snail.is_snail_dead():
            show_stat_window(True)

        if my_snail.msg_from_snail and t.time() - start_msg_time < my_snail.msg_time: # Если есть сообщение и не прошло время - рисуем
            draw.rect(main_window, colors.msg_white, [(5,450), my_snail.msg_from_snail.get_rect()[2:4]])
            main_window.blit(my_snail.msg_from_snail, (5,450))
        else: my_snail.msg_from_snail = "" # Если нет - обнуляем
        # Основные кнопки
        draw.rect(main_window, heart_image.change_rect_color(my_snail.is_ill), [heart_image.pos, (heart_image.rect[2]+2, heart_image.rect[3])])
        draw.rect(main_window, want_eat_image.change_rect_color(my_snail.hungry), [(150, 135), (want_eat_image.rect[2]-7, want_eat_image.rect[3]-15)])
        draw.rect(main_window, make_me_clear_image.change_rect_color(my_snail.is_dirty), [make_me_clear_image.pos, make_me_clear_image.rect[2:4]])
        draw.rect(main_window, game_image.change_rect_color(my_snail.is_dirty), [game_image.pos, game_image.rect[2:4]])
        draw.rect(main_window, sleep_image.change_rect_color(my_snail.is_sick), [sleep_image.pos, sleep_image.rect[2:4]])
        heart_image.update()
        want_eat_image.update()
        make_me_clear_image.update()
        game_image.update()
        sleep_image.update()

        if t.time() - start_time >= 10: # Каждые 10 секунд +год, -сытость
            my_snail.time_for_heal -= 10
            my_snail._show_my_message_to_player(str(my_snail.time_for_heal) + " секунд для лікування", 30) # До смерти
            
            my_snail.years += 1
            my_snail.hungry -= 1

            if my_snail.hungry <= 5:
                my_snail._snail_is_hungry() #Напоминание

            if not my_snail.is_ill: # Если не болен
                rand = random.randint(0,1) 
                if rand == 0: # Если заболел
                    start_msg_time = t.time()
                    my_snail._show_my_message_to_player("Схоже, я захворів", 30)
                    my_snail.is_ill = True
            start_time = t.time() # обнуление

        if t.time() - day_night_time >= 60: # Через минуту - спать
            if my_snail.is_sick: # Если не поспали
                start_msg_time = t.time()
                my_snail._show_my_message_to_player("Равлику теж треба спати", 30)
                my_snail.not_sleep += 1
                if my_snail.is_snail_dead():
                    show_stat_window(True)
            else:
                start_msg_time = t.time()
                my_snail.want_to_sleep()
            day_night_time = t.time() # обнуление

        if is_must_draw_eat: #Если нажали на еду
            draw.rect(main_window, colors.eat_color, [cake_image.pos, cake_image.rect[2:4]])
            draw.rect(main_window, colors.eat_color, [cherry_image.pos, cherry_image.rect[2:4]])
            draw.rect(main_window, colors.eat_color, [pancakes_image.pos, pancakes_image.rect[2:4]])
            cake_image.update()
            cherry_image.update()
            pancakes_image.update()
        # Нижние кнопки
        draw.rect(main_window, colors.blue, [btn_show_statistic.pos, btn_show_statistic.rect[2:4]]) 
        draw.rect(main_window, colors.blue, [btn_back_to_menu.pos, btn_back_to_menu.rect[2:4]])
        btn_show_statistic.update()
        btn_back_to_menu.update()
        display.update()
        time.delay(33)

intro_menu()