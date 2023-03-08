print("Welcome to the game, Paper-Scissors-Rock")

computer = "PSRRSPRPSRPSPRPSPRPS" # creating a string only with letters for the computer's choice.

while True:  # start of the loop.
    for computer_choice in computer:

        user_choice = input(
            "Please pick 'P'[Paper], 'S'[Scissors], 'R'[Rock] or the «ENTER» key to exit the game!\nUser picked: "
        ).upper().strip()  # user choice.
        if user_choice == "":
            # if user types no-string, the game will end.
            print("END OF THE GAME!")
            quit()
        elif user_choice != "P" and user_choice != "S" and user_choice != "R":
            print("Please only pick between 'P'-'S'-'R'")  # user must type only these three letters.
            continue

        elif user_choice == "P" and computer_choice == "P" or user_choice == "S" and \
                computer_choice == "S" or user_choice == "R" and computer_choice == "R":
            print("Computer picked: " + computer_choice)
            print("Draw!")

        elif user_choice == "R" and computer_choice == "S":
            print("Computer picked: " + computer_choice)
            print("You win!")

        elif user_choice == "S" and computer_choice == "P":
            print("Computer picked: " + computer_choice)
            print("You win")

        elif user_choice == "P" and computer_choice == "R":
            print("Computer picked: " + computer_choice)
            print("You win!")

        else:
            print("Computer picked: " + computer_choice)
            print("Computer wins!")

    print("End of round!")
    play = input("Press any key to play again or the «ENTER» key to exit the game: ").strip()
    if play == "":
        print("END OF THE GAME!")
        quit()
    else:
        # game starts over.
        continue
