from tkinter import TOP
from tkinterdnd2 import TkinterDnD, DND_ALL
import customtkinter

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(master=self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()




from tkinter import TOP
from tkinterdnd2 import TkinterDnD, DND_ALL
import customtkinter as ctk
from main import transcribe_audio

class Tk(ctk.CTk, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        TkinterDnD.DnDWrapper.__init__(self)
        self.TkdndVersion = TkinterDnD._require(self)
        
        self.minsize(350, 180)
        ctk.set_appearance_mode("dark")
        
        # Pack DragAndDrop widget first
        self.dnd_widget = DragAndDrop(self)
        self.dnd_widget.pack(fill="both", expand=True)
        
        self.button = ctk.CTkButton(master=self, text="Transcribe", command=self.button_event)
        self.button.pack(padx=20, pady=20)

    def button_event(self):
        transcribe_audio()
        print("button pressed")

class DragAndDrop(ctk.CTkFrame):
    def __init__(self, parent, *args, **kwargs):
        ctk.CTkFrame.__init__(self, parent, *args, **kwargs)
        
        self.entryWidget = ctk.CTkEntry(self)
        self.entryWidget.pack(side=TOP, padx=5, pady=5)

        self.pathLabel = ctk.CTkLabel(self, text="Drag and drop file in the entry box")
        self.pathLabel.pack(side=TOP)

        self.entryWidget.drop_target_register(DND_ALL)
        self.entryWidget.dnd_bind("<<Drop>>", self.get_path)
    
    def get_path(self, event):
        self.pathLabel.configure(text=event.data)

if __name__ == "__main__":
    root = Tk()  # Create the root window
    root.mainloop()  # Start the main event loop
