from time import sleep
from random import choice
import arrays

print("Welcome to the magic ball!")
name_player = input("What's your name? ")
print("Hello, ", name_player, "\nSo, what is your 'yes or no' question, my dear friend")
question = input()

print("Hmmm, let me think")
sleep(2)
print(f'{choice(arrays.introductory_words).capitalize()},'
      f' {choice(arrays.expressive_words)}. {choice(arrays.contrasting_sentences)}')
sleep(2)
