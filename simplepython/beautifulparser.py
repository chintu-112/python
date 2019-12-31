#!/usr/bin/env python3

import requests
import re
import random
from bs4 import BeautifulSoup

urls = ["http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.01",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.02",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.03",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.04",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.05",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.06",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.07",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.08",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.09",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.10",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.11",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.12",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.13",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.14",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.15",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.16",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.17",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.18",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.19",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.20",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.21",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.22",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.23",
        "http://www.manythings.org/vocabulary/lists/l/words.php?f=3esl.24"
        ]

def prepareWordList(urlList, wordsList):
  for url in urlList:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    for i in soup.find_all('li'):
      word = str(i.get_text())
      wordsList.append(word)
  return wordsList

def specialCharFilter(spell):
  regex = re.compile('[-.\'@_!#$%^&*()<>?/\|}{~: ]')
  if(regex.search(spell) == None):
    return False
  else:
    return True

def filterWords(words):
  filteredList = []
  for word in words:
    if specialCharFilter(word):
      #print("Unsuitable : " + word)
      pass
    else:
      if len(word) < 3:
        #print("Unsuitable : " + word)
        pass
      else:
        #print("Suitable : " + word)
        filteredList.append(word)
  return filteredList

def segregateWords(words):
  threeLetters = []
  fourLetters = []
  fiveLetters = []
  sixLetters = []
  sevenLetters = []
  eightLetters = []
  nineLetters = []
  tenLetters = []
  complexLetters = []

  for word in words:
    if len(word) < 4:
      threeLetters.append(word)
    elif len(word) < 5:
      fourLetters.append(word)
    elif len(word) < 6:
      fiveLetters.append(word)
    elif len(word) < 7:
      sixLetters.append(word)
    elif len(word) < 8:
      sevenLetters.append(word)
    elif len(word) < 9:
      eightLetters.append(word)
    elif len(word) < 10:
      nineLetters.append(word)
    elif len(word) < 11:
      tenLetters.append(word)
    else:
      complexLetters.append(word)
  masterList = {"3" : threeLetters, "4" : fourLetters, "5" : fiveLetters, "6" : sixLetters, "7" : sevenLetters, "8" : eightLetters, "9" : nineLetters, "10" : tenLetters, "11" : complexLetters}
  return masterList

def missingLettersPuzzle(master, level):
  randomWords = []
  for i in range(5):
    rand = random.choice(master[level])
    if rand in randomWords:
      pass
    else:
      randomWords.append(rand)
  print(randomWords)

  for eachWord in randomWords:
    orgWord = list(eachWord)
    tempWord = list(eachWord)
    levelNum = int(level)
    l = list(range(1, levelNum))
    random.shuffle(l)

    #rand1 = l.pop()
    #rand2 = l.pop()
    #tempWord[rand1] = " "
    #tempWord[rand2] = " "

    for i in range(int((levelNum / 2) + 0.5)):
      tempWord[l.pop()] = " "

    print(str(orgWord) + " : " + str(tempWord))
    while True:
      charInput = input("Enter the Character : ")
      index = input("Enter the index to fill : ")
      tempWord[int(index)] = charInput
      print(str(orgWord) + " : " + str(tempWord))
      if str(tempWord) == str(orgWord):
        break

def ruffleshufflePuzzle(master, level):
  randomWords = []
  for i in range(5):
    rand = random.choice(master[level])
    if rand in randomWords:
      pass
    else:
      randomWords.append(rand)
  print(randomWords)

  for eachWord in randomWords:
    orgWord = eachWord
    l = list(eachWord)
    random.shuffle(l)
    shuffleWord = ''.join(l)
    print(orgWord + " : " + shuffleWord)

    while True:
      tempWord = []
      for index in range(int(level)):
        charInput = input("Enter the Character : ")
        #tempWord[index] = charInput
        tempWord.append(charInput)

        print(orgWord + " : " + str(tempWord))
      finalTempWord = ''.join(tempWord)
      if finalTempWord == orgWord:
        break


### Main Section

words = []
finalWords = prepareWordList(urls, words)
filteredWords = filterWords(finalWords)
finalList = segregateWords(filteredWords)

#print(finalList['hard'])

levels = (1,2,3,4,5,6,7,8,9)

print("Games to Play")
print("Missing Letter Words : 1")
print("Shuffle Ruffle : 2")
gameNumber = input("Enter the Game you want to Play : ")

if gameNumber == "1":
  for eachLevel in levels:
    print("Starting with Level : " + str(eachLevel))
    missingLettersPuzzle(finalList, str((eachLevel + 2)))
  print("End of Game")
elif gameNumber == "2":
  for eachLevel in levels:
    print("Starting with Level : " + str(eachLevel))
    ruffleshufflePuzzle(finalList, str((eachLevel + 2)))
  print("End of Game")
else:
  print("Need to add more games")
