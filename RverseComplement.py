#coding=utf-8
import tkinter as tk
import tkinter.font as tkFont

#titleFont = tkFont.Font(family = "Fixdsys", size = 16, weight = tkFont.BOLD)
#labelFont = tkFont.Font(family = "Yu Gothic UI",size = 10,weight = tkFont.BOLD)

root = tk.Tk()
#"500x300+350+240"
#widthxheight+x+y (x and  y are where the window appears)
root.geometry("500x300+350+240")
root.title("Rverse Complement Calculator")

mainTitle = tk.Label(root,text="Get Rverse Complement of a Sequence"
	,font="Times 15 bold")
mainTitle.pack()
mainTitle.place(x = 30, y = 10,width = 440,height = 30)


text1 =tk.Label(root,text = "Original sequences",font = "Yu\ Gothic\ UI 8 bold")
text1.pack()
text1.place(x = 10, y = 50, height = 20, width = 100)

# scrollbar1 = tk.Scrollbar(root)
# scrollbar1.pack(side="bottom",fill = "x",orient=HORIZONTAL)

#textInput = tk.Entry(root,xscrollcommand=scrollbar1.set)
textInput = tk.Entry(root)
textInput.pack()
textInput.place(x = 160, y =50, height = 30, width = 320)

#scrollbar1.config(command = textInput.xview)

text2 = tk.Label(root,text="Reverse Complement",font = "Yu\ Gothic\ UI 8 bold")
text2.pack()
text2.place(x = 10, y = 90, height = 20, width = 110 )

textOutput = tk.Text(root,wrap="word")
textOutput.pack()
textOutput.place(x = 160, y = 90, height = 200, width = 320)


def print_content():
#	print(reverseComplement(textInput.get()))	
#	var.set(value = reverseComplement(textInput.get()))
#	print(var.get())
	textOutput.delete(1.0,"end")
#	print(textInput.get())
#	txt = textInput.get()
	#print(type(text))
	#var.set(value = reverseComplement(text))
	#textOutput.insert(reverseComplement(text))
	textOutput.insert(1.0,reverseComplement(textInput.get()))
def reverseComplement(inputStr):
	query = inputStr.upper()
#	print(query)
	reverse_complement = ""
	for letter in query:
		if letter == 'A':
			reverse_complement += 'T'
		elif letter == 'T':
			reverse_complement += 'A'
		elif letter == 'G':
			reverse_complement += 'C'
		elif letter == 'C':
			reverse_complement += 'G'
#	print(reverse_complement)	
	reverse_complement = reverse_complement[::-1]
#	print(reverse_complement)
	return reverse_complement




# tk.Button(root,text="print",command = print_content).pack()	
root.bind("<Return>",lambda event:print_content()) #<Return> refer to Enter

# textOutput = tk.Message(root,textvariable = var)
# textOutput.pack()
root.mainloop()