import random
import time


print("Hello, and welcome to Aces High")

name = input("Please enter your pilot's name:\n")

print(f"Welcome aboard {name}")
print("Before you start, you must learn some basic commands. These will work in any of the menus")
print("Balance - Shows your current balance")
print("Return - Sends you back to the previous page")
#Setting global variables


#Setting some variables
mission_level = 1
in_dogfight = "N"
next_location = "menu"
current_location = "menu"
location_history = 0
location_levels = ["menu", "menu", "menu", "menu"]
balance = 0


class pilot:
    def __init__(self, name, vitality, secondary_vitality, agility, attack):
        self.name = name
        self.vitality = vitality
        self.secondary_vitality = secondary_vitality
        self.agility = agility
        self.attack = attack
        self.exp = 0
        self.level = 0

    #(Unused due to testing using only fighter objects with pilot object in it (see more further down))
#Creating player character
#pilot1 = pilot(name, 0, 0, 0, 0)

# Enemy pilot list (Unused due to testing using only fighter objects with pilot object in it (see more further down))
#rookie1 = pilot("Rookie-1", 0, 0, 0, 0)
#rookie2 = pilot("Rookie-2", 0, 0, 0, 0)
#rookie3 = pilot("Rookie-3", 0, 0, 0, 0)
#rookie4 = pilot("Rookie-4", 0, 0, 0, 0)
#rookie5 = pilot("Rookie-5", 0, 0, 0, 0)
#rookie6 = pilot("Rookie-6", 0, 0, 0, 0)

class fighter:
    def __init__(self, pilot, plane, allegiance):

        #Constant attributes
        self.name = pilot.name
        self.hp = plane[0] + pilot.vitality #Primary hp, determines if plane is still flying
        self.secondary_hp = plane[1] + pilot.secondary_vitality #Secondary hp, when depleted takes away 1 primary hp
        self.agility = plane[2] + pilot.agility #Determines your ability to attack first and how well you can evade hits
        self.attack = plane[3] + pilot.attack #Must be high enough in order to inflict primary hp damage to player
        self.allegiance = allegiance #Which side are you on. 0 is player side

        #Battle attributes, change during battle
        self.battle_hp = self.hp
        self.battle_secondary_hp = self.secondary_hp
        self.inniciative = 0 #Higher inniciatives attack first
        self.battle_attack = 0 #Currently useless, subject to change
        self.battle_agility = 0 #Currently useless, subject to change
        self.target = 0 #Which enemy will be targetted
        self.target_acquired = False


# Plane list
f16 = [3, 4, 7, 6]
harrier = [2, 4, 6, 5]
f4 = [2, 2, 4, 4]
mig_21 = [1, 1, 3, 1]

#Creating player character
pilot1_plane = f4
ally1 = fighter(pilot(name, 0, 0, 0, 0), pilot1_plane, 0)

#Enemy list
rookie1_1 = fighter(pilot("Rookie-1", 0, 0, 0, 0), mig_21, 1)
rookie2_1 = fighter(pilot("Rookie-2", 0, 0, 0, 0), mig_21, 1)
rookie3_1 = fighter(pilot("Rookie-3", 0, 0, 0, 0), mig_21, 1)
rookie4_1 = fighter(pilot("Rookie-4", 0, 0, 0, 0), mig_21, 1)
rookie5_1 = fighter(pilot("Rookie-5", 0, 0, 0, 0), mig_21, 1)
rookie6_1 = fighter(pilot("Rookie-6", 0, 0, 0, 0), mig_21, 1)
rookie7_1 = fighter(pilot("Rookie-7", 0, 0, 0, 0), mig_21, 1)
rookie8_1 = fighter(pilot("Rookie-8", 0, 0, 0, 0), mig_21, 1)

