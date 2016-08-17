#Sample place-in exam, part 1

#Imports
import random

#Body
def play_game():
    print("Let's play the game of Seventeen!")
    marbles_left = 17
    while marbles_left > 0:
        print("Number of marbles left in jar: {} \n ".format(marbles_left))
        user_input = input("Your turn: How many marbles will you remove (1-3)? ")
        if user_input != '1' and user_input != '2' and user_input != '3':
            print("Sorry, that is not a valid option. Try again!")
            continue
        if int(user_input) > marbles_left:
            print("Sorry, that is not a valid option. Try again!")
            continue
        print("You removed {} marbles.".format(user_input))
        marbles_left -= int(user_input)
        if marbles_left == 0:
            print("There are no marbles left. Computer wins!")
            return
        print("Number of marbles left in jar: {} \n ".format(marbles_left))
        print("Computer's turn...")
        computer_input = random.randint(1, 3)
        while computer_input > marbles_left:
            computer_input = random.randint(1, 3)
        print("Computer removed {} marbles.".format(computer_input))
        marbles_left -= computer_input
        if marbles_left == 0:
            print("\nThere are no marbles left. User wins!")
            return



#########################################################################
def main():

    play_game()

if __name__ == '__main__':
    main()