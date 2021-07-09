from elfClasses import Cardslot
from elfClasses import Textbox
from bnwclasses import Character
import pygame
import os
import random

pygame.init()
red = (253, 1, 35)
yellow = (73, 69, 100)
lite_green = (0, 206, 67)
green = (0, 150, 107)
lite_blue = (143, 242, 239)
tan = (252, 247, 146)
# The following determines the actual amount of images in each folder for error catching
body_count = len(next(os.walk("Characters/body"))[2])
brow_count = len(next(os.walk("Characters/brow"))[2])
shoe_count = len(next(os.walk("Characters/shoe"))[2])
hat_count = len(next(os.walk("Characters/hat"))[2])
head_count = len(next(os.walk("Characters/head"))[2])
leg_count = len(next(os.walk("Characters/leg"))[2])
nose_count = len(next(os.walk("Characters/nose"))[2])
item_list = ["Lava Lamp", "Whoopie Cushion", "Drinky Bird", "Snow Globe"]

def menu():
    pass
def gnome_creator():
    pygame.display.set_caption('Gnomecraft')
    background = "Backgrounds/blank-book-illustration.jpg"
    bg = pygame.image.load(background)
    screenwidth = 1200
    screenheight = 700
    win = pygame.display.set_mode((screenwidth, screenheight))
    win.blit(bg, (0, 0))
    hat = Cardslot(green, 675, 100, 100, 75, None, False, name="Hat")
    head = Cardslot(green, hat.x + 170, hat.y, 100, 75, None, False, name="Head")
    brow = Cardslot(green, hat.x+5, head.y + 120, 100, 75, None, False, name="Brows")
    nose = Cardslot(green, head.x+5, head.y + 120, 100, 75, None, False, name="Nose")
    body = Cardslot(green, hat.x+10, nose.y + 120, 100, 75, None, False, name="Body")
    legs = Cardslot(green, head.x+10, nose.y + 120, 100, 75, None, False, name="Legs")
    shoe = Cardslot(green, hat.x+15, legs.y + 120, 100, 75, None, False, name="Shoes")
    randomize = Cardslot(green, head.x+15, legs.y + 120, 100, 75, None, False, name="Randomize")
    done = Cardslot(lite_green, 215, 475, 300, 75, None, False, name="Begin the Adventure!")
    title = Cardslot(red, 180, 100, 350, 60, None, False, name ="Welcome to Gnomecraft")
    choose_buttons = [hat, head, brow, nose, body, legs, shoe, randomize]
    fhat, fhead, fbrow, fnose, fbody, flegs, fshoe = 1, 1, 1, 1, 1, 1, 1
    first_char = Character("gn", fhat, fhead, fbrow, fnose, fbody, flegs, fshoe)
    first_char.draw(win, 250, 50)

    for part in choose_buttons:
        part.draw(win, outline=True)
    done.draw(win, outline=True)
    title.draw(win, outline=True)
    pygame.display.flip()
    start = False

    while start == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if done.isOver(pos):
                    finished_char = Character("gn", fhat, fhead, fbrow, fnose, fbody, flegs, fshoe)
                    the_adventure_begins(finished_char)
                for choices in choose_buttons:
                    if choices.isOver(pos):
                        if choices.name == "Hat":
                            if fhat is not hat_count:
                                fhat += 1
                            else:
                                fhat = 1
                        elif choices.name == "Head":
                            if fhead is not head_count:
                                fhead += 1
                            else:
                                fhead = 1
                        elif choices.name == "Brows":
                            if fbrow is not brow_count:
                                fbrow += 1
                            else:
                                fbrow = 1
                        elif choices.name == "Nose":
                            if fnose is not nose_count:
                                fnose += 1
                            else:
                                fnose = 1
                        elif choices.name == "Body":
                            if fbody is not body_count:
                                fbody += 1
                            else:
                                fbody = 1
                        elif choices.name == "Legs":
                            if flegs is not leg_count:
                                flegs += 1
                            else:
                                flegs = 1
                        elif choices.name == "Shoes":
                            if fshoe is not shoe_count:
                                fshoe += 1
                            else:
                                fshoe = 1

                        elif choices.name == "Randomize":
                            fhat = random.randint(1, hat_count)
                            fhead = random.randint(1, head_count)
                            fbrow = random.randint(1, brow_count)
                            fnose = random.randint(1, nose_count)
                            fbody = random.randint(1, body_count)
                            flegs = random.randint(1, leg_count)
                            fshoe = random.randint(1, shoe_count)

                redraw_screen(win, choose_buttons, fhat, fhead, fbrow, fnose, fbody, flegs, fshoe, bg=background, options=[done,title])


