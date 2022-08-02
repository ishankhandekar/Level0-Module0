from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range(10):
        # 4. Ask the user for a guess using a pop-up window, and save their response
        guess=simpledialog.askinteger("Game","What is your guess for a random number")
        
        # 5. If the guess is correct
            # 6. Win. Use 'sys.exit(0)' to end the program
        if guess == random_num:
            messagebox.showinfo("Game","You won")
            sys.exit(0)
        elif guess > random_num:
            messagebox.showinfo("Game","Your guess is too high.")
        elif guess < random_num:
            messagebox.showinfo("Game","Your guess is too low.")
        # 7. if the guess is high
            # 8. Tell them it's too high
        # 9. Else if the guess is low
            # 10. Tell them it's too low
    messagebox.showinfo("Game","You didn't get the answer in time.")
    #11. Outside of the loop, tell the user they lost

    window.mainloop()
