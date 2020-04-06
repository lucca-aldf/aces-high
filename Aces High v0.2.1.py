import random
import time

print("Hello, and welcome to Aces High")

name_1 = input("Please enter your pilot's name:\n")

print(f"Welcome aboard {name_1}")
print("Before you start, you must learn some basic commands. These will work in any of the menus")
print("Balance - Shows your current balance")
print("Return - Sends you back to the previous page")
print("Menu - Goes back to the menu")

# Setting some variables
mission_level = 1
pilot_exp = [5, 8, 10, 13, 16, 20, 25, 32, 40, 50, 62, 75, 90, 110, 130]
hp_cost = 3
shp_cost = 1
agility_cost = 1
attack_cost = 1
in_dogfight = "N"
next_location = "menu"
current_location = "menu"
location_history = 0
location_levels = ["menu", "menu", "menu", "menu"]
balance = 40
purchase = "N"
skip_condition = False
class plane:
    def __init__(self, name, hp, shp, agility, attack):
        self.name = name
        self.hp = hp  # How many hits until the plane is shot down
        self.shp = shp  # How many times a 'scratch' attack has to hit to take down a hp
        self.agility = agility
        self.attack = attack

class pilot:
    def __init__(self, name, plane, hp, shp, agility, attack):
        self.name = name
        self.plane = plane
        self.hp = hp  # Bonus to plane hp
        self.shp = shp  # Bonus to plane secondary hp
        self.agility = agility  # Bonus to plane agility
        self.attack = attack  # Bonus to plane attack
        self.exp = 0
        self.level = 0
        self.sp = 0


class fighter:
    def __init__(self, pilot, allegiance):
        # Constant attributes
        self.name = pilot.name
        self.plane = pilot.plane
        self.hp = pilot.plane[1] + pilot.hp  # Primary hp, determines if plane is still flying
        self.shp = pilot.plane[2] + pilot.shp  # Secondary hp, when depleted takes away 1 primary hp

        self.agility = pilot.plane[3] + pilot.agility
        # Defines your ability to attack first and how well you can evade hits

        self.attack = pilot.plane[4] + pilot.attack
        # Must be high enough in order to inflict primary hp damage to player

        self.allegiance = allegiance  # Which side are you on. 0 is player side

        # Battle attributes, change during battle
        self.battle_hp = self.hp
        self.battle_shp = self.shp
        self.initiative = 0  # Higher initiatives attack first
        self.battle_attack = 0  # Currently useless, subject to change
        self.battle_agility = 0  # Currently useless, subject to change
        self.target = None  # Which enemy will be targetted
        self.target_acquired = False  # If fighter has target
        self.target_struck = False  # If the target was hit


# Plane list
grasshopper = ("Grasshopper", 1, 1, 1, 1)
vortexI = ("Vortex I", 2, 1, 3, 2)
vortexII = ("Vortex II", 2, 3, 3, 4)
vortexIII = ("Vortex III", 3, 3, 5, 6)

# kondorA = ("KondorA",
# khastovI = ("Khastov I",

ghost = ("Ghost", 0, 0, 0, 0)  # For keeping other allies inaccessible

# Creating player character
name_2 = "Ghost"
name_3 = "Ghost"
name_4 = "Ghost"

pilot_1 = pilot(name_1, ghost, 0, 0, 0, 0)
pilot_2 = pilot(name_2, ghost, 0, 0, 0, 0)
pilot_3 = pilot(name_3, ghost, 0, 0, 0, 0)
pilot_4 = pilot(name_4, ghost, 0, 0, 0, 0)
player_sqd = ("Player Squadron", pilot_1, pilot_2, pilot_3, pilot_4)

# Enemy list
archer_1 = fighter(pilot("Archer-1", grasshopper, 0, 0, 0, 0), 1)
archer_2 = fighter(pilot("Archer-2", grasshopper, 0, 0, 0, 0), 1)
archer_3 = fighter(pilot("Archer-3", grasshopper, 0, 0, 0, 0), 1)
archer_4 = fighter(pilot("Archer-4", grasshopper, 0, 0, 0, 0), 1)
archer_sqd = ("Archer Squadron", archer_1, archer_2, archer_3, archer_4)

tempest_1 = fighter(pilot("Tempest-1", vortexI, 0, 0, 0, 0), 1)
tempest_2 = fighter(pilot("Tempest-2", vortexI, 0, 0, 0, 0), 1)
tempest_3 = fighter(pilot("Tempest-3", vortexI, 0, 0, 0, 0), 1)
tempest_4 = fighter(pilot("Tempest-4", vortexI, 0, 0, 0, 0), 1)
tempest_sqd = ("Tempest Squadron", tempest_1, tempest_2, tempest_3, tempest_4)

