# THE game "Donut Dream"
import random

def start_game():
    '''
    The function welcomes the user,
    asks him/her to type in nickname]'
    
    And it checks if the nickname was entered
    '''
    # Welocome screen that asks you to type in your name
    input("===       WELCOME      === ")
    input("To the RPG game Donut Dream!")
    input("You will now experience the sugar overdose and chill vibes!")
    input("===     Press enter    === ")
    print()
    nickname = input("Please, enter your name: \n>>> ")
    # An infinite while loop breaks only when you typed in your name
    while True:
        if nickname == "":
            nickname = input("You didn't enter a nickname. Please, enter your name: \n>>> ")
            continue
        break
    return nickname

def rand_num_game():
    '''
    The function that generates the password,
    converts each number of it to binary and
    makes player to guess the original numbers

    >>> rand_num_game()
    You look at the password pannel

    The door generates a random password. It consists of four numbers
    Guess the password if it is printed in binary

    Enter the password where each number is seperated with space:

    0001
    1001
    0101
    1001
    >>> 1 9 5 9

    The infinite while loop breaks only when entered number is the password
    that was shown in binary
    The password changes every 3 wrong guesses
    '''
    # Setting the list of numbers that generate the password
    one_ten = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    password = ""
    # Asking the player to enter the password
    input("You look at the password pannel")
    print()
    input("The door generates a random password. It consists of four numbers")
    input("Guess the password if it is printed in binary")
    print()
    
    # Checking whether 4 numbers are typed in
    cont = True
    while cont:
        # Generening the random password
        for e in range(4):
            password = str(random.choice(one_ten)) + password
        for r in range(4):
            element = int(password[r])
            element = bin(element)[2:].zfill(4)
            print(element)
        # Checking if you entered the right password in three attempts
        for i in range(3):
            # A bool that help to check whether you entered numbers correctly
            check_four = True
            while check_four:
                try:
                    # Asking the player to enter numbers
                    guess1, guess2, guess3, guess4 = input("Enter the password where each number is seperated with space: \n>>> ").split()
                    print()
                    check_four = False
                except ValueError:
                    # If the player didn't enter numbers correctly
                    print("You didn't enter four numbers or didn't space it. Please try again")
                    check_four = True
                    continue
                if guess1.isalpha() is False and guess2.isalpha() is False\
                    and guess3.isalpha() is False and guess4.isalpha() is False and \
                    len(guess1) == 1 and len(guess2) == 1 and len(guess3) == 1 and len(guess4) == 1:
                    check_four = False
                    pass
                else:
                    print("You didn't enter four numbers or didn't space it. Please try again")
                    check_four = True
            # Checking the numbers with if-else functions
            # If you entered the right number the while loop breaks
            if guess1 == password[0] and guess2 == password[1] and guess3 == password[2] and guess4 == password[3]:
                input("The dook is unlocked! You go to bed")
                cont = False
            else:
                # If the number was incorrect then the while loop continues
                input("Your Guess was incorrect :(")
                attempts = 2 - i
                print("You have", attempts, "attempts left.", end = "")
                if attempts == 0:
                    print()
                    print
                    input("Sorry, the password has changed now. You have used all attempts. Here is your reset password in binary: ")
                    print()
                    cont = True
                    break
                else:
                    print()
            if cont != True:
                break