def battle(reward, *units):
    print("")
    global balance
    global mission_level

    prize = reward
    ally_hp = 1 #Sum of allied and enemy hp. Starts at 1, later converted to the sum of the hp of each side
    enemy_hp = 1 #When either reach 0, the battle ends and the winner is declared
    unit_list = []

    # To make sure hp is right at the start of the battle
    for fighter in units:
        fighter.battle_hp = fighter.hp
        fighter.battle_secondary_hp = fighter.secondary_hp

    turn_counter = 0

    while ally_hp != 0 and enemy_hp != 0:

        #if turn_counter == 0:
            #print("You have engaged the enemy. If you wish to know about the current s")




        ally_hp = 0
        enemy_hp = 0
        turn_counter += 1

        for fighter in units:
            if fighter.battle_hp != 0:
                fighter.inniciative += fighter.agility + random.randint(0, 3)
                unit_list.append(fighter)
            else:
                pass

        unit_list.sort(key=lambda x: x.inniciative, reverse=True)
        #print("Order of attack is:")
        #for fighter in unit_list:
            #print(fighter.name, fighter.inniciative)
        #input("\nPress Enter to continue\n")
        print("Targets for each aircraft are:\n")
        for fighter in unit_list:
            if fighter.battle_hp > 0:

                target_counter = 1

                while fighter.target_acquired == False or target_counter == 1:

                    try:
                        # print("debug try target")
                        fighter.target = unit_list[unit_list.index(fighter) + target_counter]
                        fighter.target_acquired = True
                        target_counter += 1

                        if fighter.inniciative == fighter.target.inniciative or fighter.allegiance == fighter.target.allegiance or fighter.target.battle_hp <= 0:
                            fighter.target_acquired = False

                        else:
                            pass

                    except:
                        fighter.target = None
                        break

                if fighter.target != None:
                    time.sleep(0.75)
                    print(fighter.name, "target is", fighter.target.name)

                else:
                    time.sleep(0.75)
                    print(fighter.name, "has no Target")


            else:
                pass
        print("")
        input("Press Enter to continue")

        for fighter in unit_list:
            time.sleep(0.75)
            if fighter.target_acquired == True and fighter.target.battle_hp != 0:
                fighter.battle_attack = fighter.attack
                fighter.target.battle_agility = fighter.target.agility
                fighter.inniciative -= fighter.target.inniciative
                #fighter.strike_counter += 1
                #fighter.target.targetted_counter += 1
                print("")

                if fighter.battle_attack > fighter.target.battle_agility:
                    hit_chance = int(((fighter.battle_attack / fighter.target.battle_agility) - 1) * 100)
                    hit_scan = random.randint(0, 101)

                    if hit_scan <= hit_chance:
                        fighter.target.battle_hp -= 1
                        print(f"{fighter.name} has hit {fighter.target.name}, {fighter.target.battle_hp} hp remaining")
                    else:
                        fighter.target.battle_secondary_hp -= 1
                        if fighter.target.battle_secondary_hp == 0:
                            fighter.target.battle_secondary_hp = fighter.target.secondary_hp
                            fighter.target.battle_hp -= 1
                            print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle_hp} hp remaining")
                        else:
                            print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle_secondary_hp} secondary hp remaining")
                        # input("Press Enter to continue")


                else:
                    hit_chance = int((1 - (fighter.battle_attack / fighter.target.battle_agility)) * 100)
                    hit_scan = random.randint(0, 101)

                    if hit_scan <= hit_chance:
                        fighter.target.battle_secondary_hp -= 1
                        if fighter.target.battle_secondary_hp == 0:
                            fighter.target.battle_secondary_hp = fighter.target.secondary_hp
                            fighter.target.battle_hp -= 1
                            print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle__hp} hp remaining")
                        else:
                            print(f"{fighter.name} has scratched {fighter.target.name}, \
{fighter.target.battle_secondary_hp} secondary hp remaining")

                    else:
                        print(f"{fighter.name} has missed {fighter.target.name}")

                fighter.target = None
                fighter.target_acquired = False

            else:
                fighter.target = None


            if fighter.allegiance == 0:
                ally_hp += fighter.battle_hp

            else:
                enemy_hp += fighter.battle_hp
        time.sleep(0.75)
        print("")
        # print("Ally hp is", ally_hp)
        # print("Enemy hp is", enemy_hp)
        # print(unit_list)

        unit_list = []

        # input("Press Enter to continue")
    time.sleep(0.75)
    for fighter in units:
        fighter.battle_hp = fighter.hp
        fighter.battle_secondary_hp = fighter.secondary_hp
        fighter.inniciative = 0
        fighter.battle_attack = 0
        fighter.battle_agility = 0
        fighter.target = None
        fighter.target_acquired = False


    if ally_hp != 0:
        print(f"Victory in {turn_counter} turns!")
        balance += prize
        mission_level += 1

    else:
        print(f"Defeated after {turn_counter} turns...")
    next_loc = current_loc = previous_loc = "menu"
    skip_end_menu = True
