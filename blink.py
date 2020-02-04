# Name: Tsui, Hang Yiu Henry
# Student ID: 20105575

word_dict = []
with open('words1.txt') as f:
    words = f.read().splitlines()

for w in words:
    w = w.lower()
    word_dict.append(w)

def restart_game():
    print('')
    userchoice = str(input("Enter y if you would like to play another game\nEnter n if you would like to exit\nEnter here:"))
    print('')
    if userchoice == 'y' or userchoice == 'Y':
        print("Reloading game...")
        print('')
        Interface()
    if userchoice == 'n' or userchoice == 'N':
        print("Exiting game...")
        exit()
    else:
        print("Invalid input")
        restart_game()

def word(word_fragment, player, userInput):

    word_fragment += userInput

    if len(word_fragment) > 3 and word_fragment in word_dict:
        print("Word formed: ",word_fragment)
        print("Player",player,"lost!")
        restart_game()

    valid_fragment = False
    for valid_word in word_dict:
        if valid_word.startswith(word_fragment):
            valid_fragment = True
            break
    if not valid_fragment:
        print("Current character(s): ", word_fragment)
        print("Player",player,"lost!")
        restart_game()

    return word_fragment


def challenge(wordfrag, player, numPlayers): #challenges a player
    challengePlayer = True

    if wordfrag == '':
        print("Word fragment is empty, please enter a letter first")
        print('')
        if numPlayers == 2:
            twoPlayerGame()
        if numPlayers == 3:
            threePlayerGame()
    elif wordfrag != '':
        while challengePlayer:
            if numPlayers == 3:
                if player == 1:
                    print("Player 1 has challenged Player 3!")
                    userinput = 3
                    challengePlayer = False
                if player == 2:
                    print("Player 2 has challenged Player 1!")
                    userinput = 1
                    challengePlayer = False
                if player == 3:
                    print("Player 3 has challenged Player 2!")
                    userinput = 2

            if numPlayers == 2:
                if player == 1:
                    print("Player 1 has challenged Player 2!")
                    userinput = 2
                    challengePlayer = False
                if player == 2:
                    print("Player 2 has challenged Player 1!")
                    userinput = 1
                    challengePlayer = False
        print('')
        print("Current word fragment is:",wordfrag)
        print("Player",userinput,"has to guess the word fragment: ")
        userguess = str(input())

        beginstring = userguess[:len(wordfrag)] #comparing to see if the first few characters of userguess and wordfrag match
        
        if beginstring != wordfrag:
            print("Player",userinput,"has guessed the word incorrectly")
            print("Player",userinput,"has lost!")
            restart_game()
        if userguess in word_dict:
            print("Player",userinput,"has guessed the word correctly!")
            restart_game()

        if not userguess in word_dict:
            print("Player",userinput,"has guessed the word incorrectly")
            print("Player",userinput,"has lost!")
            restart_game()



def twoPlayerGame(): #two player game mode
    wordfrag = ''
    userInput = ''
    player = 0
    count = 1
    numPlayers = 2
    while True:
        if count == 1:
            player = 1
            print("It is Player 1's turn")
        if count == 2:
            player = 2
            print("It is Player 2's turn")

        count += 1
        if count == 3:
            count = 1

        print('')
        while player != 0:
            print("Please enter a letter or type 'challenge': ")
            userInput = str(input())
            userInput = userInput.lower()

            if userInput == 'challenge':
                break
            if len(userInput) > 1:
                continue
            if userInput.isalpha():
                break
        

        if userInput == 'challenge':
            challenge(wordfrag, player, numPlayers)
        else:
            wordfrag = word(wordfrag, player, userInput)
            print("Current character(s): ", wordfrag)

def threePlayerGame(): #three player game mode
    wordfrag = ''
    userInput = ''
    player = 0
    count = 1
    numPlayers = 3
    while True:
        if count == 1:
            player = 1
            print("It is Player 1's turn")
        if count == 2:
            player = 2
            print("It is Player 2's turn")
        if count == 3:
            player = 3
            print("It is Player 3's turn")

        count += 1
        if count == 4:
            count = 1

        print('')
        while player != 0:
            print("Please enter a letter or 'challenge': ")
            userInput = str(input())
            userInput = userInput.lower()

            if len(userInput) > 1 and userInput == "Challenge":
                break
            elif userInput.isalpha():
                break
            elif len(userInput) > 1:
                continue

        if userInput == "challenge":
            challenge(wordfrag, player, numPlayers)

        else:
            wordfrag = word(wordfrag, player, userInput)
            print("Current character(s): ", wordfrag)
            print('')


def Interface():
    while True:
        try:
            numplayers = int(input("Do you want 2 or 3 players?: "))
            if numplayers == 2:
                break
                
            if numplayers == 3:
                break

            if numplayers != 2 or numplayers != 3:
                print("Please enter a number between 2 or 3")
                
        except:
            print("Please enter a number between 2 or 3")
    if numplayers == 2:
        twoPlayerGame()
    if numplayers == 3:
        threePlayerGame()
            

def main():
    Interface()

main()