# Random number function end
                
                
def first_act(health, points, nickname):
    '''
    The first act

    A lot of inputs present the plot of the game to the player
    Also, along the way the choices are given to the player
    All of them lead to one outcome but with different concequences to the player

    The choices that the player make are in while loops and they break only when the choice that exists is chosen
    '''
    # Inputs that present the game script
    print()
    input("Late night, {} has fallen asleep. But then you go to your fridge and realise that all donuts have been eaten. Press enter".format(nickname))
    input("You’ve eaten them all")
    input("Your depression strikes because you can’t eat anything sweet")
    print()
    input("Press Enter to see your actions: ")
    print()
    input("1. Go to sleep (start the game)")
    input("2. Go outside")
    print()
    # The first choice of actions
    your_action_1 = input("Enter the number of an action: \n>>> ")
    print()
    # The infinite loop breaks if you entered the right action
    while True:
        # The script if you have chosen 1
        if your_action_1 == "1":
            input("\"Oh my God, I feel so lonely and bad\" – you say")
            print()
            input("You need to enter a password to your bedroom") 
            input("The absence of sugar in your blood for a long time forced you to forget it. \n\
And it has changed because of too many failed attempts")
            # Running the opening door mini-game
            rand_num_game()  
            input("You are sleeping, and in your dream there is something strange. You feel everything")
            break
        # The script if you have chosen 2
        elif your_action_1 == "2":
            # The inputs that continue the script
            input("It’s cold outside. But you need some sugar in your veins") 
            input("You need at least a bar of chocolate")
            print()
            input("Choose an action:")
            print()
            input("1. Get a jacket to not be frozen alive")
            input("2. Go without it (you will probably catch cold)")
            print()
            # One more choice of actions
            your_action_2 = input("Enter your action: \n>>> ")
            # The infinite loop breaks if you entered the right action
            while True :
                if your_action_2 == "1":
                    input("You have a jacket now. You feel much warmer")
                    print()
                    break
                elif your_action_2 == "2":
                    input("You fell the pain of cold weather. You have 90/100 health left")
                    print()
                    # You lose health if you have chosen 2-nd action
                    health -= 10
                    break
                else:
                    # The loop isn't broken if you didn't enter the right choice
                    your_action_2 = input("Please, enter your choise again: \n>>> ")
            input("You are in a shop. You see a bar of chocolate and a vanilla donut")
            print()
            input("What will you choose?")
            print()
            input("1. Buy a bar of chocolate")
            input("2. Buy a donut")
            print()
            your_action_3 = input("Enter the number of an action: \n>>> ")
            # You get additional points if you get to this point in game
            while True:
                # You get different amount of points that depends on your choice
                if your_action_3 == "1":
                    points += 15
                    input("The chocolate was too sticky without a hot drink")
                    input("It made you thirsty and your mouth sticky")
                    break
                elif your_action_3 == "2": 
                    points += 50
                    input("You enjoyed the donut so much. It was perfect")
                    break
                else:
                    your_action_3 = input("Please, enter your choise again: \n>>> ")
            input("You came home")
            input("You need to enter a password to your room") 
            input("The absence of sugar in your blood forced you to forget it. And now it is changed")
            # Starting the guessing password game
            rand_num_game()  
            input("You have fallen asleep...")
            break
        else:
            your_action_1 = input("Please, enter your choise again: \n>>> ")
    # In the end of the act you get points and the function returns you stats
    points += 100
    return health, points

