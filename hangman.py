import random

name = input('What is your name? ').title()
print(f'Hi...{name} Good Luck!')

words = ['abdomen', 'apple', 'orange', 'mango', 'kiwi', 'apricot', 'almond', 'banana']
secret_word = random.choice(words)
secret_word_character_list = ['-'] * len(secret_word)
the_word = ''
failed = 0
while failed < 9:
    
    print(f'You have {9 - failed} chances to guess the complete word.')
    alphabet = input('Guess a character: ').lower()
    if alphabet in secret_word:
        i = secret_word.index(alphabet)
        secret_word_character_list[i] = alphabet
        the_word = ''.join(secret_word_character_list)
    else:
        print('WRONG GUESS')
    print(the_word)

    if the_word == secret_word:
        break
    count += 1

if the_word == secret_word:
    print(f'You gussed the correct word in {count + 1} chances.')
else:
    print(f'You failed to guess the word. The word was {secret_word}')

def hangman_im(i):
    tiles = [
      '''
         _____
         |  |
         |
         |
         |
         |
         |
       __|__''',
      '''
         _____
         |  |
         |  O
         |
         |
         |
         |
       __|__''',
      '''
         _____
         |  |
         |  O
         |  |
         |  
         | 
         |
       __|__''',
      '''
         _____
         |  |
         |  O
         | \|
         |
         |
         |
       __|__''',
      '''
         _____
         |  |
         |  O
         | \|/
         |
         |
         |
       __|__''',
      '''
         _____
         |  |
         |  O
         | \|/
         |  |
         |
         |
       __|__''',
      '''_____
         |  |
         |  O
         | \|/
         |  |
         |  |
         |
       __|__''',
      '''
         _____
         |  |
         |  O
         | \|/
         |  |
         |  |
         | /
         |
       __|__''',
      '''
         _____
         |  |
         |  O
         | \|/
         |  |
         |  |
         | / \
         |
       __|__'''
      ]
    return tiles[i]
