#coding=utf-8
#calculate the length of sting inputs
import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("500x300+350+240")
root.title("Length of Sequence")

mainTitle = tk.Label(root,text="Get Length of a Sequence"
	,font="Times 15 bold")
mainTitle.pack()
mainTitle.place(x = 30, y = 10,width = 440,height = 30)


text1 =tk.Label(root,text = "Original Seuqence",font = "Yu\ Gothic\ UI 8 bold")
text1.pack(expand=1, fill=tk.BOTH)
text1.place(x = 10, y = 90, height = 20, width = 110 )

textInput = tk.Entry(root)
textInput.pack()
textInput.place(x = 160, y = 50, height = 200, width = 320)

text2 = tk.Label(root,text="Original Seuqence",font = "Yu\ Gothic\ UI 8 bold")
text2.pack()
text2.place(x = 10, y = 265, height = 20, width = 100)

textOutput = tk.Text(root,wrap="word")
textOutput.pack()
textOutput.place(x = 160, y =265, height = 20, width = 300)

def print_content():
    textOutput.delete(1.0,"end")
    textOutput.insert(1.0,calculateLengthOfString(textInput.get()))

#don't calculate blanks in sequence
def calculateLengthOfString(inputStr):
    import re
    query = inputStr.upper()
    lengthOfString = 0
    for letter in query:
        if letter in ['A','T','C','G']:
            lengthOfString += 1
        elif letter == " ":
            continue
        elif re.match('[a-zA-Z]',letter) is not None:
            return "not only ATCG!"
            break        
    return lengthOfString

root.bind("<Return>",lambda event:print_content())
root.mainloop()