def second_act(max_health, health, damage, points, coke, nickname):
    '''
    The second act

    A lot of inputs present the plot of the game to the player
    Also, along the way the choices are given to the player
    All of them lead to one outcome but with different concequences to the player

    The choices that the player make are in while loops and they break only when the choice that exists is chosen
    '''
    # The variable your_action_3 is announced beforehand because it is used in the if-else function below
    # even if the player didn't get to choose it
    your_action_3 = "0"
    # Using .format to get the nickname of the player
    input("{}, you find yourself in a strange place".format(nickname))
    input("On one hand you realise it’s a dream, but on the other hand, it’s too real not to be true")
    print()
    input("You walk forward, look around. The trees are full of fruit. “Oh, fruits, hate them so much” — you think")
    input("The grass is very green and the sky is clear")
    print()
    input("But then you see a man or...")
    print()
    input("A waffle going by. A very sweet chocolate one. He looks destroyed, like half-eaten. It walks right into you")
    print()
    input("Your actions: ")
    print()
    input("1. \"Who are u?\"")
    input("2. \"Where the hell am I?\"") 
    input("3. Beat him to death and eat") 
    input("4. Go away")
    print()
    # The four choices that leads to one final boss but in different ways. You also get points along the way
    your_action_1 = input("Choose your action: \n>>> ")
    # The infinite loop breaks if you enter the right action
    while True:
        if your_action_1 == "1":
            input("\"I’m the survivor. Healthy food has conquered all the island of yummy food")
            input("We lived happily for a long time. It was a heaven you every being in this world. Now look at me")
            input("I’m almost done. Almost dead. There are only a few of us, like you and me\"")
            print()
            input("Your actions: ")
            print()
            input("1. Why am I like you?")
            input("2. Don’t interrupt")
            print()
            your_action_2 = input("Choose your action: \n>>> ")
            # The infinite loop breaks only if you enter the right action
            while True:
                if your_action_2 == "1":
                    input("\"You are also a survivor. The one who will save us\"")
                    input("You look at yourself and realise that you.. are.. a donut")
                    input("\"The world needs you, the Golden Warrior {}\"".format(nickname))
                    break
                elif your_action_2 == "2":
                    input("\"I have read about you. You are the one who has the power that will defeat the monsters")
                    input("The Golden Warrior {}. Let me walk you through the island\"".format(nickname))
                    break
                else:
                    your_action_2 = input("Please, enter your choise again: \n>>> ")
            # You get different amount of points that depend on your choice
            points += 25
            break
        elif your_action_1 == "2":
            input("\"The yummy food island. You are like us. You are the survivor")
            input("I have read about you. You are the one who has the power of will that will defeat the monsters")
            input("You look at yourself and you realize that you are a donut. Not a human")
            input("The Golden Donut. {}. Let me walk you through the island\"".format(nickname))
            # You get different amount of points that depend on your choice
            points += 20
                        
            break
        elif your_action_1 == "3":
            input("The waffle comes to you. You say: ")
            print()
            input("I will kill you and I will eat you. You look too yummy")
            input("\"No, you don’t know who you will be fighting against")
            input("Ok")
            input("It’s time for you to die\"")
            print()
            input("You beat him first, you start the fight")
            # You get different amount of points that depend on your choice
            points += 30
            break
        elif your_action_1 == "4":
            input("You don’t even look at him. You just go away")
            print()
            input("\"Hey, you, come here!\"")
            print()
            input("1. Turn around and ask him what is happening there")
            input("2. Ignore him")
            your_action_3 = input("Choose your action: \n>>> ")
            print()
            # The infinite loop breaks only if you enter the right action
            while True:
                if your_action_3 == "1":
                    input("You have turned around and started walking to him")
                    print()
                    input("\"Hey, what the hell is happening here?\" You said")
                    print()
                    input("\"It's the yummy food island. And you are like us. You are the survivor")
                    input("I have read about you. You are the one who has the power of will that will defeat the monsters")
                    input("You look at yourself and you realize that you are a donut. Not a human")
                    input("The Golden Donut. {}. Let me walk you through the island\"".format(nickname))
                    break
                if your_action_3 == "2":
                    input("\"Where are you going? I didn’t think you will be that rude\"")
                    input("He is sad")
                    input("He will kill you")
                    print()
                    input("He beats you first. You enter the fight")
                    break
                else:
                    your_action_3 = input("Please, choose your action again: \n>>> ")
            points += 25
            break
        else:
            your_action_1 = input("Please, enter your choise again: \n>>> ")
                      
            
    # Your different choices leads to one of the two possible scenarios. This scenarios are made with the help of if-else
    if your_action_1 == "1" or your_action_1 == "2" or your_action_3 == "1":
        print()
        input("You both walk down the road")
        input("You look around and notice that even little clouds have the form of vegetables")
        input("The waffle walks with you to the castle")
        print()
        input("\"The KING lives there. He is the one who is responsible for the illumination of our kind")
        input("You may need this\"")
        print()
        input("He gives you a coke")
        # One coke adds to the "c" variable, which is coke
        coke += 1
        input("\"It heals you. Use it when you will be in trouble\"")
        print()
        input("The coke heals 25 health")
        input("Suddenly the waffle falls on the ground, he feels sick")
        input("He starts pulsating. His body doesn't feel right")
        input("Then he looks at you")
        print()
        input("\"Finish the mission\" he said")
        input("\"Remember one thing. You can do itttttt....\"")
        print()
        input("And he died")
        print()
        input("But you were in a wrong spot and suddenly...")
        input("The ground starts to fall under you")
        input("You feel like you are levitating")
        print()
        input("You have fallen down the hill. You have lost 50 health")
        # Loosing health
        health -= 50
        input("You can use the coke. It will heal 25 health")
        print()
        input("1 Use it")
        input("2 Maybe next time")
        print()
        your_action_4 = input("\n>>> ")
        # The infinite loop breaks if you enter the right action
        while True:
            # if-else that adds 25 hp to your health if you choose to drink coke
            if your_action_4 == "1":
                input("You have drinked a coke and healed 25 health")
                coke -= 1
                health += 25
                break
            if your_action_4 == "2":
                input("You have saved your coke and you are moving on")
                break
            else:
                your_action_4 = input("Plese, enter your action again: \n>>> ")
        # You get points depending on your choice
        points += 35
    else:
        # The battle between the waffle man and the main player, the second possible scenario
        input("The battle HAS STARTED")
        print(">>><<<>>><<<>>><<<>>><<<>>><<<>>><<<")
        print(">>><<<>>><<<>>><<<>>><<<>>><<<>>><<<")
        print("....................................")
        print(">>><<<>>><<<>>><<<>>><<<>>><<<>>><<<")
        print(">>><<<>>><<<>>><<<>>><<<>>><<<>>><<<")
        # Your health and damage; waffle's health and damage before the fight
        input("Your attack deals {} damage, you have {} health. His damage is 5, health – 60".format(damage, health))
        input("Both of you hit each other")
        input("Both of you deal damage")
        input("After all, you have WON")
        # You lose health after the fight depending on whether you attacked first or not
        health -= 25
        # If you didn't attack first, which happens when your_action_1 == "4", you lose more health
        if your_action_1 == "4":
            health -= 5
            points -= 10
        print()
        # Prints your health at the moment
        print("You have lost", 100 - health, end = " ")
        input("health")
        input("And you have {}/{} health left".format(health, max_health))
        print()
        input("\"You are strong. You are him. THE ONE\"")
        input("Remember one thing. You can do ittttt....\"")
        input("And he became silent...")
        print()
        input("You have killed the waffle. You see a chest near you that has dropped after his death") 
        print()
        # After you killed the waffle you get as a bonus either damage boost or health boost
        dam_health = ["health", "damage"]
        item = random.choice(dam_health)
        if item == "health":
            # If you are lucky to get max health boost
            print("You have a new max health! Now your health is", end = " ")
            max_health += 25
            print("{}/{}".format(health, max_health), end = "")
            input()
        else:
            # The increese of damage
            print("Your damage has increased! Now it is", end = " ")
            damage += 5
            input(damage)
        # Adding points
        points += 50
        print()
    # The end of the second act and the functon returns player stats
    input("So, you have reached the entrance of the castle")
    print()
    input("You look straight in the eyes of the carrot. He has a broccoli sword...")
    input("\"Agghh. This thing. Hate it\", you say")
    print()
    input("\"Hey! It’s forbidden for sweet things to be here.\" The ugly voice appeared. \"Be ready to die!\"")
    print()
    input("You have finished the second act")
    
    return max_health, health, damage, points, coke

