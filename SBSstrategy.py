
import time
import random


def clear_screen():
    print("\033[H\033[J")

def display_text(text, speed=0.04):
    try:
        for i in text:
            print(i, end="", flush=True)
            time.sleep(speed)
    except ValueError as e:
        print(e)
    print()

def display_print(text):
    clear_screen()
    display_text(text)
    time.sleep(2)

def disp_txt(text):
    display_text(text)
    time.sleep(1)

def get_player_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Выберите вариант: ")
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        choice = input("Пожалуйста, выберите номер варианта: ")
    return int(choice)

def hold(dmg, opponent_hp, pl_hp, pl_hero, hold_cost, points, max_hp, opp_max_hp):
    if pl_hero == "Sven":
        opponent_hp -= int(dmg * 1.3 // 1)
        points -= hold_cost
    
    elif pl_hero == "Slark":
        a = opponent_hp
        opponent_hp -= int((opponent_hp / 100 * 20) // 1)

        pl_hp -= int((a - opponent_hp) // 100 * 50 // 1)
        points -= hold_cost

    elif pl_hero == "Zeus":
        opponent_hp -= int(dmg * 2.5 // 1)

        points -= hold_cost

    elif pl_hero == "Wraith King":
        opponent_hp -= int(dmg * 2 // 1)

        pl_hp -= int(pl_hp // 100 * 15 // 1)
        points -= hold_cost

    elif pl_hero == "Drow Ranger":
        opponent_hp -= int(dmg * 1.7 // 1)
        points -= hold_cost

    elif pl_hero == "Axe":
        opponent_hp -= 280

        points -= 2


    elif pl_hero == "Sniper":
        rand = random.randint(1, 100)
        if rand <= 55:
            opponent_hp -= int(dmg * 2.3 // 1)
            disp_txt("Повезло!!!")
        else:
            disp_txt("Не повезло!!!")

        points -= 1

    elif pl_hero == "Necrophos":
        opponent_hp -= int((opp_max_hp - opponent_hp) * 0.5)
        points = 0


    return pl_hp, opponent_hp, points
        
def atk(opp_type_atk, opp_hp, dmg, melee_dmg, range_dmg, magic_dmg, points):    
    
            if opp_type_atk == "melee":
                opp_hp -= int((dmg * melee_dmg) // 1)

            elif opp_type_atk == "range":
                opp_hp -= int((dmg * range_dmg) // 1)

            elif opp_type_atk == "magic":
                opp_hp -= int((dmg * magic_dmg) // 1)

            if points < 5: points += 1

            return opp_hp, points


def fight(us_char, opp_char ):
    if opp_char == "Drow Ranger":
        opp_hp = 700
        opp_dmg = 180
        opp_melee_dmg = 0.75
        opp_range_dmg = 1.25
        opp_magic_dmg = 1.25
        opp_type_atk = "range"
        opp_hold_cost = 3

    elif opp_char == "Sven":
        opp_hp = 1010
        opp_dmg = 130
        opp_melee_dmg = 1.5
        opp_range_dmg = 0.75
        opp_magic_dmg = 1
        opp_type_atk = "melee"
        opp_hold_cost = 2

    elif opp_char == "Slark":
        opp_hp = 1100
        opp_dmg = 100
        opp_melee_dmg = 0.75
        opp_range_dmg = 1.25
        opp_magic_dmg = 1
        opp_type_atk = "melee"
        opp_hold_cost = 1

    elif opp_char == "Zeus":
        opp_hp = 500
        opp_dmg = 230
        opp_melee_dmg = 1.25
        opp_range_dmg = 0.75
        opp_magic_dmg = 1
        opp_type_atk = "magic"
        opp_hold_cost = 4

    elif opp_char == "Wraith King":
        opp_hp = 1200
        opp_dmg = 90
        opp_melee_dmg = 1
        opp_range_dmg = 1
        opp_magic_dmg = 1
        opp_type_atk = "melee"
        opp_hold_cost = 2

    elif opp_char == "Axe":
        opp_hp = 1500
        opp_dmg = 95
        opp_melee_dmg = 1.25
        opp_range_dmg = 0.9
        opp_magic_dmg = 0.9
        opp_type_atk = "melee"
        opp_hold_cost = 2

    elif opp_char == "Sniper":
        opp_hp = 700
        opp_dmg = 140
        opp_melee_dmg = 1.29
        opp_range_dmg = 0.8
        opp_magic_dmg = 1.2
        opp_type_atk = "range"
        opp_hold_cost = 1

    elif opp_char == "Necrophos":
        opp_hp = 925
        opp_dmg = 105
        opp_melee_dmg = 1.26
        opp_range_dmg = 1.2
        opp_magic_dmg = 0.8
        opp_type_atk = "magic"
        opp_hold_cost = 5
        




    
    if us_char == "Drow Ranger":
        hp = 700
        dmg = 200
        melee_dmg = 1
        range_dmg = 1.50
        magic_dmg = 1.50
        type_atk = "range"
        hold_cost = 3


    elif us_char == "Sven":
        hp = 1010
        dmg = 130
        melee_dmg = 1.5
        range_dmg = 0.75
        magic_dmg = 1
        type_atk = "melee"
        hold_cost = 2

    elif us_char == "Slark":
        hp = 1100
        dmg = 110
        melee_dmg = 0.75
        range_dmg = 1.25
        magic_dmg = 1
        type_atk = "melee"
        hold_cost = 1

    elif us_char == "Zeus":
        hp = 500
        dmg = 230
        melee_dmg = 1.25
        range_dmg = 0.75
        magic_dmg = 1
        type_atk = "magic"
        hold_cost = 4

    elif us_char == "Wraith King":
        hp = 1200
        dmg = 90
        melee_dmg = 1
        range_dmg = 1
        magic_dmg = 1
        type_atk = "melee"
        hold_cost = 2

    elif us_char == "Axe":
        hp = 1500
        dmg = 95
        melee_dmg = 1.25
        range_dmg = 0.9
        magic_dmg = 0.9
        type_atk = "melee"
        hold_cost = 2

    elif us_char == "Sniper":
        hp = 700
        dmg = 140
        melee_dmg = 1.29
        range_dmg = 0.8
        magic_dmg = 1.2
        type_atk = "range"
        hold_cost = 1

    elif us_char == "Necrophos":
        hp = 925
        dmg = 105
        melee_dmg = 1.26
        range_dmg = 1.2
        magic_dmg = 0.8
        type_atk = "magic"
        hold_cost = 5

    


    points = 0

    opp_points = 0

    turn = 0

    
    opp_max_hp = opp_hp
    max_hp = hp


    disp_txt(f"Ваш оппонент - {opp_char}")
    disp_txt("3..")
    disp_txt("2..")
    disp_txt("1..")


    display_print("Начало боя")

    while hp > 0 and opp_hp > 0:
        turn += 1
        clear_screen()
        clear_screen()
        display_print(f"Ход номер {turn}\n\n")

        print(f"Ваши очки навыков: {points} из 5")

        disp_txt(f"Ваше здоровье: {hp} из {max_hp}\n\n\n")
        disp_txt(f"Очки навыков противника: {opp_points} из 5")
        disp_txt(f"Здоровье противника: {opp_hp} из {opp_max_hp}\n")


        disp_txt("Выберете действие:")

        if points >= hold_cost:
            num = get_player_choice(["Обычная атака", "Заряженная атака"])
            if num == 1:
                opp_hp, points = atk(opp_type_atk, opp_hp, dmg, melee_dmg, range_dmg, magic_dmg, points)


                clear_screen()


            elif num == 2:
                hp, opp_hp, points = hold(dmg, opp_hp, hp, us_char, hold_cost, points, max_hp, opp_max_hp)

                clear_screen()
                
        elif points < hold_cost:
            num = get_player_choice(["Обычная атака"])

            opp_hp, points = atk(opp_type_atk, opp_hp, dmg, melee_dmg, range_dmg, magic_dmg, points)

            clear_screen()


        if opp_points >= opp_hold_cost:
            opp_hp, hp, opp_points = hold(opp_dmg, hp, opp_hp, opp_char, opp_hold_cost, opp_points, opp_max_hp, max_hp)

        else:

            hp, opp_points = atk(type_atk, hp, opp_dmg, opp_melee_dmg, opp_range_dmg, opp_magic_dmg, opp_points)

    display_print("КОНЕЦ БОЯ")
    if opp_hp > hp:
        disp_txt("Вы проиграли(((")
        a = 0
        return a

    else:
        disp_txt("Вы победили)))")
        a = 1
        return a



# TODO: акс с зараяженой атакой - крутилкой урон крутилки 200 хп 1500 урон 80                                - не готово
# TODO: снайпер с заряженой атакой - хедшотом с шансом 30% урон хеда +150 к базовой атаке хп 600 урон 130    - не готово
# TODO: некр заряженая атака стоит 5 очков, сносит 50% от потерянного хп хп 1000 урон 100                    - не готово
# TODO: пофиксить повторное выпадение противника                                                             - не готово



user_character = None # TODO: имя перса стринг

meeted_opponents = set()

characters = ["Sven", "Slark", "Zeus", "Wraith King", "Drow Ranger", "Axe", "Sniper", "Necrophos", "Узнать больше о героях"]

ch = [1, 2, 3, 4, 5, 6, 7, 8]

points = 5


hp = 1000
opp_hp = 1000

def main():
    display_print("Добро пожаловать в пошаговую стратегию под названием DOTA 0.5")




    display_text("Вы уважаете яндекс?")
    answer = get_player_choice(["Да", "Нет"])
    if answer == 1:
        display_print("Респект от Даниила Анашечева")

        us_charact = -1
        while us_charact not in ch:
            display_print("Выберете своего героя из списка:")
            us_charact = get_player_choice(characters)
            if us_charact == len(characters):
                clear_screen()
                clear_screen()

                print(" Sven: Тип боя - ближний. Тип урона - физический. Класс - физ дамагер.\n"
                    "Герой очень силен против других героев ближнего боя, но слаб против героев с магическим уроном и героев дальнего боя.\n"
                    "Заряженная атака - ценой в 2 очка герой может нанести 130% урона от атаки\n"
                    "Стартовые характеристики:\nУрон - 130\nЗдоровье - 1010\n\n", 

                    "Slark: Тип боя - ближний. Тип урона - физический. Класс - физ дамагер.\n"
                    "Герой силен против героев дальнего боя, но слаб против героев с магическим уроном.\n"
                    "Заряженная атака - ценой в 1 очко герой может нанести 10% урона от текущего хп. противника и получить 50% от нанесенного урона\n"
                    "Стартовые характеристики:\nУрон - 110\nЗдоровье - 1100\n\n", 

                    "Zeus: Тип боя - дальний. Тип урона - магический. Класс - маг дамагер.\n"
                    "Герой силен против героев ближнего боя, но слаб против героев дальнего.\n"
                    "Заряженная атака - ценой в 4 очка герой может нанести 140% урона от атаки\n"
                    "Стартовые характеристики:\nУрон - 230\nЗдоровье - 500\n\n",

                    "Wraith King: Тип боя - ближний. Тип урона - физический. Класс - танк.\n"
                    "Герой не имеет сильных или слабых сторон.\n"
                    "Заряженная атака - ценой в 2 очка герой может потерять 15% от текущего хп и нанести 200% урона от атаки\n"
                    "Стартовые характеристики:\nУрон - 90\nЗдоровье - 1200\n\n",
                    
                    "Drow Ranger: Тип боя - дальний. Тип урона - физический. Класс - физ дамагер.\n"
                    "Герой силен против героев дальнего боя, а так же героев с магическим типом урона, но слаб против героев ближнего боя.\n"
                    "Заряженная атака - ценой в 3 очка герой может нанести 170% урона от атаки\n"
                    "Стартовые характеристики:\nУрон - 200\nЗдоровье - 700\n\n"

                    "Axe: Тип боя - ближний. Тип урона - физический. Класс - танк.\n"
                    "Герой силен против других героев ближнего боя, слаб против героев с магическим уроном.\n"
                    "Заряженная атака - ценой в 2 очка герой наносит противнику 280 урона\n"
                    "Стартовые характеристики:\nУрон - 95\nЗдорьвье - 1500\n\n"

                    "Sniper: Тип боя - дальний. Тип урона - физический. Класс - физ дамагер.\n"
                    "Герой силен против героев ближнего боя, а также героев с магическим уроном. Слаб против героев дальнего боя.\n"
                    "Заряженная атака - ценой в 1 очко герой с шансом 55% наносит противнику 230% урона. В случае неудачи не наносит урона.\n"
                    "Стартовые характеристики:\nУрон - 140\nЗдорьвье - 700\n\n"

                    "Necrophos: Тип боя - дальний. Тип урона - магический. Класс - танк.\n"
                    "Герой силен против других героев дальнего боя, а также против героев ближнего боя. Слаб против героев с магическим уроном.\n"
                    "Заряженная атака - ценой в 5 очков герой наносит противнику 50% от потерянного здоровья.\n"
                    "Стартовые характеристики:\nУрон - 105\nЗдорьвье - 925\n\n"
                    
                    "Перейти к выбору героя?")
            
                get_player_choice(["Да"])
            
            else:
                user_character = characters[us_charact-1]
            
            
            clear_screen()

        display_print(f"Ваш герой - {user_character}")

        
        display_print("Хотите начать обучение?")
        

            


        if get_player_choice(["Да", "Нет"]) == 1:
            
            display_print("Тогда приступим!")

            disp_txt("Суть игры заключается в том, чтобы победить выбранным героем 2 противников и дойти до конца.\n"
                        "При поражении в бою придется начинать все с самого начала.\n"
                        "В случае победы вас ждет \"восхитительная награда\", а в случае поражения - НЕТ)")
            


            disp_txt("В течение боя у персонажа будут накапливаться/расходоваться очки навыков\n"
                    "При обычных атаках будет накапливаться 1 очко, а при заряженных атаках будет расходоваться определенное колличество очков\n"
                    "У героя есть 2 варианта атаки: обычная атака и заряженная атака, которые были расписаны в обучении\n"
                    "Бой будет окончен, если один из бойцов (союзный или вражеский герой) падет\n"
                    "В начале следующего боя очки навыков будут сброшены до начального значения, здоровье будет восполнено")
            
            time.sleep(3)

        
        
        


        a = random.randint(0, len(characters) - 2)
        opp = characters[a]
        if opp not in meeted_opponents and opp != user_character:
            meeted_opponents.update()
            z = fight(user_character, characters[a])

        if z == 1:
            num = 0
            while num != 1:
                a = random.randint(0, 4)
                opp = characters[a]
                if opp not in meeted_opponents and opp != user_character:
                    meeted_opponents.update()

                    display_print("Бой номер 2")
                    k = fight(user_character, characters[a])
                    num = 1
                
                else:
                    num = 0
            
            if k == 1:
                display_print("Ваш \"великолепный приз\" - похвала. Спасибо, что сыграли!!!")
            
            elif k == 0:
                display_print("Спасибо за игру. Вы очень далеко зашли. Попробуйте еще раз, вдруг получится)")

            


        elif z == 0:
            display_print("Спасибо за игру. От вас воняет слабостью. Вы проиграли на обучении)). Хахаххаахха. Попробуйте еще раз)")
        

        display_print("Удачи!!!")
    
    else:
        display_print("Вы не достоины играть в DOTA 0.5")
    







if __name__ == "__main__":
    main()