def the_adventure_begins(character):
    pygame.display.set_caption('Gnomecraft')
    background = "Backgrounds/Cartoon_Village.jpeg"
    bg = pygame.image.load(background)
    screenwidth = 1200
    screenheight = 600
    win = pygame.display.set_mode((screenwidth, screenheight))
    stats = char_stats(character)
    inventory = []
    while True:
        win.blit(bg, (0, 0))
        character.draw(win, 200, 200)
        choice_one, choice_two, encounter_type = encounter_gen()
        explainer_text = "You found something to do with "+encounter_type[0]+", you better do something about it."
        explain = Textbox(encounter_type[1], 100, 40, 900, 100, explainer_text, 25)
        option_one = Cardslot(choice_one[1], 220, 200, 200, 75, None, False, name=choice_one[0])
        option_two = Cardslot(choice_two[1], 220, 300, 200, 75, None, False, name=choice_two[0])
        stats_background = Textbox((210, 210, 210), 20, 200, 150, 350, "Stats", 30)
        display_fire = Cardslot(red, 70, 250, 50, 50, None, False, name=stats[0])
        display_air = Cardslot(tan, display_fire.x, display_fire.y+75, 50, 50, None, False, name=stats[1])
        display_water = Cardslot(lite_blue, display_fire.x, display_air.y+75, 50, 50, None, False, name=stats[2])
        display_earth = Cardslot(green, display_fire.x, display_water.y+75, 50, 50, None, False, name=stats[3])
        stats_display = [stats_background, display_fire, display_air, display_water, display_earth]
        for disp in stats_display:
            disp.draw(win, outline=True)
        option_one.draw(win, outline=True)
        option_two.draw(win, outline=True)
        explain.draw(win, outline=True)
        npc = Character("gn", random.randint(1, hat_count), random.randint(1, head_count),
                                random.randint(1, brow_count), random.randint(1, nose_count),
                                random.randint(1, body_count), random.randint(1, leg_count), random.randint(1, shoe_count))
        npc_strength = random.randint(0, 5)
        npc.draw(win, 600, 200, hflip=True)

        pygame.display.flip()
        choice_result_one, choice_result_two = choice_hierarchy(encounter_type, choice_one, choice_two, stats, npc_strength)
        cur_encounter = True
        while cur_encounter == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if option_one.isOver(pos):
                        if choice_result_one[2] == "Win":
                            item_won = item_list[random.randint(0, 3)]
                            explainer_text = "You selected the "+option_one.name+", and you won the exchange! " \
                                                                                 "So you get 2 "+item_won+"s"

                            inventory.append(item_won)
                            inventory.append(item_won)
                            cur_encounter = False
                        else:
                            item_won = item_list[random.randint(0, 3)]
                            explainer_text = "You selected the "+option_one.name+", and you lost the exchange... " \
                                                                                 "So you get 1 "+item_won
                            inventory.append(item_won)
                            cur_encounter = False
                    elif option_two.isOver(pos):
                        if choice_result_two[2] == "Win":
                            item_won = item_list[random.randint(0, 3)]
                            explainer_text = "You selected the "+option_two.name+", and you won the exchange! " \
                                                                                 "So you get 2 "+item_won+"s"
                            inventory.append(item_won)
                            inventory.append(item_won)
                            cur_encounter = False
                        else:
                            item_won = item_list[random.randint(0, 3)]
                            explainer_text = "You selected the "+option_two.name+", and you lost the exchange... " \
                                                                                 "So you get 1 "+item_won
                            inventory.append(item_won)
                            cur_encounter = False
        post_encounter = True
        while post_encounter == True:
            explain.text = explainer_text
            win.blit(bg, (0, 0))
            character.draw(win, 200, 200)
            explain.draw(win, outline=True)
            for disp in stats_display:
                disp.draw(win, outline=True)
            disp_inventory = "Inventory:;"
            for item in inventory:
                disp_inventory = disp_inventory+" "+item+";"
            inventory_to_show = Textbox((140,130,120), 800, 300, 380, 280, disp_inventory, 25)
            click_to_continue = Cardslot((0,0,0), 500, 400, 200, 75, None, False, name="Click To Continue")
            click_to_continue.draw(win, outline=True)
            inventory_to_show.draw(win, outline=True, newline_each_time = True)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if click_to_continue.isOver(pos):
                        post_encounter = False


