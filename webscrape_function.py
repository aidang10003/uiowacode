"""
Last updated 7/7/2024

This function scrape Merriam Webster's online thesauras and enters the results in an Excel sheet.
Run this function first.

@author: Aidan
"""

from bs4 import BeautifulSoup
import requests 
import time

full = {'a':39, 'b':46, 'c':76, 'd':51, 'e':30, 'f':34, 'g':28, 'h':30, 'i':32, 'j':7, 'k':8, 'l':24, 'm':36, 
        'n':16, 'o':18, 'p':55, 'q':4, 'r':46, 's':87, 't':36, 'u':22, 'v':10, 'w':21, 'x':1, 'y':3 ,'z':2 }
quick = {'a':2, 'b':2, 'c':2, 'd':2, 'e':2, 'f':2, 'g':2, 'h':2, 'i':2, 'j':2, 'k':2, 'l':2, 'm':2, 
        'n':2, 'o':2, 'p':2, 'q':2, 'r':2, 's':2, 't':2, 'u':2, 'v':2, 'w':2, 'x':1, 'y':2 ,'z':2 } # can be inserted into main function for quick download
test = {'a':2, 'b':2}

    
def GetInfo(dict):
    valueList = []

    for index in dict:
        n = 0

        while n < dict[index]:
            n += 1  # Represents the number of pages a letter has
            try:
                page = requests.get(f'https://www.merriam-webster.com/browse/thesaurus/{index}/{n}')
                html_doc = page.text
                soup = BeautifulSoup(html_doc, 'html.parser')

                words = soup.findAll(class_='pb-4 pr-4 d-block') # Value will change if the site changes
                for word in words:
                    if len(word.text) >= 3 and len(word.text) <= 5: # If the word is between 3 and 5 characters add it to the list
                        valueList.append(word.text)
            except ConnectionError:
                (f"The {index} web page did not return at n value {n}")
            
            time.sleep(.1) # Sleep to avoid being locked out of the page
            
    return valueList

def CleanWordList(wordList):
    for a in range(len(wordList)): # Make all words lower case
        wordList[a] = wordList[a].lower()

    print(wordList)
    for word in wordList:
        if '\'' in word or '-' in word or 'é' in word or 'ñ' in word or ' ' in word or '(' in word or "'" in word: # Remove words with special characters
            #print("remove word >> ", c)
            wordList.remove(word)
    return wordList

def CreateSpreadsheet(cleanedWordList):
    sheets = ['three', 'four', 'five']
    for sheet in sheets:
        file = open(f'{sheet}_letter.csv', 'w')
        for word in cleanedWordList:
            if sheet == 'three' and len(word) == 3:
                file.write(word,) #writes words in the file
                file.write('\n') #format in file is that all word are in the "A" column
            elif sheet == 'four' and len(word) == 4:
                file.write(word,) #writes words in the file
                file.write('\n') #format in file is that all word are in the "A" column
            elif sheet == 'five' and len(word) == 5:
                file.write(word,) #writes words in the file
                file.write('\n') #format in file is that all word are in the "A" column
        file.close
    print("View the Excel sheets") 
    return


rawWordList = GetInfo(full) # Insert 'page' for full download and 'quick' for quick download
cleanedWordList = CleanWordList(rawWordList) # Clean the list
CreateSpreadsheet(cleanedWordList) # Add words to respective Excel sheets


