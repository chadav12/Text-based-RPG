# Charles Davis
# Game: Adventure Chronicles: Dungeons
import random
import time

# Rooms map list
Rooms = {
    "Entrance": {"East": "Great Hall"},
    "Great Hall": {"North": "Northern Hallway", "South": "Southern Hallway", "East": "Armory"},
    "Northern Hallway": {"West": "Prison Room", "East": "Grand Room"},
    "Southern Hallway": {"East": "Library", "North": "Great Hall"},
    "Armory": {"West": "Great Hall"},
    "Library": {"West": "Southern Hallway"},
    "Prison Room": {"East": "Northern Hallway"},
    "Grand Room": {"West": "Northern Hallway", "South": "Boss Room"}}

# Players inventory
inventory = ["Potion"]
Key_items = []
# Game constant states, stored for use for later.
game_state = {"monster_defeated": False,
              "Monster2_defeated": False,
              "library_Chest": False,
              "Prison_Room": False}
# Player stats
Yigas = {"HP": 100,
         "attack": 15}

# Enemy stats
monster1 = {"HP": 45,
            "attack": 5,
            "magic": 10}

monster2 = {"HP": 60,
            "attack": 10,
            "magic": 20}

boss = {"HP": 200,
        "attack": 10,
        "magic": 12,
        "shimmering blade": 15,
        "ULT": 200}

# Introduction to the reasoning behind this project...
print("Welcome to my Python project showcase! \nThis collection of projects demonstrates "
      "my skills and knowledge in Python programming, \nhighlighting my ability to design, develop,"
      "and deploy efficient and effective solutions.")

i = "-"
print(i * 45)

# Text base game name
print("Adventure Chronicles!")
print(i * 45)


# Introduction dialog
def intro():
    # plot, where the setting takes place
    print("There was once a young warrior named Yigas.")
    line = input("Press enter to continue...")
    print("He hailed from the east of the castle of Alamar.")
    line = input("Press enter to continue...")
    print("His town was destroyed by the empire of Lunaria, \nso he traveled to the kingdom to fight the oppressors.")
    line = input("Press enter to continue...")
    print("Once arrived at the kingdom, he was met with the royal king's guard to escort him to the palace.")
    line = input("Press enter to continue...")
    print("The king met him and asked him if he wanted to join the fight for a better world?")
    line = input("Press enter to continue...")
    print("Yigas as he kneels before the king says that \nhe wishes to prove his worth and join the fight")
    line = input("Press enter to continue...")
    print(
        "The king stands above and tells the young warrior, \nif you want to join, you must pass the Trial of Heroes!")
    line = input("Press enter to continue...")
    print("Yigas without a beat says he would do the trial to prove his worth!")
    line = input("Press enter to continue...")
    print("The king then leads him downstairs to the darkest \npits beneath the castle to navigate the dungeon.")
    line = input("Press enter to continue...")
    print("The king tells Yigas there is a beast down here which will kill all who enters its sanctum.")
    line = input("Press enter to continue...")
    print("Go fourth through the dungeon and find this beast and slay him!")
    line = input("Press enter to continue...")
    print("Yigas agrees and sets fourth inside only armed with a shield and a sword\n, to the unknown...")
    final_line = input("Press enter to continue...")
    entrance()  # Moving to the start of the game


# Entrance
def entrance():
    print("You are at the entrance")
    movement = input("Which direction do you want to go? east? exit: ")  # Option to move to east or west
    if movement == "east":
        great_hall()
    elif movement == "exit":
        print("Yigas lowered his head and return back from where he came from.")
        line = input("Press enter to continue...")
        print("He returns and the king raises his hand calling him a coward!")
        line = input("Press enter to continue...")
        print("Yigas walks as he hangs his head in shame for what he did.")
        exit()
    else:
        print("Invalid command")
    return entrance()


