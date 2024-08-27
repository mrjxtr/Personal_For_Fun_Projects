# importing module from Question py file that has Questions class
from Proj_Question import Questions

# These are the list of questions.
prompts = [
    "\n1) What is the capital city of the Philippines?\n(a) Davao\n(b) Cebu\n(c) Manila\n\nAnswer: ",
    "\n2) How many moons are there in the Philippine flag?\n(a) 3\n(b) 0\n(c) 5\n\nAnswer: ",
    "\n3) Are there more than 7 thousand islands in the Philippines?\n(a) Yes\n(b) No\n\nAnswer: ",
    "\n4) What is the biggest major island in the Philippines?\n(a) Luzon\n(b) Visayas\n(c) Mindanao\n\nAnswer: ",
    "\n5) What is the Philippines' national language?\n(a) English\n(b) Spanish\n(c) Filipino\n\nAnswer: ",
]

# These are the question objects.
questions = [
    Questions(prompts[0], "c"),
    Questions(prompts[1], "b"),
    Questions(prompts[2], "a"),
    Questions(prompts[3], "a"),
    Questions(prompts[4], "c"),
]


# This is the code to run the test.
def start_test(question):
    cont = True
    end = False
    # While loop so I can restart game if I want
    while cont:
        score = 0
        print("\n\n==================\nWELCOME TO MY GAME\n==================")
        # for loop logic while game is ongoing
        for q in question:
            answer = str.lower(input(q.prompts))
            if answer == q.answer:
                score += 1
            else:
                score = score
        # if to output text based on score
        if score == len(questions):
            print(
                "\nGreat! You have "
                + str(score)
                + "/"
                + str(len(questions))
                + " correct\nAWESOME JOB!"
            )
        else:
            print(
                "\nYou have "
                + str(score)
                + "/"
                + str(len(questions))
                + " correct\nTRY AGAIN!"
            )
        reply = input("\nDo you want to try again?: Y/N: ")

        #### IGNORE THIS CODE (THIS WAS CAUSING BUGS IN THE Y/N LOOP)
        # While loop so I can loop prompt to try again
        #        while reply not in ("Y", "N", "y", "n", "yes", "Yes", "YES", "NO", "No", "no"):
        #            reply = input('\nPlease answer with "Y" or "N": ')
        #### IGNORE THIS CODE (THIS WAS CAUSING BUGS IN THE Y/N LOOP)
        #            if reply not in ("Y", "N", "y", "n", "yes", "Yes", "YES", "NO", "No", "no"):
        #                    reply = input('\nPlease answer with "Y" or "N": ')

        # finally fixed tha code by placing the while loop in the midle of the Y/N loop
        if reply in ("Y", "y", "yes", "Yes", "YES"):
            cont = cont
        elif reply in ("N", "n", "no", "No", "NO"):
            cont = end

        while reply not in ("Y", "N", "y", "n", "yes", "Yes", "YES", "NO", "No", "no"):
            reply = input('\nPlease answer with "Y" or "N": ')

        if reply in ("Y", "y", "yes", "Yes", "YES"):
            cont = cont
        elif reply in ("N", "n", "no", "No", "NO"):
            cont = end
    else:
        cont = end


# I am sure there is a better way to code this, but it works for now.
# This is when the test ends
start_test(questions)
print("\n\n======================\nTHANK YOU FOR PLAYING!\n======================")
