from tkinter import StringVar, TOP
from tkinterdnd2 import TkinterDnD, DND_ALL
import customtkinter as ctk

from main import transcribe_audio

class Tk(ctk.CTk, TkinterDnD.DnDWrapper):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)
        self.geometry("350x150")
        ctk.set_appearance_mode("dark")
         # Pack DragAndDrop widget first
        self.dnd_widget = DragAndDrop(self)
        self.dnd_widget.pack(fill="both", expand=True)


class DragAndDrop(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #nameVar = StringVar()
      

        self.entryWidget = ctk.CTkEntry(self)
        self.entryWidget.pack(side=TOP, padx=5, pady=5) 

        self.pathLabel = ctk.CTkLabel(self, text="Drag and drop file in the entry box")
        self.pathLabel.pack(side=TOP)

        self.button = ctk.CTkButton(master=self, text="Transcribe", command=self.button_event)
        self.button.pack(padx=20, pady=10)

        self.entryWidget.drop_target_register(DND_ALL)
        self.entryWidget.dnd_bind("<<Drop>>", self.get_path)

       

    
    def get_path(self,event):
        self.pathLabel.configure(text = event.data)
        self.filepath = event.data
        
    def button_event(self):
        print("button pressed")
        transcribe_audio(self.filepath)

#tk.set_appearance_mode("dark")
#ctk.set_default_color_theme("blue")

#def get_path(event):
    #pathLabel.configure(text = event.data)

#root = TkinterDnD.Tk()
if __name__ == "__main__":
    root = Tk()  # Create the root window
    
    root.mainloop()  # Start the main event loop