# great hall
def great_hall():
    print("You arrived at the Great Hall.")
    # Defining which movement
    movement = input(
        "Which direction do you want to go? east? west? north? south?: ")  # Option to move east west north south
    if movement == "east":
        if game_state["monster_defeated"] == True:  # if the game state is set to true, then the return is not possible
            print("There is nothing more in that room")
            great_hall()
        else:
            armory()  # if the game state is false, the return is movement to the armory
    elif movement == "west":
        entrance()
    elif movement == "south":
        southern_hallway()
    elif movement == "north":
        northern_hallway()
    else:
        print("Invalid command")
        return great_hall()


# Armory
def armory():
    print("You have arrived at the Armory.")
    line = input("Press enter to continue...")
    print("You see a chest with a red band around it.")
    line = input("Press enter to continue...")
    chest_option1 = input("Do you open the chest? Yes? No?").lower()
    # Defines which option, yes or no
    if chest_option1 == "yes":  # Input the chest option
        print("Monster appears!!!")
        line = input("Press enter to continue...")
        print(f"Yigas HP {Yigas}")
        print("-" * 10)
        print(f"Vampire Bat {monster1}")

        # Battle Scene!
        while True:
            command = (input(f"input command. Attack = 1: Item = 2: inventory = {inventory}"))
            if command == "1":
                monster1["HP"] -= Yigas["attack"]
                print(f"Vampire bat takes {Yigas["attack"]} damage")
                print(f"Vampire bat HP: {monster1["HP"]}")
                # Monsters turn
                if monster1["HP"] > 0:
                    random_action = random.randint(1, 2)  # Imports the random function to used for enemy AI
                    if random_action == 1:
                        print("Vampire Bat attacks!!!")
                        print(f"Yigas takes {monster1["attack"]} damage!")
                        Yigas["HP"] -= monster1["attack"]
                        print(f"Yigas has {Yigas["HP"]} HP!")
                        # Game over condition
                        if Yigas["HP"] <= 0:
                            print("Yigas defeated! Game over.")
                            intro()
                    elif random_action == 2:
                        print("Vampire Bat uses Fire!!!")
                        print(f"Yigas takes {monster1["magic"]} damage!")
                        Yigas["HP"] -= monster1["magic"]
                        print(f"Yigas has {Yigas["HP"]} HP!")
                        # Game over condition
                        if Yigas["HP"] <= 0:
                            print("Yigas defeated! Game over.")
                            intro()
                # Defeating the Vampire bat
                else:
                    print("You defeated the Vampire Bat!")
                    time.sleep(3)
                    print("You obtained 1 potion")
                    time.sleep(2)
                    print('Yigas says, "There is no reason to be in this room no more"')
                    inventory.append("Potion")
                    del Rooms["Armory"]
                    game_state["monster_defeated"] = True
                    great_hall()
            elif command == "2":
                Yigas["HP"] += 20
                inventory.remove("Potion")
                print("Yigas uses Potion!")
                print(f"Yigas HP: {Yigas['HP']}")
            else:
                print("Invalid command")
                continue
    elif chest_option1 == "no":  # Input the chest option no
        print("Yigas senses that this may be a trap and turns to exit")
        great_hall()
    else:
        print("Invalid command")
        return armory()


# Southern Hallway connects to the library
def southern_hallway():
    print("You have arrived at the southern hallway...")
    movement = input("Which direction do you want to go? east? north?: ")  # Option set to go either east or north
    if movement == "north":
        great_hall()
    elif movement == "east":
        if game_state["library_Chest"] == True:  # if the game state is true then the player can not return to the room
            print("There is nothing more in that room")
            southern_hallway()
        else:
            library()  # If the game state is false then the return is moving forward
    else:
        print("Invalid command")


