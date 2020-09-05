import random


def start_game():
    play = "y"

    best_score = 0

    print('*' * 8, 'Welcome to the number guessing game!', '*' * 8)

    while play == "y":
        solution = random.randint(1, 10)

        current_score = 1

        try:
            answer = int(input("-Please enter a number between 1 and 10: "))
            if answer < 1 or answer > 10:
                raise ValueError("Number must be between 1 and 10.")
        
        except ValueError as err:
            print("That is not a valid entry. Please enter a number between 1 and 10.")
            print("({})".format(err))

        else:
            while answer != solution:

                current_score += 1

                if answer < solution:
                    try:
                        answer = int(input("It's higher, enter a new number: "))
                        if answer < 1 or answer > 10:
                            raise ValueError("Number must be between 1 and 10.")

                    except ValueError as err:
                        print("That is not a valid entry. Please enter a number between 1 and 10.")

                        print("({})".format(err))
                        
                        current_score -= 1

                elif answer > solution:
                    try:
                        answer = int(input("It's lower, enter a new number: "))

                        if answer < 1 or answer > 10:
                            raise ValueError("Number must be between 1 and 10.")

                    except ValueError as err:
                        print("That is not a valid entry. Please enter a number between 1 and 10.")
                        
                        print("({})".format(err))
                        
                        current_score -= 1

            print("You got it! {} is the correct number!".format(solution))

            if current_score == 1:
                print("It took you {} attempt.".format(current_score))

            else:
                print("It took you {} attempts.".format(current_score))

            if not best_score or current_score < best_score:
                best_score = current_score

            if best_score == 1:
                print("BEST SCORE IS {} ATTEMPT".format(best_score))

            else:
                print("BEST SCORE IS {} ATTEMPTS".format(best_score))

            play = (input("Would you like to play again? [Y]es / [N]o ")).lower()

    print("Thank you for playing!")

start_game()
