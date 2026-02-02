import random
word_bank = ['rizz', 'ohio', 'sigma', 'tiktok', 'skibidi']
word = random.choice(word_bank) # The random.choice method is used to randomly select a word from the word_bank list and to assign it to the word variable.
guessedWord = ['_'] * len(word) # This line initializes the guessedWord list with underscores, representing unguessed letters.
attempts = 10
while attempts > 0:
    print('\nCurrent word: ' + ' '.join(guessedWord)) # Each time the loop runs, we will display the curremt state of the word being guessed. 

    guess = input('Guess a letter: ').lower() # In the statement above, the \n prints the statement on a new line and joins the strings in guessedWrod together with spaces.

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessedWord[i] = guess
        print('Great guess!')
    else: # This part of the code handles the case when the guessed letter is incorrect, thus reducing the number of guesses the plauer has. 
        attempts -= 1
        print('Wrong guess! Attempts left: ' + str(attempts))
    if '_' not in guessedWord: # This below section of the code handles the situation when the plauer hs guessed all of the letters in the code and there are no udnerscores left. 
        print('\nCongratulations! You guessed the word: ' + word)
        break
if attempts == 0 and '_' in guessedWord:
    print('\nYou\'ve run out of attempts! The word was: ' + word) # This part of the code handles the situation when the player has run out of attempts and still has not guessed the word correctly.