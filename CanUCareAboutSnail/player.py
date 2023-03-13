from pygame import *
import colors
from random import randint
from pic_and_button import *
font.init()
class Snail():
    def __init__(self, logicaCoins:int, yearsOld:int, hungryLvl:int, isIll:bool, isSick:bool, isDirty:bool):
        self.logica_coins = logicaCoins
        self.years = yearsOld
        self.hungry = hungryLvl
        self.is_ill = isIll
        self.is_sick = isSick
        self.is_dirty = isDirty
        self.is_died = False
        self.image = "image\snail.png"
        self.snail_eat_images = ["image\cake.png", "image\cherry.png", "image\pancakes.png"]
        self.msg_from_snail = ""
        self.msg_time = 0
        self.time_for_heal = 30
        self.not_sleep = 0
    
    def give_data_to_save(self):
        return {"logicCoins": self.logica_coins, "years": self.years,"hungry": self.hungry,"is_ill": self.is_ill, "is_sick":self.is_sick, "is_dirty":self.is_dirty}

    def is_snail_dead(self):
        if self.hungry <= 0 or self.time_for_heal <= 0 or self.not_sleep >= 2:
            self.is_died = True
        return self.is_died

    def _snail_is_hungry(self):
        return self._show_my_message_to_player("Щось я зголоднів..", 30)
    
    def _show_my_message_to_player(self, textMsg:str, sizeMsg = None, priority = 1):
        if isinstance(sizeMsg, type(None)):
            sizeMsg = 30
        if self.msg_from_snail:
            self.msg_from_snail = ""
        self.font_for_msg = font.SysFont(None, sizeMsg)
        self.msg_from_snail = self.font_for_msg.render(textMsg, 1, colors.black)
        self.msg_time = 4

    def heal_me(self):
        if not self.is_ill:
            return self._show_my_message_to_player("Я ще не хворий", 30)
        if self.logica_coins - 15 >= 0:
            self.time_for_heal = 30
            self.logica_coins -= 15
            self.is_ill = False
            return self._show_my_message_to_player("Тепер я здоровий!", 30)
        return self._show_my_message_to_player("У нас немає коінів", 30)
    
    def make_me_clear(self):
        if not self.is_dirty:
            return self._show_my_message_to_player("Я поки що чистий", 30)
        if self.logica_coins - 5 >= 0:
            self.logica_coins -= 5
            self.is_dirty = False
            return self._show_my_message_to_player("Тепер я чистий", 30)
        return self._show_my_message_to_player("У нас немає коінів", 30)

    def sleep(self):
        if not self.is_sick:
           return self._show_my_message_to_player("В мене повно енергії!", 30)
        if self.logica_coins - 2 >= 0:
            self.logica_coins -= 2
            self.is_sick = False
            return self._show_my_message_to_player("Поспали можна і поїсти", 30)
        return self._show_my_message_to_player("У нас немає коінів", 30)

    def want_to_sleep(self):
        if not self.is_sick:
            self.is_sick = True
            return self._show_my_message_to_player("Сон для равлика важливий", 30)

    def eat(self, kind_of_product):
        if (self.hungry + kind_of_product.satiety) >= 11:
            return self._show_my_message_to_player("Я стільки не з'їм", 30)
        if (self.logica_coins - kind_of_product.cost) <= 0:
            return self._show_my_message_to_player("У нас немає коінів", 30)

        self.logica_coins -= kind_of_product.cost
        self.hungry += kind_of_product.satiety
        rand = randint(0,1)
        if not self.is_dirty:
            if rand == 0: 
                self.is_dirty = True
                self._show_my_message_to_player("Схоже, треба прибратися", 30)

        return self._show_my_message_to_player("Це було смачно!", 30)
        

class Snail_eat():
    def __init__(self, image:str, satiety:int, cost:int):
        self.image = image
        self.satiety = satiety
        self.cost = cost

def init_eat():
    cake = Snail_eat("image\eat\cake.png", 3, 30)
    cherry = Snail_eat("image\eat\cherry.png", 2, 7)
    pancakes = Snail_eat("image\eat\pancakes.png", 5, 50)
    return [cake, cherry, pancakes]