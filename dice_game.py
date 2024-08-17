import random
import time

dice_dictionary = {
    1: (
        "┌─────┐\n"
        "│     │\n"
        "│  •  │\n"
        "│     │\n"
        "└─────┘"
    ),
    2: (
        "┌─────┐\n"
        "│ •   │\n"
        "│     │\n"
        "│   • │\n"
        "└─────┘"
    ),
    3: (
        "┌─────┐\n"
        "│ •   │\n"
        "│  •  │\n"
        "│   • │\n"
        "└─────┘"
    ),
    4: (
        "┌─────┐\n"
        "│ • • │\n"
        "│     │\n"
        "│ • • │\n"
        "└─────┘"
    ),
    5: (
        "┌─────┐\n"
        "│ • • │\n"
        "│  •  │\n"
        "│ • • │\n"
        "└─────┘"
    ),
    6: (
        "┌─────┐\n"
        "│ • • │\n"
        "│ • • │\n"
        "│ • • │\n"
        "└─────┘"
    )
}

def compare(computer_sum, player_sum):
    if computer_sum == player_sum:
        print("---------")
        print("Egaliate!")
        print("---------")
        return 0,0,"Egal"
    elif computer_sum > player_sum:
        print("-----------")
        print("Ai pierdut!")
        print("-----------")
        return 1,0,"Pierdut"
    else:
        print("------------")
        print("Ai castigat!")
        print("------------")
        return 0,1,"Castigat"

def dice_play():
    print("Castiga cine da zarul mai mare sau cine da dubla!")
    computer_score = 0
    player_score = 0
    history = []
    while True:
        message = None
        while message != "da" and message != "nu":
            message = input("Continui jocul?(Da/Nu): ").lower()
        
        if(message == "nu"):
            print("-----------------------------------------------------")
            print("Jocul s-a terminat!")
            print("Scorul final este: Computer - Player: " + str(computer_score) + "-" + str(player_score))
            print("Istoricul meciurilor: ", end="")
            
            if not history:
               print("Nu s-a jicat niciun meci!")
            else:
               print(", ".join(history))
    
            print("-----------------------------------------------------")
            game()
            break
        
        elif(message == "da"):

            computer_random_number1 = random.randint(1, 6)
            computer_random_number2 = random.randint(1, 6)
            computer_sum = computer_random_number1 + computer_random_number2
            
            print("--------------------------")
            print("Computer:")
            print(list(dice_dictionary.values())[computer_random_number1-1])
            print(list(dice_dictionary.values())[computer_random_number2-1])
            print("--------------------------")
            
            time.sleep(2)
            
            player_random_number1 = random.randint(1, 6)
            player_random_number2 = random.randint(1, 6)
            player_sum = player_random_number1 + player_random_number2
            
            print("--------------------------")
            print("Player:")
            print(list(dice_dictionary.values())[player_random_number1-1])
            print(list(dice_dictionary.values())[player_random_number2-1])
            print("--------------------------")
            
            time.sleep(1)
            
            if computer_random_number1 == computer_random_number2 and player_random_number1 != player_random_number2:
                print("-----------")
                print("Ai pierdut!")
                print("-----------")
                history.append("Pierdut")
                computer_score += 1
            elif computer_random_number1 != computer_random_number2 and player_random_number1 == player_random_number2:
                print("------------")
                print("Ai castigat!")
                print("------------")
                history.append("Castigat")
                player_score += 1
            elif computer_random_number1 == computer_random_number2 and player_random_number1 == player_random_number2:
                
                return_cs, return_ps, return_msg = compare(computer_sum, player_sum)
                computer_score += return_cs
                player_score += return_ps
                history.append(return_msg)
                
            else:
                
                return_cs, return_ps, return_msg = compare(computer_sum, player_sum)
                computer_score += return_cs
                player_score += return_ps
                history.append(return_msg)
            
            time.sleep(1)
            print("----------------------------------")
            print("Computer - Player: " + str(computer_score) + "-" + str(player_score)) 
            print("----------------------------------")
            print()
            
            message = None

def higher_lower_game():
   computer_score = 0
   player_score = 0
   history = []
   print("--------------------------")
   print("Vezi zarul computer-ului, apoi alegi Higher daca consideri ca suma zarurilor tale va fi mai mare sau Lower in caz contrat. Castigi daca ai ghicit!")
   while True:
       message = None
       while message != "da" and message != "nu":
           message = input("Continui jocul?(Da/Nu): ").lower()
       
       if message == "nu":
           print("-------------------------------------------")
           print("Jocul s-a terminat!")
           print("Scorul final este: Computer - Player: " + str(computer_score) + "-" + str(player_score))
           print("Istoricul meciurilor: ", end="")
           
           if not history:
               print("Nu s-a jicat niciun meci!")
           else:
               print(", ".join(history))
           
           print("-------------------------------------------")
           game()
           break
       
       elif message == "da":
           computer_random_number1 = random.randint(1, 6)
           computer_random_number2 = random.randint(1, 6)
           computer_sum = computer_random_number1 + computer_random_number2
           
           print("Computer:")
           print(list(dice_dictionary.values())[computer_random_number1-1])
           print(list(dice_dictionary.values())[computer_random_number2-1])
           print("Suma zarurilor este " + str(computer_sum))
           print("--------------------------")
           
           higher_lower = None
           while higher_lower != "higher" and higher_lower !="lower":
               higher_lower = input("Higher sau Lower?: ").lower()
           
           player_random_number1 = random.randint(1, 6)
           player_random_number2 = random.randint(1, 6)
           player_sum = player_random_number1 + player_random_number2
           
           print("Player:")
           print(list(dice_dictionary.values())[player_random_number1-1])
           print(list(dice_dictionary.values())[player_random_number2-1])
           print("Suma zarurilor este " + str(player_sum))
           time.sleep(2)
           
           if higher_lower == "lower" and player_sum < computer_sum:
               print("-------------")
               print("Ai castigat!")
               print("-------------")
               history.append("Castigat")
               player_score += 1
           elif higher_lower == "lower" and player_sum > computer_sum:
               print("-------------")
               print("Ai pierdut")
               print("-------------")
               history.append("Pierdut")
               computer_score += 1
           elif higher_lower == "higher" and player_sum > computer_sum:
               print("-------------")
               print("Ai castigat!")
               print("-------------")
               history.append("Castigat")
               player_score += 1
           elif higher_lower == "higher" and player_sum < computer_sum:
               print("-------------")
               print("Ai pierdut")
               print("-------------")
               history.append("Pierdut")
               computer_score += 1
           else:
               print("-------------")
               print("Egalitate!")
               print("-------------")
               history.append("Egal")
           print("Computer - Player: " + str(computer_score) + "-" + str(player_score)) 
           print("--------------------------")
    
def game():    
    start_message = None
    while start_message != "1" and start_message != "2" and start_message != "3":
        print("--------------------------")
        print("Jocuri disponibile:")
        print("1.Dice Roll")
        print("2.Higher/Lower")
        print("3.Exit")
        start_message = input("Alege jocul dorit(1/2/3): ")
        print("--------------------------")
        
    if start_message == "1":
        dice_play()
    elif start_message == "2":
        higher_lower_game()
    elif start_message == "3":
        print("Ai parasit meniul!")
    
game()