def dogfight_engage():
    global in_dogfight
    in_dogfight = str(input("")).upper()
    if in_dogfight == "Y":
        print("Target acquired, engaging")
    elif in_dogfight == "N":
        print("Roger that " + name + ", pulling off")
    else:
        print("Command not recognized, returning to menu")
        in_dogfight = "N"

while True:
    in_dogfight = False
    if next_location == "menu":
        location_history = 0
        current_location = "menu"
        print(str("This is the menu. Where would you like to head next? Options are 'dogfight', 'hangar'"))
        next_location = str(input("")).lower()

    elif location_levels[0] == "menu" and next_location == "dogfight":
        location_history = 1
        location_levels[1] = "dogfight"
        current_location = "dogfight"
        print("Dogfight selected")

        #Unused since F-4E is starting aircraft
        #if pilot1 == None:
            #print("Sorry, you don't own a plane yet. Please head to the hangar for one")
            #current_loc = "menu"

        if mission_level == 1:
            print("Target spotted: a lone Mig-21. Engage? (Y/N)")
            dogfight_engage()
            if in_dogfight == "Y":
                battle(50, ally1, rookie1_1)
            else:
                pass

        elif mission_level == 2:
            print("Target spotted: a trio of Mig-21s. Engage? (Y/N)")
            in_dogfight = str(input("")).upper()
            if in_dogfight == "Y":
                battle(100, ally1, rookie1_1, rookie2_1, rookie3_1)
            else:
                pass

        else:
            print("Target spotted: five Mig-21s. Engage? (Y/N)")
            in_dogfight = str(input("")).upper()
            if in_dogfight == "Y":
                battle(100, ally1, rookie1_1, rookie2_1, rookie3_1, rookie4_1, rookie5_1)
            else:
                pass
        next_location = "menu"

    elif location_levels[0] == "menu" and next_location == "hangar":
        location_history = 1
        location_levels[1] = "hangar"
        current_location = "hangar"
        print("Hangar selected")
        print("This is the Hangar. Here you can buy new planes. Options are 'shop','return'")
        next_location = str(input("")).lower()

    elif location_levels[1] == "hangar" and next_location == "shop":
        location_history = 2
        location_levels[2] = "shop"
        current_location = "shop"
        print("Shop selected")
        print("Current planes for sale: A) F-16C. Which would you like to view (use a single capital letter)?")
        next_location = str(input("")).lower()



    elif location_levels[2] == "shop" and next_location == "a":
        location_history = 3
        location_levels[3] = "a"
        print("F-16C selected")
        # print("Stats:")
        # print("Placeholder")
        print("Would you like to purchase the aircraft?(Y/N)")
        purchase = str(input("")).upper()

        if purchase == "Y" and balance >= 50:

            pilot1_plane = f16
            print("Congrats on your purchase, pilot")
            next_loc = "menu"
        else:
            if purchase == "N" and not balance >= 50:
                print("Sorry, not enough money available, returning to plane selection")
            elif purchase == "N":
                print("We are sorry to hear your negative intentions. Returning to plane selection")
            else:
                print("Command not registered, returning to selection")
        purchase = "N"

    elif next_location == "balance":
        print(f"Balance is {balance}")
        next_location = current_location

    elif next_location == "return":
        print("Returning")
        next_location = location_levels[location_history - 1]


    else:
        print("Error, location not registered, try again")
        next_location = current_location





print("Congrats, you lost it!")