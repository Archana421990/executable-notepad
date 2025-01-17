
#https://www.youtube.com/watch?v=sQErlafZrjQ
#https://www.youtube.com/watch?v=iyJ1_ODzNUk&t=3s    (https://www.geeksforgeeks.org/make-notepad-using-tkinter/)


# new with more functions
#https://www.javatpoint.com/make-notepad-using-tkinter


import tkinter as tk   #library
from tkinter.filedialog import askopenfilename, asksaveasfilename #import 2 functions from tkinter package
window=tk.Tk()    #gui variable
window.title("Notepad") #give name to it

# assign minimum size of row and column
window.rowconfigure(0, minsize=600, weight=1) #define row, column configuration
window.columnconfigure(1, minsize=800, weight=1)  #define row, column configuration

""" def new_file(**kwargs):
    window.title("Notepad")
    file=None
    filepath = askopenfilename(
        filetypes =[("Text Files", "***kwargs")]
    )
    if not filepath: #if not filetype then return nothing
        return
    txt_edit.delete(1.0, tk.END) """
    
def open_file(): #create open file function
    filepath = askopenfilename(
        filetypes =[("Text Files", "*.txt"),("All Files","*.*")]
    )
    if not filepath: #if not filetype then return nothing
        return
    txt_edit.delete(1.0, tk.END)
    with open(filepath,"r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Notepad - {filepath}")
    
def save_file():
    filepath = asksaveasfilename(
        defaultextension = "txt",
        filetypes= [("Text Files", "*.txt"), ("All Files", "*.*")],       
        )
    if not filepath:
        return
    with open(filepath,"w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Notepad - {filepath}")            

txt_edit= tk.Text(window)# define text window frame
fr_buttons =tk.Frame(window, relief=tk.RAISED, bd=2) #define frames for buttons, bd means border
btn_open=tk.Button(fr_buttons, relief=tk.SOLID, command=open_file, text="Open") # create open button to adjust with the frame to open files
btn_save=tk.Button(fr_buttons, text="Save As", command=save_file, relief=tk.SOLID) #create save button to adjust with the frame to save files

btn_open.grid(row=0, column=0, sticky="ew", padx=10, pady=10) #define position on grid to open the file so that we can see on window
btn_save.grid(row=1, column=0, sticky="ew", padx=10) #define position on grid to save the file so that we can see on window


fr_buttons.grid(row=0, column=0, sticky="ns") #define button frame on window grid - size of the content
txt_edit.grid(row=0, column=1, sticky="nsew") #define button frame on window grid - size of content for editing om grid


#run main loop
window.mainloop()


#define two functions one for open and another for edit
#filedialog needed so import and also
#define the functionalities of open and save as



#https://www.javatpoint.com/simple-to-do-list-gui-application-in-python