def encounter_gen():
    # Types: 1 - Fire, 2 - Air, 3 - Water, 4 - Earth
    type_of_encounter = random.randint(1, 4)
    choice_one = 0
    choice_two = 0
    encounter = []
    if type_of_encounter == 1 or type_of_encounter == 3:
        choice_one = ["Air Choice", tan]
        choice_two = ["Earth Choice", green]
    elif type_of_encounter == 2 or type_of_encounter == 4:
        choice_one = ["Fire Choice", red]
        choice_two = ["Water Choice", lite_blue]

    if type_of_encounter == 1:
        encounter = ["Fire", red]
    elif type_of_encounter == 2:
        encounter = ["Air", tan]
    elif type_of_encounter == 3:
        encounter = ["Water", lite_blue]
    elif type_of_encounter == 4:
        encounter = ["Earth", green]

    return choice_one, choice_two, encounter


def choice_hierarchy(encounter_type, choice_one, choice_two, stats, npc_strength):
    # encounter_type is [name, color]
    if encounter_type[0] == "Fire":
        if stats[1] >= npc_strength:
            choice_one.append("Win")
        else:
            choice_one.append("Lose")
        if stats[3] >= npc_strength:
            choice_two.append("Win")
        else:
            choice_two.append("Lose")
    elif encounter_type[0] == "Air":
        if stats[0] >= npc_strength:
            choice_one.append("Win")
        else:
            choice_one.append("Lose")
        if stats[2] >= npc_strength:
            choice_two.append("Win")
        else:
            choice_two.append("Lose")
    elif encounter_type[0] == "Water":
        if stats[1] >= npc_strength:
            choice_one.append("Win")
        else:
            choice_one.append("Lose")
        if stats[3] >= npc_strength:
            choice_two.append("Win")
        else:
            choice_two.append("Lose")
    elif encounter_type[0] == "Earth":
        if stats[0] >= npc_strength:
            choice_one.append("Win")
        else:
            choice_one.append("Lose")
        if stats[2] >= npc_strength:
            choice_two.append("Win")
        else:
            choice_two.append("Lose")

    return choice_one, choice_two


def char_stats(character):
    fire_stat, air_stat, water_stat, earth_stat = random.randint(0, 4), random.randint(0, 4), random.randint(0, 4), random.randint(0, 4)
    return [fire_stat, air_stat, water_stat, earth_stat]


