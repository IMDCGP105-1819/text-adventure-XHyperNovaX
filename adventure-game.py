#///Text-Adventure Game by Anthony Skipwith//
#//---------------------------------------//

#Quick "Tutorial"
#pick rock/stone/pebble
#throw rock/stone/pebble at window
#pick note
#go right
#go right (you don't need the key, it's just there as a red herring)
#use keypad
#type the code you got from the note
#go left
#go up
#use button

import os, time, random #os for exiting and clearing, time for waiting time, random for the randomised code

def outsideHouse(inventory): #Your starting location
    print("You're standing outside of a house, the door is right in front of you. There is a stone garden beside you with small fist sized rocks.")
    choice = "" #Empty string to save your choices in
    while True: #Constantly looping so that you can keep putting in inputs to actually play the game
        choice = input("") #Takes your input an saves it
        if choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "INVENTORY": #If the first word of the input is a synonym of inspect, and the second is someone
        #sort of amalgamation of capitals and lo wer case letters, spelling out the word "inventory" ("INVENTORY", "Inventory", "InVeNtOrY"...)
            showInventory(inventory) #then run "showInventory" with your current inventory, which will print it out for you. Similar stuff happens throughout the rest of the code
        elif choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "DOOR":
            if "key" in inventory: #If you have the key in your inventory and either open the door or go through the door's direction
                os.system("cls") #then you can enter through the door
                print("You enter through the unlocked door.")
                entrance(inventory) #and it will load the entrance room with your current inventory
            else:
                print("The door is locked, maybe you can do something with that window?") #Otherwise it tells you that it's locked and hints to the window
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in upSynonyms:
            if "key" in inventory:
                os.system("cls")
                print("You enter through the unlocked door.")
                entrance(inventory)
            else:
                print("The door is locked, maybe you can do something with that window?")
        elif choice.split(" ", 1)[0].upper() in pickUpSynonyms and choice.split()[1].upper() in stoneSynonyms: #If you go to pick up a stone
            if "stone" in inventory: #but you already have one, it will stop you. Stop picking up so many stones, you'll ruin the garden
                print("You already have a stone with you. You don't need another.")
            else: #Otherwise, sure, take a stone
                print("You pick up the stone and put it in your inventory.")
                inventory.append("stone") #The stone is now appended to your inventory
        elif choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "WINDOW":
            if "key" in inventory: #If you have the key, then you have already entered the house and as such you don't need to go through the window
                print("A broken window. The door is open, and you don't want to hurt yourself on the shards.")
            else: #Otherwise, you haven't gone inside yet, so it tells you that there's a fragile window
                print("A fragile window.")
                if "stone" in inventory: #Self explanatory to be honest
                    print("It seems like if could be broken by a certain fist sized opaque object that you may or may not have already picked up. RIP 4th wall.")
        elif choice.split(" ", 1)[0].upper() in throwSynonyms and choice.split()[1].upper() in stoneSynonyms and choice.split()[2].upper() == "AT" and choice.split()[3].upper() == "WINDOW":
            if "key" in inventory: #If the key is in your inventory, then that means that...
                print("The window is broken, and the door is open. Just use the door for goodness sake...")
            else:
                os.system("cls") #Clear the screen, say what you did, remove the rock from your inventory
                print("You throw the rock at the window, and climb through.")
                inventory.remove("stone")
                kitchen(inventory) #Load up the kitchen with your current inventory
        elif "code" in inventory and choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "CODE":
            print("The code reads: "+code) #If you have the code from the kitchen, then you can inspect it and read the code
        else:
            print("Invalid input; try 'move', 'inspect', 'throw', or 'pick'.") #Tells you you input something wrong, and gives some examples of what to try

