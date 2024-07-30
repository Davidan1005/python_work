wordle_guess = ["", "e", "", "a", ""]
possible_letters = ["q", "w", "u", "o", "f",
                    "h", "j", "l", "z", "x", "c", "v", "m"]
ambiguous_letter = "r"
possible_combinations = []


def swap(index_1, index_2):
    tempword = wordle_guess[index_1]
    wordle_guess[index_1] = wordle_guess[index_2]
    wordle_guess[index_2] = tempword


first = 0
last = 13


def crack_wordle():
    for i in range(first, last):
        for j in range(first + 1, last):
            wordle_guess[0] = possible_letters[i]
            wordle_guess[2] = possible_letters[j]
            wordle_guess[4] = ambiguous_letter
            print(wordle_guess[0] + wordle_guess[1] +
                  wordle_guess[2] + wordle_guess[3] + wordle_guess[4])
            possible_combinations.append(wordle_guess)

            swap(2, 4)
            print(wordle_guess[0] + wordle_guess[1] +
                  wordle_guess[2] + wordle_guess[3] + wordle_guess[4])
            possible_combinations.append(wordle_guess)

        # for k in range(0,first):

    print("you have found " + str(len(possible_combinations)) +
          " of 312 possible combinations")


crack_wordle()
