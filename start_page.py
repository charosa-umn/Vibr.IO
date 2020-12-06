import tkinter as tk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l1 = tk.Label(self, text="Vibr.IO", font=(None, 32), pady=50)
        l1.pack()

        h = 5
        w = 30

        btn1 = tk.Button(self, text='Growth Model', command=lambda: controller.show_frame("ModelPage"))
        btn1.config(height=h, width=w)
        btn1.pack(pady=50)

        btn2 = tk.Button(self, text='About Us', command=lambda: controller.show_frame("AboutUsPage"))
        btn2.pack(pady=50)
        btn2.config(height=h, width=w)

        btn3 = tk.Button(self, text='Exit', command=lambda: exit())
        btn3.pack(pady=50)
        btn3.config(height=h, width=w)

