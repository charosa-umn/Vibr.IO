import tkinter as tk


class AboutUsPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        l1 = tk.Label(self, text="About Vibr.IO", font=(None, 28), pady=20)
        l1.pack()

        l2 = tk.Label(self,
                      text="Vibr.IO is developed by Charosa Research Incubator, a student group at the University of Minnesota - Twin Cities.",
                      font=(None, 14), pady=10)
        l2.pack()

        t1 = tk.Label(self, text="Contributors", font=(None, 20), pady=0)
        t1.pack()

        l3 = tk.Label(self, text="David Wang\n Alessandro Snyder\n Gaurav Behera", font=(None, 14), pady=10)
        l3.pack()

        t2 = tk.Label(self, text="Model Approximations", font=(None, 20), pady=0)
        t2.pack()

        l4 = tk.Label(self,
                      text="The model represents cell growth in culture as a batch process described by Monod growth kinetics. For the model, NaCl was considered the limiting substrate for cell growth. The growth constants umax, Ks, and Yxs were fit from experimental data of Vibrio fischeri growth in medium containing yeast extract, tryptone, and NaCl (Castillo-Gomez et al. 2019). The fit values were: umax = 0.43 hr\u207b\u00b9, Ks = 1.2 g/L, Yxs = 1.21. Peak cell density was approximated as the point where the cell population grew by less than 0.01% versus the previous timestep.\n Cell death was approximated by first-order kinetics, with a death constant of Kd = 0.43 hr\u207b\u00b9. This value from the literature describes the death rate of E. coli in culture, and was used as a first approximation to estimate the death rate of V. fischeri (Schink et al. 2019).",
                      font=(None, 14), wraplength=1000, pady=10)
        l4.pack()

        t3 = tk.Label(self, text="Acknowledgements", font=(None, 20), pady=0)
        t3.pack()

        l5 = tk.Label(self, text="Thank you to Y. Luna Lin, for the Vibrio fischeri modeling advice.", font=(None, 14),
                      pady=10)
        l5.pack()

        btn1 = tk.Button(self, text='Back', command=lambda: controller.show_frame("StartPage"))
        btn1.config(height=3, width=20)
        btn1.pack(pady=30)