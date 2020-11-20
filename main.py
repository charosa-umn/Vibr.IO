import tkinter as tk
from model_page import ModelPage
from start_page import StartPage

WINDOW_SIZE = "1366x768"


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry(WINDOW_SIZE)  # set window size

        container = tk.Frame(self)  # container frame will hold all possible frames of app
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.pack()

        self.frames = {}  # define a dictionary of frames in the app

        # Create a frame for each of the classes
        for F in (ModelPage, StartPage):
            page_name = F.__name__  # string name of class is F.__name__
            frame = F(container, self)  # parent of frame is container. Pass in self to allow frame to use Main's funcs
            frame.grid(row=0, column=0, sticky="nsew")  # stack all of the frames on top of each other
            self.frames[page_name] = frame  # assign to dictionary for easy access later

        self.show_frame("StartPage")  # Show the start page first

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]  # Get frame from dictionary
        frame.tkraise()  # raise that frame to the top of the stack


if __name__ == "__main__":
    root = Main()
    root.mainloop()
