import random
import json
import copy
def flashcards(): 
  count = 0
  with open("flashcards.json", "r") as f:
    d = json.load(f)

  keysList = list(d.keys())
  random.shuffle(keysList)
  for keyy in keysList:
    question = input(f"name a {keyy}, type something when you got an answer ")
    if question == question:
      yn = input(f"is your answer {d[keyy]}? answer y/n ")
      yn = yn.lower()
      if yn == "y":
        count += 1
        with open("counter.json", "r") as f:
          new_counter = json.load(f)
        new_counter[keyy] = count
        with open()
 
          
        
flashcards()   