# Library
def library():
    print("You arrived at the library")
    time.sleep(1)
    print("You see many fascinating books in the library.")
    time.sleep(1)
    print("You see a wooden chest at the corner of the room")
    line = ("Press enter to continue...")

    # Opening the chest sequence
    while True:
        # Input if you want to open the chest or not...
        chest_library = input("Do you want to open the chest? Yes or No?: ").lower()  # Option to open or not

        if chest_library == "yes":
            print("You found a potion inside!")
            time.sleep(1)
            print("You put the potion in your inventory.")
            inventory.append("Potion")
            del Rooms["Library"]
            game_state["library_Chest"] = True
            southern_hallway()
        elif chest_library == "no":
            print("You have an erie feeling about the chest so Yigas leaves it alone...")
            southern_hallway()
        else:
            print("Invalid command")


# Northern Hallway
def northern_hallway():
    print("Yigas arrives at the northern hallway.")
    time.sleep(2)
    movement = input(
        "Which direction do you want to go? east? west? south?: ").lower()  # Choose which direction to go east west south
    if movement == "south":
        great_hall()
    elif movement == "west":
        if game_state["Prison_Room"] == True:  # If the game state is true then the player can not return to the room
            print("No reason to return to that room again...")
            northern_hallway()
        else:
            prison_room()  # if the game state is false then the player will proceed
    elif movement == "east":
        grand_room()
    else:
        print("Invalid command")


def prison_room():
    print("Yigas arrives at the prison_room.")  # Dialog for the room
    line = input("Press enter to continue...")
    print("Yigas looks up and a monster appears!!!")
    line = input("Press enter to continue")
    print("Yigas draws his blade and prepares for battle...")
    line = input("Press enter to continue.")
    print(f"Yigas HP: {Yigas}")
    print("-" * 10)
    print(f"Scorpion: {monster2}")
    # Battle Scene!!!
    while True:
        if Yigas["HP"] <= 0:
            print("Yigas defeated! Game over.")
            intro()
        command = (input(f"input command. Attack = 1: Item = 2: inventory = {inventory}"))
        if command == "1":
            print("Yigas attacks with his sword!")
            monster2["HP"] -= Yigas["attack"]
            print(f"Scorpion takes {Yigas["attack"]} damage")
            print(f"Scorpion HP: {monster2["HP"]}")
            if monster2["HP"] > 0:
                random_command = random.randint(1, 3)  # used for the enemy AI
                if random_command == 1:
                    Yigas["HP"] -= monster2["attack"]
                    print(f"Scorpion attacks yigas dealing {monster2["attack"]} damage!")
                    print(f"Yigas has {Yigas["HP"]} HP")
                    if Yigas["HP"] <= 0:
                        print("Yigas defeated! Game over.")
                        intro()
                elif random_command == 2:
                    Yigas["HP"] -= monster2["magic"]
                    print(f"Scorpion uses Earth Shatter dealing {monster2["magic"]} damage!")
                    print(f"Yigas has {Yigas["HP"]} HP")
                    if Yigas["HP"] <= 0:
                        print("Yigas defeated! Game over.")
                        intro()
                elif random_command == 3:

                    print(f"Scorpion leaps into the air, Yigas prepares for his next move...")
                    time.sleep(1)
                    print(f"Scorpion lunges down preparing to use its might stinger")

                    # This is a quick time event commonly seen in video games
                    while True:
                        evasive_command = (input(
                            "What should Yigas do? \nRaise his shield to defend? = 1\n Or Dodge the incoming attack? = 2: "))
                        if evasive_command == "1":
                            super_sting = 45
                            Yigas["HP"] -= super_sting
                            print(
                                f"Yigas attempts to dodge the attack but the stinger got him dealing {super_sting} damage!")
                            time.sleep(4)
                            print(f"Yigas has {Yigas["HP"]} remaining...")
                            break
                        elif evasive_command == "2":
                            strike = 5
                            monster2["HP"] -= strike
                            print("Yigas blocks the attack swiftly then with quick force,\n Strikes the scorpion!")
                            print(f"Scorpion takes {strike} damage")
                            print(f"Scorpion has {monster2["HP"]}")
                            break
                        else:
                            print("Invalid command...")
            elif monster2["HP"] <= 0:
                game_state["Prison_Room"] = True
                print("Scorpion fell down dead after Yigas preformed his final blow")
                time.sleep(4)
                print("Yigas obtains a potion from the enemy!")
                inventory.append("Potion")
                print("Yigas sees a Golden Chest in the room...")
                time.sleep(4)
                print("He opens the chest to find the key that would open the inner sanctum...")
                Key_items.append("key")  # Key item needed to enter the final room
                time.sleep(4)
                print("Yigas turns around with key in hand and walks to the northern hallway...")
                northern_hallway()  # Returning back to the previous hallway

        # Potion
        elif command == "2":
            Yigas["HP"] += 25
            inventory.remove("Potion")
            print("Yigas uses Potion!")
            print(f"Yigas HP: {Yigas['HP']}")
        else:
            print("Invalid command")
            continue


