# IPND Stage 2 Final Project

# A list of replacement words to be passed in to the play game function.
placeholders  = ["___1___", "___2___", "___3___", "___4___"]

# Solutions
level1Solution = ["Peter", "peck", "pickled", "peppers"]
level2Solution = ["flea", "fly", "flew", "flue"]
level3Solution = ["need", "needles", "needless", "see"]
level4Solution = ["dame", "tree", "toed", "The"]

# Quizes
level1 = '''___1___ Piper picked a ___2___ of ___3___ ___4___;
A ___2___ of ___3___ ___4___ ___1___ Piper picked.
If ___1___ Piper picked a ___2___ of ___3___ ___4___,
Where's the ___2___ of ___3___ ___4___ ___1___ Piper picked?'''
# source: http://www.lbt-languages.de/de/englisch-hilfen/englisch-lernhilfen/tongue-twister/
# on May 4th 2016

level2 = '''A ___1___ and a ___2___ ___3___ up in a ___4___.
Said the ___1___, "Let us ___2___!"
Said the ___2___, "Let us flee!"
So they ___3___ through a flaw in the ___4___.'''
# source: http://www.lbt-languages.de/de/englisch-hilfen/englisch-lernhilfen/tongue-twister/
# on May 4th 2016

level3 = '''I ___1___ not your ___2___, they're ___3___ to me;
For kneading of noodles, 'twere ___3___, you ___4___;
But did my neat knickers but ___1___ to be kneed,
I then should have ___1___ of your ___2___ indeed.'''
# source: http://www.lbt-languages.de/de/englisch-hilfen/englisch-lernhilfen/tongue-twister/
# on May 4th 2016

level4 = '''My ___1___ hath a lame tame crane,
My ___1___ hath a crane that is lame.
A ___2___ toad loved a she-toad
Who lived up in a ___2___.
He was a two-___3___ ___2___ toad
But a three-___3___ toad was she.
___4___ two-___3___ ___2___ toad tried to win
___4___ three-___3___ she-toad's heart,
For the two-___3___ ___2___ toad loved the ground
That the three-___3___ ___2___ toad trod.
But the two-___3___ ___2___ toad tried in vain.
He couldn't please her whim.
From her ___2___ toad bower
With her three-___3___ power
___4___ she-toad vetoed him.'''
# source: http://www.lbt-languages.de/de/englisch-hilfen/englisch-lernhilfen/tongue-twister/
# on May 4th 2016

welcomeString = '''Please select a game difficulty by typing it in!
Possible choices include easy, medium, hard and extreme.
Your choice: '''
choiceMadeString = '\n' + "You will get 5 guesses per problem."

currentString = "Right now, the current paragraph reads as such:"

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Gives quiz according to chosen difficulty level.
def quizAccordingToDifficulty(difficulty):
	if difficulty == "easy":
		return level1
	elif difficulty == "medium":
		return level2
	elif difficulty == "hard":
		return level3
	elif difficulty == "extreme":
		return level4
	else:
		return "Ooops, something went wrong!"

# Gives solution according to chosen difficulty level.
def solutionAccordingToDifficulty(difficulty):
	if difficulty == "easy":
		return level1Solution
	elif difficulty == "medium":
		return level2Solution
	elif difficulty == "hard":
		return level3Solution
	elif difficulty == "extreme":
		return level4Solution
	else:
		return "Ooops, something went wrong!"

# Prints current state of the quiz with a message
def printQuiz(quiz):
	return currentString + '\n'*2 + quiz + '\n'

# Checks if a chosen difficulty level is a valid choice, returns True if it is,
# False if not.
def checkValidityOfChosenDifficulty(difficulty):
	if difficulty == "easy" or difficulty == "medium" or difficulty == "hard" or difficulty == "extreme":
		return True
	return False

# Handles a correct answer, prints message
def correctAnswer(quiz, word, solution):
	quiz = quiz.replace(word,solution)
	print '\n' + "Correct!"
	return quiz

# Handles a wrong answer given the trys left, prints message
def wrongAnswer(trysLeft):
	trysLeft -= 1
	if trysLeft > 0:
		print '\n' + "Wrong answer. You have " + str(trysLeft) + " trys left."
	else:
		print "Game Over"
	return trysLeft

# Handles players win, prints message
def winAnswer(quiz):
	print '\n' + "Congratulation, you won!" + '\n'*2 + "Your correct solution is:" + '\n'*2 + quiz

# Handles communication with user until difficulty is chosen
def chooseDifficulty():
	user_difficulty = raw_input(welcomeString)
	while not checkValidityOfChosenDifficulty(user_difficulty):
		user_difficulty = raw_input(welcomeString)
	print choiceMadeString
	return user_difficulty

# Handles a word the user put in and returns the None if the user has more than 5 wrong guesses
# and the quiz after filling in the correct answer, if the user found the correct answer
def wordInput(quiz, word, solution):
	trysLeft = 5
	while trysLeft > 0:
		user_input = raw_input("What should be substituded in for " + word + "?" + '\n'
			+ "Your guess: ")
		while user_input == "":
			user_input = raw_input("Make a guess for " + word + ". The game will end after 5 wrong guesses." + '\n' + "Your guess: ")
		if user_input == solution:
			return correctAnswer(quiz, word, solution)
		else:
			trysLeft = wrongAnswer(trysLeft)
	return

# Plays a full game of mad_libs. A player is prompted to replace words in ml_string,
# which appear in parts_of_speech with their own words.
def play_game(parts_of_speech):
	user_difficulty = chooseDifficulty()
	quiz = quizAccordingToDifficulty(user_difficulty)
	indexOfWordToBeReplaced = 0
	while indexOfWordToBeReplaced < len(placeholders):
		print '\n' + printQuiz(quiz)
		word = placeholders[indexOfWordToBeReplaced]
		solution = solutionAccordingToDifficulty(user_difficulty)[indexOfWordToBeReplaced]
		quiz = wordInput(quiz,word,solution)
		if quiz == None:
			return
		indexOfWordToBeReplaced += 1
	winAnswer(quiz)

play_game(placeholders)