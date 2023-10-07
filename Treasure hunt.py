def main_game():
    print("Welcome to my Treasure Hunt")
    print("In this game, you will type where to go in certain directions")
    print("Good Luck, Have Fun :)")
    set_game = True

    while set_game:
        choice = input("Choose to go straight, right, or left ").lower()
        if choice == "straight":
            print("You died")
            set_game = False
        elif choice == "right":
            second_choice = input("You found another tunnel, go left or right? ").lower()
            if second_choice == "left":
                print("You fell into a dark deep hole that led you to your death, not the treasure")
                set_game = False
            else:
                print("You found nothing, but then you get killed by a random thief")
                set_game = False
        elif choice == "left":
            print("You arrived at the Treasure! You are now rich!")
            set_game = False
        else:
            print("Please choose a valid direction.")

if __name__ == "__main__":
    end_game = True
    while end_game:
        main_game()
        play_again = input("Would you like to play again? ").lower()
        if play_again != "yes":
            end_game = False







