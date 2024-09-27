#from IPython.display import clear_output
def clear_console():
    import os
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

def game_start():
    clear_console()
    print("Welcome to Tic Tac Toe!")
    result = False
    player = '-1'
    player1 = ""
    mylist = [0, " ", " ", " ", " ", " ", " ", " ", " ", " "]
    while player1 == "":
        player1 = input("\nPlayer 1: Do you want to be X or O?\nEnter 'No' to stop the Game:\n")
        if player1 in ['X', 'x', 'O', 'o']:
            player1 = player1.upper()
            clear_console()
            result, player = board(mylist, player1)
            if result:
                print(f"'{player}' player has won the Game!!\n")
                player = '-2'

            elif player == 'over':
                clear_console()
                print("Thanks for playing the game!!")

            else:
                print("Game Over - No-one won the game!!")
                player = '-3'

        elif player1.lower() == 'no':
            break
        else:
            clear_console()
            print("Invalid input!!")
            player1 = ""

    if player in ['-2', '-3']:
        player1 = input(
            "\nDo you want to play another game?\nEnter 'No' to stop the Game, press any key to conitnue:\n")
        if player1.lower() == 'no':
            pass
        else:
            game_start()


def board(mylist, myinput):
    position = 1
    game_over = False

    while position in [1, 2, 3, 4, 5, 6, 7, 8, 9]:

        print(mylist[1], '|', mylist[2], '|', mylist[3])
        print("---------")
        print(mylist[4], '|', mylist[5], '|', mylist[6])
        print("---------")
        print(mylist[7], '|', mylist[8], '|', mylist[9])

        position = input(
            f"Player '{myinput}' choose your next position: (1-9) \nChoose 10 - Close the game\nChoose 11 - Restart the game\n")

        if not (position.isdigit()):
            clear_console()
            print("Invalid position!\n")
            position = 1
            continue
        elif int(position) in [10, 11]:
            if int(position) == 11:
                game_start()
            elif int(position) == 10:
                status = 'over'
                result = False
                return [result, status]
        elif position.isdigit() and int(position) not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            clear_console()
            print("Invalid position!\n")
            position = 1
            continue
        else:
            position = int(position)  # Converting string to integer

            # Loop to check if the input index is already filled or not
            if mylist[position].upper() in ['X', 'O']:
                clear_console()
                print(f"{mylist[position]} cannot be overridden at position {position} with {myinput}")
                position = 1
                continue
            # updating the index value with the X/O value
            mylist[position] = myinput

            # check to find if the game is won or not by any player
            result = game_won(mylist, myinput)

            # if won, return the result
            if result:
                clear_console()
                print(mylist[1], '|', mylist[2], '|', mylist[3])
                print("---------")
                print(mylist[4], '|', mylist[5], '|', mylist[6])
                print("---------")
                print(mylist[7], '|', mylist[8], '|', mylist[9])
                return [result, myinput]
                # if not won, loop to check if the game is still on or over
            else:
                # Loop tp check if all fields/indexes are filled up to confirm if the game is over or not
                for item in range(1, len(mylist)):
                    if mylist[item] not in ['X', 'O']:
                        game_over = False
                        break
                    else:
                        game_over = True

                # game_over check
                if game_over:
                    clear_console()
                    print(mylist[1], '|', mylist[2], '|', mylist[3])
                    print("---------")
                    print(mylist[4], '|', mylist[5], '|', mylist[6])
                    print("---------")
                    print(mylist[7], '|', mylist[8], '|', mylist[9])
                    status = 'game_end'
                    return [not (game_over), status]

                # change the user input as X or O for next iteration if game not over
                if myinput == 'X':
                    myinput = 'O'
                else:
                    myinput = 'X'
                position = 1
                clear_console()


def game_won(mylist, myinput):
    result = False

    if mylist[1] == myinput and mylist[2] == myinput and mylist[3] == myinput:
        result = True
    elif mylist[4] == myinput and mylist[5] == myinput and mylist[6] == myinput:
        result = True
    elif mylist[7] == myinput and mylist[8] == myinput and mylist[9] == myinput:
        result = True
    elif mylist[1] == myinput and mylist[4] == myinput and mylist[7] == myinput:
        result = True
    elif mylist[2] == myinput and mylist[5] == myinput and mylist[8] == myinput:
        result = True
    elif mylist[3] == myinput and mylist[6] == myinput and mylist[9] == myinput:
        result = True
    elif mylist[1] == myinput and mylist[5] == myinput and mylist[9] == myinput:
        result = True
    elif mylist[3] == myinput and mylist[5] == myinput and mylist[7] == myinput:
        result = True
    else:
        result = False

    return result

def main_1():
    pass


