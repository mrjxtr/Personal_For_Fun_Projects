

secret_word = "bubby"
guess = ""
count = 0
limit = 3
limitx = False

print("WELCOME TO MR J XTR's GUESSING GAME!")

while guess != secret_word and limitx == False:
    if count < limit:
        guess = input("guess a word: ")
        if guess == secret_word:
            print("YOU GOT THE RIGHT WORD!")
            print("YOU WIN!")
        else:
            print("wrong word")
            count += 1
    else:
        limitx = True
        print("OUT OF GUESSES")
        print("YOU LOSE!")
