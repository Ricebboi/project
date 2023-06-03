import sys

name = input("What is your name? ")

print("Welcome", name, "to the city of Dragonite.")

print(f"Driven by curiosity and the desire to face the most formidable challenges you face a choice.", name, "is met with a path to a forest and a path towards the mountains. type (Forest/Mountain)")

answer = input("Which path do you take? ")

if answer == "Forest".lower():
      print("You walk into the forest and stumble across a sword.")
      sword = input("Do you pick it up? ")

      if sword != "Yes".lower():
            print("You encounter a dragon immediately after.")
            dragon = input("You can run or fight (run/fight) ")

            if dragon != "Fight":
                   print("You decide to run and fall over a branch in the forest. The dragon breaths fire and you are burnt to ash.")
                   sys.exit()
            else:
                   print("You decided to fight the dragon. You don't have a", sword, "to fight it with. You are slain.")
                   sys.exit()
                  
      else:
            print(f"A thief confronts you right after you pick up the sword." " He yells", name, "you stole my sword! Give it back or I will take it back by force.")
      thief = input("Do you try to talk to the thief or fight him? (Talk/Fight) ")

      if thief == "Talk".lower():
              print("You explain to the thief that you had simply stumbled across the sword and had no intention of stealing it.")
              print("He says: My name is Valerian, and I am not a thief. I am actually a Dragon Warrior from Dragonite who had lost his sword battling a group of bandits.")
              warrior_choice = input("Would you like to spar with me to test your strength? (yes/no) ")
              if warrior_choice == "Yes":
                     print("You guys fight until the last breathe. He deems you a man of worthy strength. You two head back to the town together, slaying monsters in the forest. The End.")
              else:
                     print("You offend Valerian by declining his offer to test your strength. He overpowers you and slays you just like the filthy bandits before.")
                     sys(exit)



      elif thief == "Fight".lower():
              print("He was not actually a thief. He was a Dragon Warrior from Dragonite and you were slain.")
              sys.exit()
      else:
              print("Not a valid option. Type (Talk/Fight)")

elif answer == "Mountain".lower():
            print("You start the trecherous climb up the mountain. It takes hours and you stop to regain energy and eat food.")
            print("You heard tales of the Whispering Cavern hidden within the heart of the mountain.")
            print("You also notice a narrow path winding its way upward. It has a sign labeled Eagle's Peak.")

            path_choice = input("Which path do you take? (Cavern/Peak) ")

            if path_choice == "Peak".lower():
             print("You fall off")
             sys.exit()

            elif path_choice == "Cavern".lower():
              print("You reach the Cavern, and inside is a giant troll.")

            troll = input("The troll runs at you with a giant baseball bat. You must either run or fight him. (run/fight) ")
            if troll == "Run".lower():
                   print("You trip and fell over a stone running out of the", path_choice, "and the troll catches up and kills you.")
                   sys.exit()
            else:
                   print("The troll overpowers you and you are slain.")
                   sys.exit()

else:
            print("That is not a valid answer. (Cavern/Peak)")