obelisk_1 = fighter(pilot("Obelisk-1", vortexI, 0, 0, 0, 0), 1)
obelisk_2 = fighter(pilot("Obelisk-2", vortexI, 0, 0, 0, 0), 1)
obelisk_3 = fighter(pilot("Obelisk-3", vortexI, 0, 0, 0, 0), 1)
obelisk_4 = fighter(pilot("Obelisk-4", vortexI, 0, 0, 0, 0), 1)
obelisk_sqd = ("Obelisk Squadron", obelisk_1, obelisk_2, obelisk_3, obelisk_4)

# engel_1 = fighter(pilot("Engel-1", kondorA, 0, 0, 0, 0), 1)
# engel_2 = fighter(pilot("Engel-2", kondorA, 0, 0, 0, 0), 1)
# engel_3 = fighter(pilot("Engel-3", kondorA, 0, 0, 0, 0), 1)
# engel_4 = fighter(pilot("Engel-4", kondorA, 0, 0, 0, 0), 1)
# engel_sqd = ("Engel Squadron", engel_1, engel_2, engel_3, engel_4)

# balkush_1 = fighter(pilot("Balkush-1", khastovI, 0, 0, 0, 0), 1)
# balkush_2 = fighter(pilot("Balkush-2", khastovI, 0, 0, 0, 0), 1)
# balkush_3 = fighter(pilot("Balkush-3", khastovI, 0, 0, 0, 0), 1)
# balkush_4 = fighter(pilot("Balkush-4", khastovI, 0, 0, 0, 0), 1)
# balkush_sqd = ("Balkush Squadron", balkush_1, balkush_2, balkush_3, balkush_4)

# Enemy list
level_1_enemies = (archer_sqd, archer_sqd)
level_2_enemies = (tempest_sqd, tempest_sqd)
level_3_enemies = (obelisk_sqd, obelisk_sqd)


