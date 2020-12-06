"""
Class Main adapted from the following StackOverflow post:
https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

File deals with basic app set up and management
"""
import tkinter as tk
from model_page import ModelPage
from start_page import StartPage
from about_us_page import AboutUsPage

# z library
# b/ok.cc
# umn libraries

WINDOW_SIZE = "1366x768"
ICON_FILE = 'vibrio icon_rounded.ico'


class Main(tk.Tk):
    """A class for managing the different windows of the app and for handling basic setup of the app"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # main window set up
        self.geometry(WINDOW_SIZE)                # set initial window size
        self.title("Vibr.IO")                     # set window title
        self.iconbitmap(ICON_FILE)                # set icon for app

        container = tk.Frame(self)  # container frame will hold all possible frames of app
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        container.pack()

        self.frames = {}  # define a dictionary of frames in the app

        pages = (ModelPage, StartPage, AboutUsPage)
        # Create a frame for each of the classes
        for F in pages:
            page_name = F.__name__  # string name of class is F.__name__
            frame = F(container, self)  # parent of frame is container. Pass in self to allow frame to use Main's funcs
            frame.grid(row=0, column=0, sticky="nsew")  # stack all of the frames on top of each other
            self.frames[page_name] = frame  # assign to dictionary for easy access later

        self.show_frame("StartPage")  # Show the start page first

    def show_frame(self, page_name):
        """Displays the frame page_name. Used to show the different windows of the apps"""
        frame = self.frames[page_name]  # Get frame from dictionary
        frame.tkraise()  # raise that frame to the top of the stack to show it


if __name__ == "__main__":
    root = Main()
    root.mainloop()
