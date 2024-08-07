wordle_guess = ["", "", "c", "a", ""]
possible_letters = ["q", "w", "y", "u", "i",
                    "a", "d", "f", "g", "j", "k", "z", "x", "c" "b", "n", "m"]
# ambiguous_letter = "r"
possible_combinations = []


def swap(index_1, index_2):
    tempword = wordle_guess[index_1]
    wordle_guess[index_1] = wordle_guess[index_2]
    wordle_guess[index_2] = tempword


first = 0
last = 13


def crack_wordle():
    for letter in possible_letters:
        wordle_guess[0] = letter
        for character in possible_letters:
            # if character != letter:
            wordle_guess[1] = character
            for symbol in possible_letters:
                # if symbol != character and letter:
                wordle_guess[4] = symbol
                word = wordle_guess[0] + wordle_guess[1] + wordle_guess[2] + wordle_guess[3] + wordle_guess[4]
                print(word)
                possible_combinations.append(wordle_guess)
                with open ('wordle guesses.txt','a') as file_object:
                    file_object.write(word + '\n')

    print("you have found " + str(len(possible_combinations)) +
          " of 4080 possible combinations")


crack_wordle()
