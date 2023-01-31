#https://www.loom.com/share/d79ae31ffd6d4ab8b63c818d49b7430d


from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x500")
root.title("Class")

element1 = ["Label" , "Button" , "Drop Down" , "Enput Box"]
selected_element = StringVar()
drop_down = ttk.Combobox(root, values = element1 , textvariable= selected_element)
drop_down.pack()

class create_element:
    
    def __init__(self):
        print("xyz")
        
    def create_new_element(self):
        selected_item = selected_element.get()
        if selected_item == "Label" :
            label1 = Label(root , text = "hello")
            label1.pack(padx = 20 , pady = 20)
            
        elif selected_item == "Button" :
            btn1 = Button(root , text = "button")
            btn1.pack(padx = 20 , pady = 20)
            
        elif selected_item == "Drop Down" :
            new_element = ["1" , "2" , "3"]
            new_element1 = StringVar()
            drop_down = ttk.Combobox(root, values = new_element  , textvariable= new_element1)
            drop_down.pack(padx = 20 , pady = 20)
            
        elif selected_item == "Enput Box" :
            enput1 = Entry(root)
            enput1.pack(padx = 20 , pady = 20)
            
             
            
object1 = create_element()
btn = Button(root , text = "Click to generate new element" , command = object1.create_new_element)
btn.pack(padx = 20 , pady = 20)
            
root.mainloop()
        




        
        