def the_boss (max_health, health, damage, points):
    '''
    The function that gives you the final battle with the final boss

    You have a set of three rules to fight the boss. 
    If you follow them, win the mini-games that help you to defeat the boss faster and don't die – you win the game!
    '''
    # Explaining the rules of the boss fight and wishing good luck
    print()
    input("The rules are: ")
    print('1. Before each of your attacks you should guess in under three attempts the right number \n\
that was multiplied to reflect half of the damage dealt to you.\
Else you deal half your damage')
    print()
    print("2. Before each of Carrot’s attacks you should guess the number from 0 to 150 in under 10 attempts \n\
to break his shield and deal two times more damage!")
    print()
    print("3. After two of his attacks you will have a random chance of either getting a coke or a pepsi if you answer the riddle correctly")
    input("So now...")
    print()
    input("Good luck!")
    print("===           GO           === ")
    print("===           GO           === ")
    print("===           GO           === ")
    print()

    def your_damage(is_more_damage):
        '''
        The function that generates a random number from 0 to 150
        
        And you need to guess it in 10 attempts
        After each one the system will help you:
        it will tell you either the number is bigger or smaller
        '''
        # Generating the random number which the player should guess
        number = random.randrange(0, 150)
        input("Quick, guess the right number from 0 to 150!")
        print("Enter your guess: \n", end = "")
        for i in range(10):
            # The infinite loop breaks if you entered the right action
            while True:
                # If the input isn't an integer, the system asks you to enter the number again
                try:
                    guess = int(input(">>> "))
                    pass
                except ValueError:
                    guess = input("You did not enter a number. Please try again! \n>>> ")
                    continue
                # Checking if number was correct and returning the bool True if you guessed the right number
                if guess == number:
                    input("You have dealt two times more damage!")
                    is_more_damage = True
                    return is_more_damage
                # Else, if you didn't manage to guess the right number, unfortunately, you don't deal additional damage
                else:
                    print("You have", 9 - i, "attempts left")
                    if 9 - i == 0: 
                        print()
                        print('You have used all your attempts')
                        input("Unfortunately, you didn't deal additional damage")
                        return is_more_damage
                    print ("You didn't enter the right number. The number is ", end = "")
                    print( "Smaller "if (number < guess) else "Bigger")
                    break

    def reflection (is_active_shield):
        '''
        The function that makes the user guess what number was multiplied to activate your shield!
        
        And you need to guess it in 3 attempts
        If you didn't guess it – your shield will not be activated
        '''
        # Generating two random numbers that will be multiplied
        a = random.randrange(1, 15)
        b = random.randrange(1, 15)
        c = a * b
        # Asking player to enter the numbers
        input("Guess what number was multiplied to activate your shield!")
        print("{} * ? = {}".format(a, c))
        print("Enter your guess: \n", end = "")
        # For loop gives the player three attempts to guess the number
        for i in range(3):
            # The infinite loop breaks if you entered the right action
            while True:
                # If the input isn't an integer, the system asks you to enter the number again
                try:
                    guess = int(input(">>> "))
                    pass
                except ValueError:
                    print("You did not enter a number. Please try again!")
                    continue
                # If-else that checks if you entered the right number
                if guess == b:
                    input("You have activated the shield!")
                    is_active_shield = True
                    return is_active_shield
                else:
                    print("You have", 2 - i, "attempts left")
                    print("The guess was incorrect!")
                    if 2 - i == 0: 
                        print()
                        print('You have used all your attempts')
                        input("Unfortunately, the shield wasn't activated")
                        return is_active_shield
                    break

    def health_boost(health):
        '''
        The function gives the player a random riddle
        
        If the player answers the question correctly, he gets a random heal:
        either 25 hp or 50 hp
        '''
        # Creating the list of two of the possible things you can get
        choice = ["coke", "pepsi"]
        input("Answer the riddle to get either a coke or a pepsi!")
        # Making a list of riddles and answers
        riddles = ["The Earth is flat", "The Moon is made of cheese", "2 + 2 = 5?", \
            "Humans have never landed on Mars",  "There are just a few of galaxies in our Universe", \
            "Grass is green", "Humanity is the worst civilisation", \
            "The sunlight needs 8 minutes to reach Earth", "Iron cannot be liquid"]
        answers = [False, False, False, True, False, True, True, True, False]
        # Creating a random i that takes a riddle from the list and prints it
        i = random.randrange(0, 8)
        input("Enter \"True\" if you think that the answer is True and \"False\" if you think that the answer is False")
        print("\n", riddles[i], "\n", sep = "")
        guess = input("Enter your guess: \n>>> ")
        # The infinite loop breaks if you entered the right action
        while True:
            # if-else function that checks if you entered True or False. Else - asks you to enter your guess again
            if guess == "True" or guess == "False":
                pass
            else:
                guess = input("Enter your guess again please: \n>>> ")
                continue
            # if-else that checks if your answer was correct
            if guess == str(answers[i]):
                input("The guess was right!")
                print()
                drink = random.choice(choice)
                # if-else that adds you aditional health depending on whether it's coke or pepsi
                if drink == "coke":
                    input("You have got a coke. You drink it immediately and you got +25 health")
                    health += 25
                    if health > max_health:
                        health = max_health
                else:
                    input("You have got a pepsi. You drink it immediately and you got +50 health")
                    health += 50
                    if health > max_health:
                        health = max_health
                print()
                print("Now you have {}/{} health".format(health, max_health), end = "")
                input()
                return health
            else:
                # If you didn't guess right - the function returns the same health as you have had before
                print()
                input("You guessed wrong :(")
                print()
                return health
    # Health and damage of the carrot boss
    boss_health = 100
    boss_damage = 30
    # The i variable
    i = 0
    # The script that repeats until you either die or kill the boss
    while True:
        # Booleans that are for checking if you deal full damage and if you reflect some of the damage
        is_more_damage = False
        is_active_shield = False
        input("He attacks you and you need to pull off your shield")
        # The function returns the bool and depending on that you either get fewer damage or not
        is_active_shield = reflection (is_active_shield)
        if is_active_shield:
            print()
            input("You have got {} damage from the boss!".format(boss_damage / 2))
            print()
            health -= boss_damage / 2
        else:
            print()
            input("You have got {} damage from the boss!".format(boss_damage))
            print()
            health -= boss_damage
        # The script that ends the game if you have lost all your health
        if health <= 0:
            print("Unfortunately, you have DIED...")
            input("You have got too much damage from the boss")
            input("Better luck next time!")
            print()
            print("Your points:", points)
            exit()
        # Printing your health
        input("Your health: {}. His health: {}".format(health, boss_health))
        print()
        input("Now, YOU attack!")
        print()
        # The function returns the bool and depending on that you either deal a lot of damage or not
        is_more_damage = your_damage(is_more_damage)
        if is_more_damage:
            input("You have dealt {} damage to the boss!".format(damage * 2))
            boss_health -= damage * 2
        else:
            input("You have dealt {} damage to the boss!".format(damage))
            boss_health -= damage
        print()
        # Checks if the boss is dead or not
        if boss_health <= 0:
            input("The boss has: 0 health remaining")
            print()
            input("=== IMPOSSIBLE! YOU COULDN'T HAVE WON === ")
            print()
            input("===       YOU ARE JUST A DONUT!       === ")
            print()
            input("===         IT IS NOT THE END!        === ")
            print("===                                   === ")
            print("===                                   === ")
            print("===                                   === ")
            input("===          TO BE CONTINUED!         === ")
            input("===         Thanks for playing!       === ")
            print()
            points += 250
            # Returns all the stats
            return max_health, health, damage, points
        # Printing the health of the boss
        print("The boss has:", boss_health, end = " ")
        input("health remaining")
        print()
        # Every two times you pull up a shield and deal damage you get a chance to heal yourself
        # This if and variable check if it's time for you to heal
        i += 1
        if i % 2 == 0:
            input("Now, you can get a health boost!")
            print()
            health = health_boost(health)

