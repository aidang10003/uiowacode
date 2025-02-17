"""
Created on Sun May  3 10:10:17 2020

@author: dilan
"""


import random


def choose_difficulty():
    difficulty = input('Choose "easy", "normal", or "hard" difficulty: ')
    if difficulty == 'easy':
        return 'three'
    elif difficulty == 'normal':
        return 'four'
    elif difficulty == 'hard':
        return 'five'
    else:
        input("please choose a valid difficulty (easy, normal, hard): ")


def generate(word_list):
    file = open(word_list , 'r')
    text = file.read()
    file.close()
    list = text.split('\n') #change from ',' because text is split by line
    x = random.randint(0,len(list))
    word = list[x]
    word = word.strip()
    return word

def comp_guess(result, last_guess):
    guess = []
    for x in range(len(last_guess)):
        guess.append(' ')
    for a in range(len(result)):
        if result[a] == 'x':
                guess[a] = last_guess[a]
    keep_letters = {}
    wrong_letters = []
    counter = 0
    for letter in last_guess:
        if result[counter] == 'x':
            counter += 1
            continue
        if result[counter] == 'o':
            keep_letters[counter] = letter
        else:
            wrong_letters.append(letter)
        counter += 1
    for letter in keep_letters:
        spot = random.randint(0 , len(last_guess)-1)
        while spot == letter or guess[spot] != ' ':
            spot = random.randint(0, len(last_guess)-1)
            if spot != letter and guess[spot] == ' ':
                break
        guess[spot] = keep_letters[letter]
    letter_list = 'abcdefghijklmnopqrstuvwxyz'
    for letter in guess:
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
    for letter in guess:
        output += letter
    print(f'The computer guesses: {output}')
    return output

def word_game(word):
    true_word = word
    while True:
        guess = input('Enter a guess: ')
        guess = guess.lower()
        while len(guess) != len(true_word):      #check if guess length matches answer length
            guess = input('Please enter a correct word legnth: ')
            if len(guess) == len(true_word):
                break
        word = true_word
        if guess == word:
            print(f'Congratulations! {guess} is the correct answer!')
            break
        output = []     #output list to track results
        for x in word:
            output.extend(' ')  #initiliaze list length to match word
        counter = 0
        for letter in guess:
            if word[counter] == letter:     #check if letter in guess matches answer, appends 'x' to list if true
                output[counter] = 'x'
            counter += 1
        counter = 0
        for x in range(len(output)):        #slices answer to include only letters not guessed completely correctly
            if output[x] == 'x':
                word = word[:counter] + word[counter + 1:]
            else:
                counter += 1
        counter = 0
        for letter in guess:
            if output[counter] == 'x':      #checks if letter is already correct before continuing
                counter += 1
                continue
            if letter in word:              #if letter in string of answer, appends 'o' in correct index
                output[counter] = 'o'
                word = word.replace(letter,'',1)
            counter += 1
        print(f'Results: {output} \n')         #prints result of guess
        check = comp_guess(output, guess)     #runs computer guess
        c_guess = check
        if c_guess == true_word:
            print(f'Sorry! The computer beat you! The correct word was {true_word}.')
            break
        word = true_word
        output = []     #output list to track results
        for x in word:
            output.extend(' ')  #initiliaze list length to match word
        counter = 0
        for letter in check:
            if word[counter] == letter:     #check if letter in guess matches answer, appends 'x' to list if true
                output[counter] = 'x'
            counter += 1
        counter = 0
        for x in range(len(output)):        #slices answer to include only letters not guessed completely correctly
            if output[x] == 'x':
                word = word[:counter] + word[counter + 1:]
            else:
                counter += 1
        counter = 0
        for letter in check:
            if output[counter] == 'x':      #checks if letter is already correct before continuing
                counter += 1
                continue
            if letter in word:              #if letter in string of answer, appends 'o' in correct index
                output[counter] = 'o'
                word = word.replace(letter,'',1)
            counter += 1
        print(f'Results: {output} \n')         #prints result of guess
    return output
        
a = generate(f'{choose_difficulty()}_letter.csv') #changes based on difficulty
b = word_game(a)

