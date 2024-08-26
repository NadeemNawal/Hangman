import random
import hangman_art
import hangman_list
end_of_game = False
# set lives avriable=6
lives = 6
print(hangman_art.logo)

# to do. randomly choose a word from the word_list and assign it to a variable called chosen_word
# ask the user to guess a letter and assign their answer to a variable called guess. make guess lowercase.
# check if the letter the user guessed (guess) is one of the letters in the chosen_word
chosen_word = random.choice(hangman_list.word_list)
word_length = len(chosen_word)
# print(chosen_word)
# create an empty list of blanks called display. for each letter in the chosen word, add a blank to  display
display = []
for _ in range(word_length):
  display += "_"
  # or display = display + "_"
print(display)
# loop through each position in the chosen word. if the letter at that position matches guess then reveal that letter in the display at that position.
# if all blanks are filled. you have won or if lives are used, you lose. while loop has to break in both conditions.
while not end_of_game:
  guess = input("Guess a Letter ").lower()
  if guess in display:
    print(f"You have already guessed{guess}")
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
      print(display)

  if "_" not in display:
    end_of_game = True
    print("You win")

  if guess not in chosen_word:
    lives = lives-1
    if lives == 0:
      end_of_game = True
      print("You lose!", "The word was", chosen_word)
  print(hangman_art.Stages[lives])
