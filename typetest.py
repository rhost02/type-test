import random
import time
import os

length = int(input('Number of words: '))

with open('words_alpha.txt') as f:
    words = f.readlines()
    word_repo = [word.rstrip() for word in words]

chosen_words = random.choices(word_repo, k=length)
total = len(chosen_words)
words_left = total

start = time.time()
while words_left > 0:
    os.system('clear')
    current = chosen_words[0]
    print('{} words remaining\n\n{}'.format(words_left, current))
    entry = input('\n\n>>')
    if entry == current:
        del chosen_words[0]
        words_left -= 1
duration = time.time() - start

os.system('clear')
print('{} words in {:.2f}s\n{:.2f}wpm'.format(
    total, duration, total/(duration/60)))
