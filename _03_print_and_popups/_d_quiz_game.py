from tkinter import messagebox, simpledialog, Tk
from easygui import *
# Create an if-main code block, *hint, type main then ctrl+space to auto-complete
if __name__ == '__main__':
    # Make a new window variable, window = Tk()
    window = Tk()
    # Hide the window using the window's .withdraw() method
    window.withdraw()
    # 1. Create a variable to hold the user's score. Set it equal to zero. 
    score = 0
    # ASK A QUESTION AND CHECK THE ANSWER

    #      // 2.  Ask the user a question 
    
  
    # item choices
    choices = ["Fish", "Frog", "Dragon", "Crane"]
  
    # creating a button box
    output = choicebox("According to Japanese legend, a sick person will recover if they fold 1,000 of what type of origami?", "questions", choices)
    

        #      // 3.  Use an if statement to check if their answer is correct
    if str(output) == "Crane":
        messagebox.showinfo("Quiz Game","you got it correct")
        score+=1
    else:
        messagebox.showinfo("Quiz Game","you got it wrong")
        score-=1
    
    
    choices1 = ["Adolf Hitler", "Mahatma Ghandi", "Henry Ford", "Charles Lindbergh"]
  
    # creating a button box
    output = choicebox("Who was the first Time Magazine Man of the Year?", "questions", choices1)
    

        #      // 3.  Use an if statement to check if their answer is correct
    if str(output) == "Charles Lindbergh":
        messagebox.showinfo("Quiz Game","you got it correct")
        score+=1
    else:
        messagebox.showinfo("Quiz Game","you got it wrong")
        score-=1
    messagebox.showinfo("Questions","Your final score was " + str(score))
        #      // 4.  if the user's answer was correct, add one to their score 
    
        # MAKE MORE QUESTIONS. Ask more questions by repeating the above 
        #      // Option: Subtract a point from their score for a wrong answer
    
        # After all the questions have been asked, tell the user their final score
        # remember to convert your variable to a string using the str() function 
        
        # Run the window's .mainloop() method
