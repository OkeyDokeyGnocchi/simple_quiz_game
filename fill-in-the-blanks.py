#Python program that runs a fill-in-the-blanks game.

#Global variables, lists, etc.
blanks = ["__1__", "__2__", "__3__", "__4__"]

quiz_one = '''This program was written in a common language called __1__.  __1__'s used for __2__ . A __3__ introduced to new programmers is the print statement.  Many users start with hello __4__ .-'''
quiz_two = '''Python is used for two main purposes: __1__ and __2__.  The first, __1__ is used to develop programs that run on computers.  The second, __2__ , is used to __3__ tasks so that you don't have to do them manually!  Remember, you'll need to __4__ your source code for it to run!-'''
quiz_three = '''To bring in additional __1__ for use in your code, you'll need to use the __2__ function.  For example: if you want to generate a random number, you'll need to use __2__ __3__ at the beginning of your code.  If you need to use __1__ that aren't included with Python, you can download __4__ from the official repository.-'''

answers_one = ['python', 'programming', 'function', 'world']
answers_two = ['programming', 'scripting', 'automate', 'compile']
answers_three = ['libraries', 'import', 'random', 'packages']


#Minor functions
def wordInBlank(word, blanks):
    '''This function checks the blanks in each quiz.  It takes in
    the local blank and the list blanks, then returns the word if it
    lines up with the current word in the quiz.'''

    for blank in blanks:
        if blank in word:
            return blank

    return 'notPresent'

def selectLevel(player_level):
    '''This function takes in player_level as the player's
    selected level and outputs the correct quiz and answers
    for that level.'''

    if player_level == '1':
        print "#Easy mode, huh? Well, ok, I guess.#\n"
        return quiz_one, answers_one
    elif player_level == '2':
        print "#Medium?  Moving up in the world.#\n"
        return quiz_two, answers_two
    else:
        print "#Hard-mode it is.  I hope you're ready.#\n"
        return quiz_three, answers_three


def fillInBlank(word, filledIn, player_answer, index, blanks):
    '''This function replaces the blanks in the quiz with the correct
    answer. It takes in the blanks list, the quiz as it is up to this point
    with entered answers, the player's answer for the given blank,
    and the index that matches the player's answer with the correct blank.
    At the end of the process it outputs the quiz with the correct answers
    filled in.'''

    if wordInBlank(word, blanks) == 'notPresent':
        filledIn.append(word)

    else:
        replacement = wordInBlank(word, blanks)
        word = word.replace(replacement, player_answer)

        if replacement == blanks[index]:
            if replacement not in filledIn:
                filledIn.append(word)
            else:
                location = filledIn.index(replacement)
                filledIn[location] = word
        else:
            filledIn.append(replacement)

    return filledIn

def replaceBlanks(quiz, blanks, player_answer, filledIn, index):
    '''This function is complementary to the fillInBlank function.
    This function will replace the individual blanks with the correct answers.
    It takes in the quiz, the blanks list, the quiz with answers in it so far,
    the player's guess for the current blank, and the index to match up the
    player answer and the blank.  It outputs the quiz with replaced correct answers.'''

    quiz = quiz.split()

    if type(filledIn) == str:  #fixing the "str obj has no attribute" error... This took way longer to find than I'd like to admit.  Would love feedback on why this is necessary and how it could have been avoided....  Credit to stackoverflow for explaining the error and how to use type to fix it"
		filledIn = filledIn.split()

    for word in quiz:
        fillInBlank(word, filledIn, player_answer, index, blanks)

    filledIn = " ".join(filledIn)
    body, stop, tail = filledIn.partition("-")  #This took me way too long to figure out, but for some reason it prints extra "blanks" after the quiz.  Why does this happen?  In searching for help I learned about partition(), but why is this necessary???  As before, credit to stackoverflow for helping me realize this was my issue.  Also docs.python.org for the explanation on partition.
    filledIn = body + stop    #partition() returns a tuple (docs.python.org).  Turns out I needed positions 1 and 2.  I spent a long time testing and wondering why it kept returning the blanks again.... I needed body + stop, not just body.
    return filledIn

def getAnswers(player_level, quiz, answers):
    '''This function gets the player's answers and also tests if the answer
    is right or wrong.  Additionally, it checks the number of tries a player has left
    and prompts the player to retry if they get too many attempts wrong.  It
    takes in the player's selected level, the quiz, and the correct answers, and
    spits out the updated quiz and the index of each answer.  If the player
    is incorrect it also outputs their remaining attempts.'''

    index = 0
    player_answer = ""
    filledIn = []
    attempts = 5

    for blank in blanks:
        player_answer = raw_input("\n#Please type an answer for " + blank + ": #")

        while player_answer != answers[index]:
            attempts = attempts - 1
            print "Not quite... You have " + str(attempts) + " extra guesses remaining." +"\nTry again."
            player_answer = raw_input("\n#Please type an answer for " + blank + ":# ")
            if attempts == 0:
                gameOver()


        print "\n#That's right!#\n"

        filledIn = replaceBlanks(quiz, blanks, player_answer, filledIn, index)
        print filledIn
        index = index + 1

    return filledIn

def gameOver():
    '''This function is only called when the player answers incorrectly
    too many times.  It gives the player a chance to retry, and if they refuse,
    it terminates the program.'''


    try_again = raw_input("Would you like to try again?(y,n): ")
    if try_again == 'y':
        print "#Let's give it another shot!#"
        quizTime()
    elif try_again == 'n':
        exit()
    else:
        print "Please select 'y' or 'n'."
        gameOver()

#Game function
def quizTime():
    '''This is the game function itself.  No inputs here, but it does
    output the game.  Fun stuff.'''

    print "#Hi there!  Welcome to the quiz!#\n"
    player_level = raw_input('#Which level would you like to play(1-3)? #\n')

    if player_level == '1' or player_level == '2' or player_level == '3':
        quiz, answers = selectLevel(player_level)
        print quiz

        filledIn = getAnswers(player_level, quiz, answers)
        print "\n#A winner is you!#\n"

        play_again = raw_input("Would you like to play again?(y,n): ")
        if play_again == 'y':
            quizTime()
        else:
            exit()

    else:
        print "#Play by the rules... Let's start over, OK?#"
        quizTime()

quizTime()

#In addition to stackoverflow and docs.python.org I need to credit the madlibs chunk of the course.  getAnswers, fillInBlank, and replaceBlanks borrowed directly from the concepts taught in that lesson. wordInBlank is very similar to the madlibs lesson as well.