def grand_room():
    print("Yigas arrived at the grand room...")
    time.sleep(2)
    print("This is the room before the inner sanctum.")
    time.sleep(2)
    print("Yigas sees that there is a keyhole to the door leading to the inner sanctum.")
    if "key" in Key_items:
        print("Yigas takes out the key and puts it in the slot\n and turns it slowly to open the door")
        print("As the door opens, Yigas walks inside the inner sanctum ready for the challenge to come...")
        boss_room()
    else:
        print("Yigas does not yet posses the key to enter, he turns around and returns to the northern hallway")
        northern_hallway()


# Final Boss room
def boss_room():
    Yigas["HP"] = 100
    print("Yigas walks into the boss room with his sword drawn.")  # dialog
    line = input("Press enter to continue")
    print('"Welcome to your doom..."')
    line = input("Press enter to continue")
    print("A voice echoes through the large area and from the darkness a loud BOOM erupted")
    line = input("Press enter to continue")
    print('"What the heck was that!", Yigas screams.')
    line = input("Press enter to continue")
    print("A warrior who looked undead carrying 2 sabers, one in each hand approaches")
    line = input("Press enter to continue")
    print('"Are you the one of whom I am to test?"')
    line = input("Press enter to continue")
    print('Yigas raises his blade to the horrific looking fiend and says, "Yes I am! Come and get it!"')
    line = input("Press enter to continue")
    print("The undead beast approaches Yigas as Yigas approaches the fiend ready to do battle.")
    line = input("Press enter to continue")
    print('"Let us begin, young Yigas."')
    print(f"Yigas HP: {Yigas}")
    print("-" * 10)
    print(f"Undead Warrior: {boss}")
    while True:  # Battle scene!
        if Yigas["HP"] <= 0:
            print("Yigas defeated! Game over.")
            intro()
        command = (input(f"input command. Attack = 1: Item = 2: inventory = {inventory}: "))
        if command == "1":
            boss["HP"] -= Yigas["attack"]
            print(f"Yigas attacks dealing {Yigas["attack"]} damage")
            print(f"The boss has {boss["HP"]} left")
            if boss["HP"] >= 100:
                random_attack = random.randint(1, 3)
                print("Ha ha ha! My turn fool!")
                if random_attack == 1:
                    Yigas["HP"] -= boss["attack"]
                    print(f"The undead monster strikes Yigas dealing {boss["attack"]} damage")
                    print(f"Yigas has {Yigas["HP"]} left")
                elif random_attack == 2:
                    Yigas["HP"] -= boss["magic"]
                    print(f"The undead monster summons a energy blast dealing {boss["attack"]} damage!")
                    print(f"Yigas has {Yigas["HP"]} left")
                elif random_attack == 3:
                    Yigas["HP"] -= boss["shimmering blade"]
                    print(f"The undead monster unleashes a barrage of attacks dealing {boss["attack"]} damage")
                    print(f"Yigas has {Yigas["HP"]} left")

                    # Dialogue before the final scene
            if boss["HP"] <= 100:
                print('"I give you credit warrior, You are better than I expected."')
                time.sleep(2)
                print("Yigas panting and out of breathe from the intense fight stands there ready for the next move")
                time.sleep(2)
                print('"ha ha ha ha, it is over Yigas... Get ready for my ultimate attack!"')
                time.sleep(2)
                print("The undead warrior jumps in the air and prepares for the final blow.")
                time.sleep(2)
                print('"ULT!!!!!!"')
                time.sleep(2)
                print("A massive energy blast is hurled toward Yigas, there is no way for him to dodge it.")
                print("The energy blast got near and in an instant. Everything disappeared in that moment")
                line = input("Press enter to continue...")
                print("Yigas, in the darkness thinking that he has met his end, heard a voice.")
                line = input("Press enter to continue...")
                print('"Yigas..."')
                line = input("Press enter to continue...")
                print('"Yes, Who is there?"')
                line = input("Press enter to continue...")
                print('"It is I, The planet of where you live on. I bless you with the gift of power..."')
                line = input("Press enter to continue...")
                print('"Here... I grant you the power forge! Use it and defeat '
                      '\nyour enemy and restore peace to the world"')
                line = input("Press enter to continue...")
                print("In that moment, A bright heavenly light surrounds "
                      "\nYigas as he feels the power surging through him")
                line = input("Press enter to continue...")
                print("Yigas returns to the world and he deflects that massive blast")
                line = input("Press enter to continue...")
                print('"What the heck just happened?",  The undead warrior said.')
                line = input("Press enter to continue...")
                print('"I have real power now, Prepare to die!"')
                final_fight()
                break
        elif command == "2":
            Yigas["HP"] += 25
            inventory.remove("Potion")
            print("Yigas uses Potion!")
            print(f"Yigas HP: {Yigas['HP']}")
        else:
            print("Invalid command")

