import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(None, "Ask The Magic 8 ball a question: ")
    # Make a variable and initialize it to a random number between 0 and 3
    rand = random.randint(1,4)
    # If the random number is 0
    def msg(msg):
        messagebox.showinfo(None, message= msg)
        # tell the user "Yes"
    if rand == 1:
        msg("Yes")
    # If the random number is 1
    elif rand == 2:
        msg("No")
        # tell the user "No"
    elif rand == 3:
        msg("Go ask Google.")
    # If the random number is 2
    else:
        msg("The magic 8 ball does not wish to comment on this question.")
        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
