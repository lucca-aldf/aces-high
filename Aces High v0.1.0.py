import random

print("Hello, and welcome to Aces High")

name=input("Please enter your name:")

print("Welcome aboard",name)

loop = True
mission = 1
in_dogfight = "N"
current_location = "menu"

#plane%d = [hitpoints, agility, attack, defense]

#F-16C stats (p=1)
plane1 = [3,7,6,5]

#Harrier stats (p=2)
plane2 = [1,2,4,4]

pilot1 = None











while loop == True:
    
    sublocation = None
    in_dogfight = None
    
    if current_location == "menu":

        print(str("This is the menu. Where would you like to head next? Options are 'dogfight', 'hangar'"))
        current_location=input(str(""))
        
    elif current_location == "dogfight":
        print("Dogfight selected")
        
        if pilot1 == None:
            print("Sorry, you don't own a plane yet. Please head to the hangar for one")
            current_location = "menu"
        
        elif mission == 1:
            print("Target spotted: a lone AV-8B Harrier II. Engage? (Y/N)")
            in_dogfight = input(str(""))
            
            if in_dogfight == "Y":
                print("Target acquired, engaging")
                ally1 = pilot1.copy()
                enemy1 = plane2.copy()
                inniciative_ally1 = 0
                inniciative_enemy1 = 0
                
                while ally1[0] != 0 and enemy1[0] != 0:
                    print("You have" , ally1[0] , "hp left")
                    print("Enemy has" , enemy1[0] , "hp left")
                    
                    while inniciative_ally1 == inniciative_enemy1:
                        inniciative_ally1 = random.randint(0,11) + ally1[1]
                        inniciative_enemy1 = random .randint(0,11) + enemy1[1]
                        
                    if inniciative_ally1 > inniciative_enemy1:
                        attack_ally1 = random.randint(0,11) + ally1[2]
                        defense_enemy1 = random.randint(0,11) + enemy1[3]
                        
                        if attack_ally1 > defense_enemy1:
                            enemy1[0] = enemy1[0] - 1
                            print("We've hit'him!")
                            print(enemy1[0],"enemy hp left")
                            
                        else:
                            print("Target missed")
                            
                    else:
                        attack_enemy1 = random.randint(0,11) + enemy1[2]
                        defense_ally1 = random.randint(0,11) + ally1[3]
                        
                        if attack_enemy1 > defense_ally1:
                            ally1[0] = ally1[0] -1
                            print("We've been hit!")
                            print(ally1[0],"hp left")
                            
                        else:
                            print("Enemy missile dodged")
                              
 
                else:
                    if ally1[0] != 0:
                        print("Dogfight won, congratulations", name)
                        current_location ="menu"
                        #mission += 1
                    elif ally1[0] == 0:
                        print("You've been shot down. Game over")
                        current_location ="menu"
                        loop = False
                    
                    
                    
                    in_dogfight = "End"
             
            elif in_dogfight == "N":
                print("Roger that " + name +", pulling off")
                current_location = "menu"
                
            else:
                print("Command not recognized, returning to menu")
                in_dogfight = "N"
                current_location = "menu"

        else:
            print("Target spotted: three AV-8B Harrier IIs. Engage? (Y/N)")
            in_dogfight = input(str(""))
            
            if in_dogfight == "Y":
                print("Target acquired, engaging")
                

    
    
    
    
    
    
    
    
    
    
            elif in_dogfight == "N":
                print("Roger that " + name +", pulling off")
                current_location = "menu"
                
            else:
                print("Command not recognized, returning to menu")
                in_dogfight = "N"
                current_location = "menu"
        
        
    elif current_location == "hangar":
        print("Hangar selected")
        print("This is the Hangar. Here you can buy new planes. Options are 'shop','return'")
        sublocation=input("")
            
        if sublocation == "shop":
            print("Shop selected")
            print("Current planes for sale: A) F-16C. Which would you like to view (use a single capital letter)?")
            planeview=input(str(""))
            
            if planeview == "A":
                print("F-16C selected")
                #print("Stats:")
                #print("Placeholder")
                print("Would you like to purchase the aircraft?(Y/N)")
                purchase=input(str(""))
                
                if purchase == "Y":
                    pilot1 = plane1.copy()
                    print("Congrats on your purchase, pilot")
                    current_location = "menu"
                    pview = "null"
                    
                elif purchase == "N":
                    print("We are sorry to hear your negative intentions. Returning to plane selection")
                    sublocation = "shop"
                    
                else:
                    print("Command not registered, returning to shop")
                    sublocation = "shop"
            else:
                print("Command not registered, returning to hangar")
                 
        elif sublocation == "return":
            current_location = "menu"
            
        else:
            print("Sorry, command not recognized")
            
    else:
        print("Sorry, command not recognized")
        current_location="menu"
        
print("Congrats, you lost it!")