def battle(units, prize, penalty, exp):
    global balance
    global mission_level
    global dogfight_level

    class fighter:
        def __init__(self, pilot, allegiance):
            # Constant attributes
            self.name = pilot.name
            self.plane = pilot.plane
            self.hp = pilot.plane[1] + pilot.hp  # Primary hp, determines if plane is still flying
            self.shp = pilot.plane[2] + pilot.shp
            # Secondary hp, when depleted takes away 1 primary hp

            self.agility = pilot.plane[3] + pilot.agility
            # Defines your ability to attack first and how well you can evade hits

            self.attack = pilot.plane[4] + pilot.attack
            # Must be high enough in order to inflict primary hp damage to player

            self.allegiance = allegiance  # Which side are you on. 0 is player side

            # Battle attributes, change during battle
            self.battle_hp = self.hp
            self.battle_shp = self.shp
            self.initiative = 0  # Higher initiatives attack first
            self.battle_attack = 0  # Currently useless, subject to change
            self.battle_agility = 0  # Currently useless, subject to change
            self.target = None  # Which enemy will be targetted
            self.target_acquired = False  # If fighter has target
            self.target_struck = False  # If the target was hit

    enemies = units[random.randint(0, len(units) - 1)]
    print(f"Target spotted: {enemies[0]}. Engage? (Y/N)")
    in_dogfight = str(input("")).upper()
    if in_dogfight == "N":
        return None
    else:
        pass

    print("")

    ally_hp = 1  # Sum of allied and enemy hp. Starts at 1, later converted to the sum of the hp of each side
    enemy_hp = 1  # When either reach 0, the battle ends and the winner is declared
    all_units = []  # List of all units in the battle
    unit_list = []  # All units, sorted by initiative

    # Creating player fighters

    ally_1 = fighter(pilot_1, 0)
    ally_2 = fighter(pilot_2, 0)
    ally_3 = fighter(pilot_3, 0)
    ally_4 = fighter(pilot_4, 0)
    allies = (ally_1, ally_2, ally_3, ally_4)

    for fighter in allies:
        if fighter.plane != ghost:
            all_units.append(fighter)
        else:
            pass

    for fighter in enemies:
        if type(fighter) == str:
            pass
        else:
            all_units.append(fighter)
    # Starts counter of turn
    turn_counter = 0
    auto_turn = False
    full_skip = False

    while ally_hp != 0 and enemy_hp != 0:  # If all ally or enemy planes are eliminated, the battle ends

        # Resetting values of variables that will be added up in the end of the loop
        ally_hp = 0
        enemy_hp = 0

        # Adding agility to each fighter's initiative
        for fighter in all_units:
            if fighter.battle_hp != 0:
                fighter.initiative += fighter.agility
                unit_list.append(fighter)
            else:
                pass

        # Sorting unit_list in order of initiative
        unit_list = sorted(unit_list, key=lambda x: x.initiative, reverse=True)

        # Reversed unit_list, for deciding the target of a fighter
        target_list = sorted(unit_list, key=lambda x: x.initiative, reverse=False)
        # User actions after each turn

        # Counting 1 turn
        turn_counter += 1
        if full_skip is False:
            time.sleep(1)
            print(f"Turn {turn_counter}\n")

        while auto_turn is False:

            turn_action = str(input("Press Enter to continue, type 'hp' or 'attack order' for battle information, \
'auto' for auto playing the battle and 'skip' for skipping it to the end\n")).lower()
            if turn_action == "":
                break
            elif turn_action == "auto":
                auto_turn = True
                break
            elif turn_action == "skip":
                auto_turn = True
                full_skip = True
                break
            elif turn_action == "hp":
                print("Showing hp of fighters\n")
                for fighter in unit_list:
                    print(f"{fighter.name} health is {fighter.battle_hp, fighter.battle_shp}")
                print("")
            elif turn_action == "attack order":
                print(f"Attack order of turn {turn_counter}\n")
                for fighter in unit_list:
                    print(f"{unit_list.index(fighter)}) {fighter.name}, with {fighter.initiative} initiative")
                print("")
            else:
                print("Command not recognized, please try again")
                print("")

        for fighter in unit_list:
            if fighter.battle_hp > 0:

                target_counter = 0

                while fighter.target_acquired == False or target_counter == 0:
                    fighter.target = target_list[target_counter]
                    fighter.target_acquired = True
                    target_counter += 1

                    if target_counter == len(unit_list):
                        fighter.target_acquired = False
                        fighter.target = None
                        break

                    elif fighter.initiative <= fighter.target.initiative or fighter.allegiance == fighter.target.allegiance or fighter.target.battle_hp <= 0:
                        fighter.target_acquired = False
                        fighter.target = None

                    else:
                        break

                if fighter.target is not None:
                    if full_skip is False:
                        time.sleep(0.5)
                        print(fighter.name, "target is", fighter.target.name)

                    fighter.battle_attack = fighter.attack
                    fighter.target.battle_agility = fighter.target.agility
                    if full_skip is False:
                        time.sleep(1)

                    if fighter.battle_attack > fighter.target.battle_agility:
                        fighter.target_struck = True
                        hit_chance = int(((fighter.battle_attack / fighter.target.battle_agility) - 1) * 100)
                        hit_scan = random.randint(0, 101)
                        if hit_scan <= hit_chance:
                            fighter.target.battle_hp -= 1
                            if full_skip is False:
                                print(f"{fighter.name} has hit {fighter.target.name}, \
{fighter.target.battle_hp} hp remaining")
                            fighter.target.battle_shp = fighter.target.shp
                        else:
                            fighter.target.battle_shp -= 1
                            if fighter.target.battle_shp == 0:
                                fighter.target.battle_shp = fighter.target.shp
                                fighter.target.battle_hp -= 1
                                if full_skip is False:
                                    print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle_hp} hp remaining")
                            else:
                                if full_skip is False:
                                    print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle_shp} secondary hp remaining")

                    else:
                        hit_chance = int((1 - (fighter.battle_attack / fighter.target.battle_agility)) * 100)
                        hit_scan = random.randint(0, 101)

                        if hit_scan <= hit_chance:
                            fighter.target_struck = True
                            fighter.target.battle_shp -= 1
                            if fighter.target.battle_shp == 0:
                                fighter.target.battle_shp = fighter.target.shp
                                fighter.target.battle_hp -= 1
                                if full_skip is False:
                                    print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle_hp} hp remaining")
                            else:
                                if full_skip is False:
                                    print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle_shp} secondary hp remaining")

                        else:
                            if full_skip is False:
                                print(f"{fighter.name} has missed {fighter.target.name}")

                    fighter.target_acquired = False

                else:
                    if full_skip is False:
                        time.sleep(0.5)
                        print(fighter.name, "has no Target")

                if full_skip is False:
                    print("")
            else:
                pass

            if fighter.allegiance == 0:
                ally_hp += fighter.battle_hp

            else:
                enemy_hp += fighter.battle_hp
        for fighter in unit_list:
            if fighter.target_struck:
                fighter.initiative -= fighter.target.initiative
            else:
                pass
            fighter.target_struck = False

        unit_list = []

    time.sleep(0.75)
    for fighter in all_units:
        fighter.battle_hp = fighter.hp
        fighter.battle_shp = fighter.shp
        fighter.initiative = 0
        fighter.battle_attack = 0
        fighter.battle_agility = 0
        fighter.target = None
        fighter.target_acquired = False

    if ally_hp != 0:
        print(f"Victory in {turn_counter} turns! {prize} credits acquired and {exp} EXP gained")
        balance += prize
        pilot_1.exp += exp
        if pilot_1.exp >= pilot_exp[pilot_1.level]:
            print(f"Congratulations, {name_1} has leveled up!")

        while pilot_1.exp >= pilot_exp[pilot_1.level]:
            pilot_1.exp -= pilot_exp[pilot_1.level]
            pilot_1.level += 1
            pilot_1.sp += 1

        if dogfight_level == mission_level:
            mission_level += 1

    else:
        print(f"Defeated after {turn_counter} turns...")
        balance -= penalty


