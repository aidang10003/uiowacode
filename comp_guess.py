import random

def comp_guess(result, last_guess, wrong_letters, lastc_guess, keep_letters):
    guess = []
    for x in range(len(last_guess)):    #makes list for guess letters
        guess.append(' ')
    for a in range(len(result)):        #matches correct letters
        if result[a] == 'x':
                guess[a] = last_guess[a]
    counter = 0
    for letter in last_guess:           #seperates other letters into keep or wrong
        if result[counter] == 'x':
            counter += 1
            continue
        if result[counter] == 'o':
            keep_letters[counter] = letter
        else:
            wrong_letters.extend(letter)
        counter += 1
    counter = 0
    for letter in lastc_guess:          #seperates last guess of comupter letter
        if result[counter] == 'x':
            counter += 1
            continue
        if result[counter] == 'o':
            keep_letters[counter] = letter
        else:
            wrong_letters.extend(letter)
        counter += 1
    for letter in keep_letters:         #chooses random spot for letter
        spot = random.randint(0 , len(last_guess)-1)
        while spot == letter or guess[spot] != ' ':
            spot = random.randint(0, len(last_guess)-1)
            if spot != letter and guess[spot] == ' ':
                break
        guess[spot] = keep_letters[letter]
    letter_list = 'abcdefghijklmnopqrstuvwxyz'
    for letter in guess:                #adds letter to guess if not already there or wrong
        if letter == ' ':
            a = random.randint(0, len(letter_list)-1)
            x = letter_list[a]
            while x in wrong_letters:
                a = random.randint(0, len(letter_list)-1)
                x = letter_list[a]
                if x not in wrong_letters:
                    break
            blank = guess.index(' ')
            guess[blank] = x
    output = ''
    for letter in guess:                        #calculate guess, output str
        output += letter
    print(f'The computer guesses: {output}')
    return output, wrong_letters