def entrance(inventory): #Welcome to the entrance, new room that goes to all the other rooms
    print("You're standing in the main entrance to the house. There are 4 doors, entrance included.")
    if "key" not in inventory: #If there isn't a key in your inventory, you haven't picked it up yet
        print("There's a key on the table.") #so here it is
    choice = "" #Empty the choice variable so that by moving from the kitchen to the entrance you don't keep going into the living room
    while True: #Same while loop so that it repeats
        choice = input("") #Saves input
        if choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "INVENTORY":
            showInventory(inventory) #Checking inventory
        elif "key" not in inventory and choice.split(" ", 1)[0].upper() in pickUpSynonyms and choice.split()[1].upper() == "KEY":
            inventory.append("key") #If you don't have the key, and you try to pick up the key, you now have they key
            print("You picked up the key")
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in rightSynonyms:
            livingRoom(inventory) #If you try to go right, you go to the living room
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in leftSynonyms:
            kitchen(inventory) #If you try to go left, you go to the kitchen
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in upSynonyms:
            bedroom(inventory) #If you try to go up, you go to the bedroom
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in downSynonyms:
            if "key" in inventory: #If you try to go down, and you have the key, you go outside
                outsideHouse(inventory)
            else: #If you don't have they key, why are you even trying?
                print("I literally just told you there is a key there. You know this door is locked, and you don't even try to unlock it? PICK UP THE KEY!")
        elif "code" in inventory and choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "CODE":
            print("The code reads: "+code) #If you have the note, you can check it
        else:
            print("Invalid input; try 'move', 'inspect', 'throw', or 'pick'.") #Try inputting again

def kitchen(inventory): #Welcome to the kitchen, the second room you'll get to by breaking through a window
    print("You're standing in the kitchen. There is a door to your right.")
    if "code" not in inventory: #If you don't have the code yet, then it will be on the table for you to pick up
        print("There's a note on the table.")
    choice = "" #Clear choice, while loop, save input to choice, check inventory, same old same old
    while True:
        choice = input("")
        if choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "INVENTORY":
            showInventory(inventory)
        elif "code" not in inventory and choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "NOTE":
            print("There seems to be a code on the note.") #If the code isn't in your inventory, it will tell you there's a code on the note after inspecting it
        elif "code" not in inventory and choice.split(" ", 1)[0].upper() in pickUpSynonyms and choice.split()[1].upper() == "NOTE":
            print("You take the note with you. It reads; "+code) #If the code isn't in your inventory, you will pick it up and it will tell you the code
            inventory.append("code")
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in rightSynonyms:
            entrance(inventory) #If you try to go right, you go to the entrance
        elif "code" in inventory and choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "CODE":
            print("The code reads: "+code) #Check the code in your inventory
        else:
            print("Invalid input; try 'move', 'inspect', 'throw', or 'pick'.") #Try again

def livingRoom(inventory): #Living room with your current inventory
    print("You're in the living room. There's a keypad on the wall, and a TV that's turned on.")
    choice = "" #Tell where you are, clear choice, while etc etc...
    while True:
        choice = input("")
        if choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "INVENTORY":
            showInventory(inventory)
        elif choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "TV":
            print("There's nothing good on TV at the moment, just 'The Big Bang Theory'.") #If you try to watch the TV, you get a sarcastic joke. Yay.
        elif choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "KEYPAD":
            if "button" in inventory:
                print("There's nothing to do here, you've already cracked the code.")
            else:
                print("There's a 4 digit lock. You can brute force it, OR you can play the game properly.") #4th wall breaking telling you what to do
        elif choice.split(" ", 1)[0].upper() in useSynonyms and choice.split()[1].upper() == "KEYPAD":
            if "button" in inventory:
                print("There's nothing to do here, you've already cracked the code.")
            else:
                codeInput = input("You use the keypad: what code do you input? (without spaces) ") #If you try to use the keypad, you get to input the code
                if codeInput == code: #If what you input is the same as the code, which you got from the kitchen, or brute forced
                    print("The big red button the keypad falls off of it, maybe it's some sort of key?")
                    inventory.append("button") #Then you get a big red button that happens to be a key for some reason
                else:
                    print("The code was incorrect, try again.")
        elif "code" in inventory and choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "CODE":
            print("The code reads: "+code) #Inspecting the code, in case you forgot it
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in leftSynonyms:
            entrance(inventory) #If you try to go left, you go to the entrance
        else:
            print("Invalid input; try 'move', 'inspect', 'throw', or 'pick'.")

