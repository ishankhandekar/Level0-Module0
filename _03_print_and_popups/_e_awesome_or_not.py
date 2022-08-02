from tkinter import messagebox, simpledialog, Tk
import random

# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Make a variable equal to a positive number less than 4 using random.randInt(0, 3)
    rand = random.randInt(0, 3)
    # 2. Print your variable to the console
    print(rand)
    # 3. Get the user to enter something that they think is awesome
    awesome = input("enter something you think is awesome")
    # 4. If your variable is  0
        # -- tell the user whatever they entered is awesome!
    if rand == 0: 
        print(awesome + "is awesome") 
    elif rand == 1:
        print(awesome + "is ok")
    elif rand == 2:
        print(awesome + "is boring")
    elif rand == 3:
        print(awesome + "is the worst")
    # 5. If your variable is  1
        # -- tell the user whatever they entered is ok.
    
    # 6. If your variable is  2
        # -- tell the user whatever they entered is boring.
    
    # 7. If your variable is  3
        # -- invent your own message to give to the user (be nice).
        
    # Run the window's .mainloop() method