def start_game():
    background = "Backgrounds/Cartoon_Village.jpeg"
    pygame.display.set_caption('Gnomecraft')
    bg = pygame.image.load(background)
    screenwidth = 1200
    screenheight = 600
    win = pygame.display.set_mode((screenwidth, screenheight))
    win.blit(bg, (0, 0))
    title = Cardslot(yellow, screenwidth / 2 - 200, 100, 400, 100, None, False, name="Spirit")
    option1 = Cardslot(green, 100, 50, 200, 75, None, False, name="Talk")
    option2 = Cardslot(green, option1.x, option1.y+100, 200, 75, None, False, name="Fight")
    option3 = Cardslot(green, option2.x, option2.y+100, 200, 75, None, False, name="Keep walking")
    options = [option1, option2, option3]

    hat = Cardslot(green, 750, 150, 100, 75, None, False, name="Hat")
    head = Cardslot(green, hat.x + 110, hat.y, 100, 75, None, False, name="Head")
    brow = Cardslot(green, hat.x, head.y+90, 100, 75, None, False, name="Brows")
    nose = Cardslot(green, head.x, head.y+90, 100, 75, None, False, name="Nose")
    body = Cardslot(green, hat.x, nose.y+90, 100, 75, None, False, name="Body")
    legs = Cardslot(green, head.x, nose.y+90, 100, 75, None, False, name="Legs")
    shoe = Cardslot(green, hat.x, legs.y+90, 100, 75, None, False, name="Shoes")
    randomize = Cardslot(green, head.x, legs.y+90, 100, 75, None, False, name="Randomize")

    choose_buttons = [hat, head, brow, nose, body, legs, shoe, randomize]
    #character = pygame.image.load("Characters/Gnome General.png")  # Credit Arthur Shattan
    fhat, fhead, fbrow, fnose, fbody, flegs, fshoe = 1,1,1,1,1,1,1
    first_char = Character("gn",fhat, fhead, fbrow, fnose, fbody, flegs, fshoe)
    first_char.draw(win, 500, 50)
    #win.blit(character, (500, 50))

    for op in options:
        op.draw(win, outline=True)

    for part in choose_buttons:
        part.draw(win, outline=True)

    pygame.display.flip()
    start = False

    while start == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for choices in choose_buttons:
                    if choices.isOver(pos):
                        if choices.name == "Hat":
                            if fhat is not hat_count:
                                fhat += 1
                            else:
                                fhat = 1
                        elif choices.name == "Head":
                            if fhead is not head_count:
                                fhead += 1
                            else:
                                fhead = 1
                        elif choices.name == "Brows":
                            if fbrow is not brow_count:
                                fbrow += 1
                            else:
                                fbrow = 1
                        elif choices.name == "Nose":
                            if fnose is not nose_count:
                                fnose += 1
                            else:
                                fnose = 1
                        elif choices.name == "Body":
                            if fbody is not body_count:
                                fbody += 1
                            else:
                                fbody = 1
                        elif choices.name == "Legs":
                            if flegs is not leg_count:
                                flegs += 1
                            else:
                                flegs = 1
                        elif choices.name == "Shoes":
                            if fshoe is not shoe_count:
                                fshoe += 1
                            else:
                                fshoe = 1

                        elif choices.name == "Randomize":
                            fhat = random.randint(1, hat_count)
                            fhead = random.randint(1, head_count)
                            fbrow = random.randint(1, brow_count)
                            fnose = random.randint(1, nose_count)
                            fbody = random.randint(1, body_count)
                            flegs = random.randint(1, leg_count)
                            fshoe = random.randint(1, shoe_count)


                redraw_screen(win, choose_buttons, fhat, fhead, fbrow, fnose, fbody, flegs, fshoe, options=options, bg=background)


def redraw_screen(win, choose_buttons, fhat, fhead, fbrow, fnose, fbody, flegs, fshoe, options="", bg="", option=""):
    bg = pygame.image.load(bg)
    win.blit(bg, (0, 0))

    if options != "":
        for op in options:
            op.draw(win, outline=True)
    if option != "":
        option.draw(win, outline=True)

    for part in choose_buttons:
        part.draw(win, outline=True)

    first_char = Character("gn", fhat, fhead, fbrow, fnose, fbody, flegs, fshoe)
    first_char.draw(win, 250, 50)

    pygame.display.flip()

gnome_creator()
# start_game()