def bedroom(inventory): #Bedroom with your current inventory
    print("You are in a bedroom. There is a bed, and an empty button-shaped hole.")
    choice = "" #Same as the last rooms
    while True:
        choice = input("")
        if choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "INVENTORY":
            showInventory(inventory)
        elif choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "BED": #Inspect the bed, but it's uncomfortable so you don't waste time sleeping on it
            print("It's a bed. Well, it doesn't have a sheet or pillows, so it won't be comfortable if that's what you were thinking.")
        elif choice.split(" ", 1)[0].upper() in goSynonyms and choice.split()[1].upper() in downSynonyms:
            entrance(inventory) #If you try to go down, you go to the entrance
        elif "code" in inventory and choice.split(" ", 1)[0].upper() in inspectSynonyms and choice.split()[1].upper() == "CODE":
            print("The code reads: "+code) #Read the code from inventory
        elif "button" in inventory and choice.split(" ", 1)[0].upper() in putSynonyms and choice.split()[1].upper() == "BUTTON":
            inventory.remove("button") #Put the button in the hole and press it, then end.
            print("You put the button in the hole, and press it.") #4th wall.exe has stopped responding.
            print("You hear a fanfare. That's your prize. A fanfare.")
            print("The reason that your prize is so useless is that")
            print("You broke into someone's house and snooped around...")
            print("The intent is to provide players with a sense of pride and accomplishment for completing the game.")
            inventory.append("A sense of pride and accomplishment") #You most likely won't see this in your inventory in game, but Easter eggs, yay.
            time.sleep(15)
            os._exit(0) #Wait 15 seconds so even slow readers can finish, then end the program
        else:
            print("Invalud input; try 'move', 'inspect', 'throw', or 'pick'.")

def showInventory(inventory): #If you try to check your inventory, it will print "Inventory: | key | stone | code |" for example
    print("Inventory: | ")
    for item in inventory: #Print each item in the list, followed by " | " (space, obelisk, space; for formatting reasons)
        print(item, end = "", flush = True)

pickUpSynonyms = ["PICK", "LIFT", "COLLECT"] #Originally I tried to use syn.wordnet to import synonyms but I
throwSynonyms = ["THROW", "CHUCK", "YEET"] #couldn't install it onto my computer, so I went for simplicity instead
putSynonyms = ["PUT", "PLACE", "INSERT"]
inspectSynonyms = ["INSPECT", "LOOK" "ANALYSE"]
stoneSynonyms = ["STONE", "ROCK", "PEBBLE"]
useSynonyms = ["USE", "ACTIVATE"]
goSynonyms = ["GO", "MOVE", "WALK", "ENTER"]
upSynonyms = ["U", "UP", "NORTH", "FORWARDS"] #Instead of getting the synonyms for the cardinal directions
rightSynonyms = ["R", "RIGHT", "EAST"] #I just manually set them in a list
downSynonyms = ["D", "DOWN", "SOUTH", "BACKWARDS"]
leftSynonyms = ["L", "LEFT", "WEST"]

if __name__ == "__main__": #If the __name__ variable is equal to "__main__", which it will be, then it will run this, meaning it's the first thing to run and then will call outsideHouse(inventory)
#when needed, which is after the inventory and code are both defined
    os.system("cls") #Clears the screen
    inventory = [""] #Empty inventory at the beginning
    code = "" #Empty variable for the code to be put in
    counter = 0 #Random 4 digit number using the digits 1 through to 4
    while counter < 4:
        code = code + str(random.randint(1, 4))
        counter += 1
    outsideHouse(inventory) #Load up the starting place with your empty inventory
