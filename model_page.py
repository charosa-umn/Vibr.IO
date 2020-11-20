"""
Allows users to enter in input and then creates an embedded graph based on that input

Some possible things to change and work on
-Better layout management
-Make UI easier on the eyes
-Add peak information to the graph or display that time to the user
-Add table in addition to the graph
-Add axes titles to graphs (this wont work with current implementation for some reason)
-Add graph navigation toolbar
-Buttons that's let you switch back to home screen; maybe add exit button to this page as well
"""

import tkinter as tk
from matplotlib.pyplot import Figure
from model_math import get_plot_data, get_peak
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# TODO: Add a button that'll allow people to plot in either OD600 or cell density


class ModelPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.is_od600 = tk.StringVar()  # Will be used to track which radio button is selected
        self.is_od600.set("False")

        self.lbl = tk.Label(self, text="Choose one of the following")
        self.lbl.grid(row=0, column=0)

        self.c_btn = tk.Radiobutton(
            self,
            text="Enter Cell Density in (x10^6 cells)/mL:",
            variable=self.is_od600,
            value="False",
            command=lambda: self.toggle_entry())
        self.c_btn.grid(row=1, column=0)

        self.c_entry = tk.Entry(self)
        self.c_entry.grid(row=1, column=1)

        self.od_btn = tk.Radiobutton(
            self,
            text="Enter Cell Density in OD600:",
            variable=self.is_od600,
            value="True",
            command=lambda: self.toggle_entry())
        self.od_btn.grid(row=2, column=0)

        self.od_entry = tk.Entry(self)
        self.od_entry.grid(row=2, column=1)

        tk.Button(
            self,
            text="Generate graph",
            command=lambda: self.embed_plot()
            ).grid(row=3, column=0)
        self.toggle_entry()  # Need to run this function at least once to disable one of the entries upon app start up

    def toggle_entry(self):
        """A helper function that toggles the input entries on and off depending on which
        radio button is selected. Also clears the contents of the entries once they're disabled"""
        if self.is_od600.get() == "True":
            self.c_entry.delete(0, tk.END)
            self.c_entry.config(state="disabled")

            self.od_entry.config(state="normal")
        else:
            self.od_entry.delete(0, tk.END)
            self.od_entry.config(state="disabled")

            self.c_entry.config(state="normal")

    # TODO: Check to ensure that input is a float
    # TODO: is y axis always in od600?
    def embed_plot(self):
        if self.is_od600.get() == "True":
            yo = float(self.od_entry.get())
            t, y = get_plot_data(yo, True)
        else:
            yo = float(self.c_entry.get())
            t, y = get_plot_data(yo, False)

        peak = get_peak(y)

        fig = Figure(figsize=(5, 5), dpi=100)
        plot = fig.add_subplot(111)

        plot.plot(t, y)
        plot.set_title('Cell Density vs Time')
        # plot.xlabel('Time (hrs)')
        # plot.ylabel('Density (OD600)')

        canvas = FigureCanvasTkAgg(fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=5, column=5)


