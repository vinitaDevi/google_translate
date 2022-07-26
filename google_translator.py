from tkinter import *  #for graphic window
from tkinter import ttk #ttk class create combo box
from googletrans import Translator,LANGUAGES  #translator and languages are classes

def change(text="type", src="English", dest="Hindi"): # function for calling Translator function
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1.text


def data(): 
    s = comb_sor.get() #storing data from source
    d= comb_dest.get()  #storing data from destination
    msg = sor_text.get(1.0,END)
    textget = change(text=msg,src=s,dest=d) # calling change function
    dest_text.delete(1.0,END)
    dest_text.insert(END,textget)




root = Tk() #it gives graphic window
root.title("Translator")
root.geometry("500x700") #width x height
root.config(bg='grey') #background color

lab_txt = Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg='grey')
lab_txt.place(x=100,y=40,height=50,width=300) 

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root,text="Source Text",font=("Time New Roman",20),bg='grey',fg="Black")
lab_txt.place(x=10,y=100,height=22,width=170) 

sor_text = Text(frame,font=("Time New Roman",20,"bold"),wrap=WORD)
sor_text.place(x=10,y=130,height=150,width=480) 

list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=30,width=150) 
comb_sor.set("English")

button_change = Button(frame,text = "Translate",relief=RAISED,command=data) 
button_change.place(x=170,y=300,height=30,width=150) 

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=30,width=150) 
comb_dest.set("English")

sor_text = Text(frame,font=("Time New Roman",20),wrap=WORD)
sor_text.place(x=10,y=130,height=150,width=480) 

lab_txt = Label(root,text="Destination Text",font=("Time New Roman",20),bg='grey',fg="Black")
lab_txt.place(x=10,y=370,height=22,width=220) 

dest_text = Text(frame,font=("Time New Roman",20),wrap=WORD)
dest_text.place(x=10,y=400,height=150,width=480)

root.mainloop() 