def purchase_menu(plane, cost):
    global purchase
    global pilot_1
    global next_location
    global location_history
    global location_levels

    location_history = 3
    location_levels[3] = f"{plane}"
    print(f"{plane[0]} selected")
    print(f"Stats: {plane[1]} HP, {plane[2]} SHP, {plane[3]} Agility, {plane[4]} Attack")
    print(f"Cost of aircraft: {cost} credits")
    purchase = str(input("Would you like to purchase the aircraft?(Y/N)\n")).upper()

    if purchase == "Y" and balance >= cost and pilot_1.plane != plane:

        pilot_1.plane = plane
        print("Congrats on your purchase, pilot. Head to the hangar to equip it to one of your pilots")
        next_location = "menu"
    else:
        if purchase == "Y" and not balance >= cost and pilot_1.plane != plane:
            print("Sorry, not enough money available, returning to plane selection")
        elif purchase == "N":
            print("We are sorry to hear your negative intentions. Returning to plane selection")
        elif pilot_1.plane == plane:
            print("You already own that plane, sorry")
        elif purchase == "RETURN":
            print("Returning")
        else:
            print("Command not registered, returning to selection")
        location_history = 1
        next_location = "shop"
    purchase = "N"


while True:
    if balance < 0:
        break

    elif next_location == "menu":
        location_history = 0
        current_location = "menu"
        print(str("This is the menu. Where would you like to head next? Options are 'dogfight', 'airbase'and 'debrief'"))
        next_location = str(input("")).lower()

    elif location_levels[0] == "menu" and next_location == "dogfight" and location_history == 0:
        location_history = 1
        location_levels[1] = "dogfight"
        current_location = "dogfight"
        print("Dogfight selected")
        if pilot_1.plane != ghost:
            dogfight_level = input(f"Please select mission level (1-{mission_level}) or type 'return'\n")
            try:
                dogfight_level = int(dogfight_level)
            except:
                if dogfight_level == "return":
                    print("Roger that, returning")
                    next_location = "menu"
                else:
                    next_location = "error"
            if type(dogfight_level) == int:
                if 1 <= dogfight_level <= mission_level:
                    if dogfight_level == 1:
                        battle(level_1_enemies, 15, 10, 5)
                    elif dogfight_level == 2:
                        battle(level_2_enemies, 25, 15, 12)
                    else:
                        battle(level_3_enemies, 40, 30, 20)
                    next_location = "menu"
                else:
                    print("Sorry, level not yet unlocked, please try again")
            else:
                pass
        else:
            print("Sorry, you haven't bought a plane yet. Please head to the airbase to shop for planes")
            next_location = "menu"
    elif location_levels[0] == "menu" and next_location == "airbase" and location_history == 0:
        location_history = 1
        location_levels[1] = "airbase"
        current_location = "airbase"
        print("Airbase selected")
        #print("This is the airbase. From here you can go to 'hangar' to view your aircrafts \
