'''

author: Tarun R Jain
complete content is my own
github: github.com/lucifertrj

'''

#read comments to follow, Thank you -TRJ
import random,string
import tkinter as tk
from tkinter import messagebox as mb

def random_password():
    letters=[random.choice(string.ascii_letters) for letter in range(8)]  #list of random 8 letters(both uppercase and lowercase included)
    numbers=[random.choice(string.digits) for digit in range(3)] #list of random 3 numbers from 0-9 
    character=[random.choice(string.punctuation) for symbols in range(4)] #list of 4 random punctuation
    password=letters+character+numbers
    random.shuffle(password) #dont return this statement inside return block, as random.shuffle returns none
    return(password) #the password is shuffled

def generate():
    #enter a valid username to avoid warning messages
    username=name_var.get()
    if username=='': #empty name will rise a error
        mb.askretrycancel("Error occured","User not recognized")
    elif len(username)<=3: #a valid username consists of atleast 4 or 5 minimum characters
        mb.askretrycancel("Invalid Entry","Please enter a proper name")
    elif username[0] in string.digits:
        mb.askretrycancel("Alert","Dont play with me, enter valid name")
    else:
        #lets a use a while loop to iterate unless the user is satisfed
        while True:
            password=random_password()
            answer=mb.askquestion(f"{username}'s:Random password",f"{''.join(password)}\nAre you satisfed?").lower()
            if answer.startswith('y'):
                mb._show(" ","Thank You")
                break
            else:
                continue
                        
def main():
    global root
    root=tk.Tk()
    root.title("Password Generator")
    root.geometry("455x455")
    root.minsize(425,425)
    title=tk.Label(root,text="Random Password Generator",font=("Times New Roman",20,"bold")).grid(row=0,column=2)
    name=tk.Label(root,text="Name:").grid(row=2,column=1)
    global name_var
    name_var=tk.StringVar()
    name_entry=tk.Entry(root,textvariable=name_var).grid(row=2,column=2)
    button=tk.Button(root,text="Generate Password",command=generate).grid(row=3,column=2)
    root.mainloop()
    
if __name__ == '__main__':
    main()
    
