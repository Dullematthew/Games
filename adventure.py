def game():
    class Character:
            def __init__(self,name,health):
                self.name = name
                self.health = health
                self. inventory = []

            def show_stats(self):
                print(f"{self.name}")
                print(f"{self.health}")
                print(f"{self.inventory}")

            def add_item(self,item):
                self.inventory.append(item)
                print(f"*{item} was added to your inventory*")
    
        
    print("A Feeling of Dread")
    print("A choose your own adventure game")
    name= input("Who has come to the gates of Regal?")
    print("Terilos: Tidings ", name)
    player = Character(name, 100)
    print(f"You feel tired but healthy. your health is {player.health}")
    print(f"You check your backpack and your find it empty {player.inventory}")
    print("Terilos: You must have gotten lost to end up here, nobody has visited Regal in years.")


    # back at the gate
    def start():
        
    #died
    def died():
        died =input("Would you like to play again?").lower().strip()
        if died == "yes":
            game()
        else:
            quit()

        # wolf encounter
    def wolves():
        wolves = input("The wolves seem to aproach slowly. do you run or fight?").lower().strip()
        if wolves == "run":
            print("You try to run but the wolves are faster")
            print("what is left of your corpse is used to feed the forest")
            died()
        elif wolves == "fight":
            print("Thinking quickly you snatch up the skeletons femur, using it to bat away the approaching wolves.")
            print("They retreat, you are left at the skeleton alone")
            player.add_item("Skeleton femur")
            skeleton()
        # home encounter
    def home():
        cabin = input("The home looks weathered, the roof looks close to caving in. you hear a shifting of wood from inside. Would you like to enter? ").lower().strip()
        if cabin == "yes":
            print("You push the door open and as you do the door falls from the hinges. It falls to the floor with a thump. Inside you see the home is empty, but you do notice a doorway at the far end leading to a staircase. Would you like to descend? ")
        elif cabin == "no":
            print("Your fear overtakes you, you return to the gates of Regal")
            start()
        else: 
            print("You fear overtakes you, you return to the road.")
            home()    
    # Skeleton encounter
    def skeleton():
        skeleton = input("The skeleton looks like it has been there for a long time, would you like to APPROACH the skeleton? ").lower().strip()
        if skeleton == "yes":
            print("You aproach the skeleton and realize it hasn't been here long. You stoop to take a closer look but hear a noise from behind. While you were occupied a pair of wolves had come opon you, they attack.")
            print("Another skeleton is left on the road")
            died()
        elif skeleton == "no":
            print("a chill goes down your spine as you look upon the corpse. you decide to go back to the gates of regal")
            start()
        elif skeleton == "look around":
            print("You look around and spot movement at the edge of the forest; Wolves.")
            wolves()
        else:
            print("You become indecisive, while you ponder a pair of wolves have snuck up on you.")
            print("Another skeleton has been added to the road")
            died()
    def start():    
        # At the gates.
        print(f"You feel tired but healthy. your health is {player.health}")
        print(f"You check your backpack and you find: {player.inventory}")
        print("You look around and see a road leading to your LEFT and RIGHT running along the wall. In FRONT of you is the gate with Terilos standing beside it. BEHIND you is the forest that you had stumbled out of. ")
        choice= input("Which direction do you go?").lower().strip()
        if choice == "left":
            print("You follow the wall to the left, after what felt like half the day you stumble across a decrepit home built into the city walls.")
            home()
        elif choice == "right":
            print("You follow the wall to the right, not far from the gate you stumble across a human skeleton spread out across your path")
            skeleton()
        elif choice == "front":
            print("You step towards the gate, but Terilos raises one hand. 'woah, woah, woah. I can't let you in here without some questions first'")
        elif choice == "behind":
            print("You retreat back into the woods, your heart full of fear. In the dark of the forest you spot something out of the corner of your eye. You are to late, a creature beyond your horrors attacks")
            print("You have died")
        else:
            print("You stand still, and Terilos begins giving you a funny look")
    start()
game()