def results(points, max_player_health, player_health, player_damage):
    '''
    The function that prints your stats

    >>> results(points, max_player_health, player_health, player_damage)

    Your points: points
    Your health: {player_health}/{max_player_health}
    Your damage: player_damage

    '''
    print()
    print("Your points:", points)
    print("Your health: {}/{}".format(player_health, max_player_health))
    print("Your damage:", player_damage)
    print()

def main():
    '''
    The main() function calls all the other functions in a correct order
    and makes the game work
    '''
    # Giving a player stats that are going to change during the game
    points = 0
    max_player_health = 100
    player_health = 100
    player_damage = 10
    coke = 0 # coke heals 25 hp
    # Getting nickname of the user from the function
    nickname = start_game()
    # The function calls the function first_act. It returns your health and points
    player_health, points = first_act(player_health, points, nickname)
    # Printing player's stats for the first act
    input("The result of the first act is: ")
    results(points, max_player_health, player_health, player_damage)
    input("You are moving on")
    input("===    THE DREAM    === ")
    # The function calls the function second_act. It returns your max health, damage, health, points and coke
    max_player_health, player_health, player_damage, points, coke = second_act(max_player_health, player_health, player_damage, points, coke, nickname)
    # Printing player's stats for the second act
    input("The result of the second act is: ")
    results(points, max_player_health, player_health, player_damage)
    print()
    input("===      BEHOLD     === ")
    input("=== THE CARROT BOSS === ")
    input("===     IS HERE     === ")
    # The function calls the function the_boss. It returns your max health, damage, health and points
    max_player_health, player_health, player_damage, points = the_boss(max_player_health, player_health, player_damage, points)
    # The algorithm makes out of all player statistics points and prints the result of the game
    points += max_player_health / 5
    points += player_health
    points += player_damage
    if coke == 1:
        input('You have saved your coke! You got additional points')
        points += 200
    print("Your result is:", int(points), end = " ")
    input("points")

# Running the game with function main
if __name__ == "__main__":
    main()