# Final conflict
def final_fight():
    Yigas["HP"] += 900 # Yigas gains 900 health but the battle is set to stack in his favor
    print("Yigas gained 900 health!")
    print(f"Yigas has {Yigas["HP"]} HP")
    print("_" * 10)
    print(f"Undead Warrior has {boss["HP"]}")
    # Battle Mode finale
    while True:
        # Commands for Yigas
        command = (input(f"input command. Attack = 1: Item = 2: inventory = {inventory}: Blasto = 3: Shockwave = 4: "))
        if command == "1":
            boss["HP"] -= Yigas["attack"]
            print(f"Yigas attacks dealing {Yigas["attack"]} damage")
            print(f"The boss has {boss["HP"]} left")
        elif command == "2":
            Yigas["HP"] += 25
            inventory.remove("Potion")
            print("Yigas uses Potion!")
            print(f"Yigas HP: {Yigas['HP']}")
        elif command == "3":
            boss["HP"] -= 60
            print(f'Yigas Leaps in the air summons a massive ball of energy "Blasto!!!!" dealing 60 damage.')
            print(f"The boss has {boss["HP"]} left")
            print("The undead warrior got knocked back against the wall.")
        elif command == "4":
            boss["HP"] -= 60
            print(
                f'Yigas Leaps in the air then crashing his blade to the ground sending a shockwave dealing 60 damage.')
            print(f"The boss has {boss["HP"]} left")
            print("The undead warrior got knocked back against the wall.")
        else:
            print("Invalid Command...")
            continue
            # after the boss has 0 HP, the conflict ends
        if boss["HP"] <= 0:
            print("The undead monster has been defeated.")
            time.sleep(4)
            print("Yigas turns to walk back out the door when he heard a voice.")
            time.sleep(4)
            print('"You will too, one day too slip into darkness..."')
            line = input("Press enter to continue")
            print("Yigas sighs as he knows his destiny will not be an easy one")
            line = input("Press enter to continue")
            print("He returns to the throne room as the king welcomes him back")
            line = input("Press enter to continue")
            print('"You have came back my brave warrior, now are you ready?"')
            line = input("Press enter to continue")
            print('"Yes your majesty... I am ready to take on the kingdom of Lunaria!"')
            line = input("Press enter to continue")
            exit()


intro()