#and 'shop' to acquire new ones")
        print("This is the airbase. From here you can go to 'shop' to acquire new planes")
        next_location = str(input("")).lower()

    #elif location_levels[1] == "airbase" and next_location == "hangar" and location_history == 0:
        #location_history = 2
        #location_levels[2] = "hangar"
        #current_location = "hangar"
        #print("Hangar selected")
        #print("")

    elif location_levels[1] == "airbase" and next_location == "shop" and location_history == 1:
        location_history = 2
        location_levels[2] = "shop"
        current_location = "shop"
        print("Shop selected")
        print("Current planes for sale: A) Vortex I / B) Vortex II / C) Vortex III. \
Which would you like to view (use a single capital letter)?")
        next_location = str(input("")).lower()

    elif location_levels[2] == "shop" and next_location == "a" and location_history == 2:
        purchase_menu(vortexI, 30)

    elif location_levels[2] == "shop" and next_location == "b" and location_history == 2:
        purchase_menu(vortexII, 50)

    elif location_levels[2] == "shop" and next_location == "c" and location_history == 2:
        purchase_menu(vortexIII, 80)

    elif location_levels[0] == "menu" and next_location == "debrief" and location_history == 0:
        location_history = 1
        location_levels[1] = "debrief"
        current_location = "debrief"
        print("This is debrief. Here you can check on your pilots and their stats")
        print(f"{name_1} is level {pilot_1.level} , {pilot_1.exp}/{pilot_exp[pilot_1.level]}")
        print(f"Stats: +{pilot_1.hp} HP / +{pilot_1.shp} SHP / +{pilot_1.attack} ATK / +{pilot_1.agility} AGI")
        if pilot_1.sp != 0:
            choice = str(input("Would you like to proceed to level up your pilot? (Y/N)")).lower()
            if choice == "y":
                next_location = "level_up"
            else:
                while choice != "y" or choice != "n":
                    if choice == "y":
                        next_location = "level_up"
                        break
                    elif choice == "n":
                        print("Roger that, returning to menu")
                        next_location = "menu"
                        break
                    else:
                        print("Sorry, command not recognized")
                        choice = str(input("Would you like to proceed to level up your pilot? (Y/N)\n")).lower()
        else:
            next_location = "menu"
            print("Not enough points to level up, returning to menu")
    elif location_levels[1] == "debrief" and next_location == "level_up" and location_history == 1:
        location_history = 2
        location_levels[2] = "level_up"
        current_location = "level_up"
        print(f"Currently you have {pilot_1.sp} skill points to spend on {name_1}")
        print("Which stat would you like to improve?")
        print(f"HP ({hp_cost} SP) / SHP ({shp_cost} SP / ATK ({attack_cost} SP / AGI ({agility_cost} SP")
        stat_upgrade = str(input("Type a stat to improve it or 'return'\n")).lower()
        if stat_upgrade == "hp":
            if pilot_1.sp >= hp_cost:
                pilot_1.hp += 1
                pilot_1.sp -= hp_cost
            else:
                print("Sorry, not enough skill points")
        elif stat_upgrade == "shp":
            if pilot_1.sp >= shp_cost:
                pilot_1.shp += 1
                pilot_1.sp -= shp_cost
            else:
                print("Sorry, not enough skill points")
        elif stat_upgrade == "atk":
            if pilot_1.sp >= attack_cost:
                pilot_1.attack += 1
                pilot_1.sp -= attack_cost
            else:
                print("Sorry, not enough skill points")
        elif stat_upgrade == "agi":
            if pilot_1.sp >= agility_cost:
                pilot_1.agility += 1
                pilot_1.sp -= agility_cost
            else:
                print("Sorry, not enough skill points")
        elif stat_upgrade == "return":
            next_location = "return"
        else:
            next_location = "Error"

        if pilot_1.sp != 0:
            choice = str(input(f"You still have {pilot_1.sp} skill points unspent. Keep spending? (Y/N)"))
            if choice == "y":
                pass
            else:
                while choice != "y" or choice != "n":
                    if choice == "y":
                        break
                    elif choice == "n":
                        print("Roger that, returning to menu")
                        next_location = "menu"
                        break
                    else:
                        print("Sorry, command not recognized")
                        choice = str(input(f"You still have {pilot_1.sp} skill points unspent. \
Keep spending? (Y/N)")).lower()
        else:
            print("All points spent, returning to menu")
            next_location = "menu"

    elif next_location == "balance":
        print(f"Balance is {balance}")
        next_location = current_location
        location_history -= 1

    elif next_location == "return":
        if current_location == "menu":
            print("Sorry, already in menu, can't return further")
        else:
            print("Roger that, returning")
            next_location = location_levels[location_history - 1]
            location_history -= 2

    else:
        if next_location == current_location:
            print(f"Already in {next_location}")
        else:
            print("Error, location not registered, try again")
        next_location = current_location
        location_history -= 1

print("Congrats, you lost it!")
# Goodbye world
