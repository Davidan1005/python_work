wordle_guess = ["","e","","a",""]
possible_letters = ["q","w","u","o","f","h","j","l","z","x","c","v","m"]
ambiguous_letter = "r"
possible_combinations = []

def swap(index_1, index_2):
    tempword = wordle_guess[index_1]
    wordle_guess[index_1] = wordle_guess[index_2]
    wordle_guess[index_2] = tempword

def crack_wordle():
    for i in range(0,13):
        wordle_guess[4] = ambiguous_letter
        wordle_guess[0] = possible_letters[i]
        if i < 12:
            wordle_guess[2] = possible_letters[i+1]
        print(wordle_guess)
        possible_combinations.append(wordle_guess)
        swap(2,4)
        print(wordle_guess)
        possible_combinations.append(wordle_guess)
    print("you have found " + str(len(possible_combinations)) + " of 312 possible combinations")


crack_wordle()


