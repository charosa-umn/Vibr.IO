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
-Add peak to graph
-Have an option to export table in csv
-
"""

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
# from matplotlib.pyplot import Figure
from model_math import solve
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# TODO: Add a button that'll allow people to plot in either OD600 or cell density
MIN_SIM_TIME = 5    # Minimum possible duration of simulation
MAX_SIM_TIME = 120  # Maximum possible duration of simulation

MIN_INT_TIME = 1    # Minimum increment time
MAX_INT_TIME = 10   # Maximum increment time


class ModelPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.is_od600 = tk.StringVar()  # Will be used to track which radio button is selected
        self.is_od600.set("False")

        # model page will be divided into these different frames
        self.input_frame = tk.Frame(self, height=400)  # frame for input part of window
        self.plot_frame = tk.Frame(self, width=100, height=400)  # frame to display the plots
        self.input_frame.grid(row=0, column=0, padx=(0, 0))  # Add a bit of padding to the right
        self.plot_frame.grid(row=0, column=1)

        # Create and add a separator for the input frame
        sep = ttk.Separator(self.input_frame, orient=tk.VERTICAL)
        sep.grid(rowspan=10, column=3, sticky="ns", ipady=330)

        # Begin adding widgets to input frame to construct the input part of the window
        # ENTER CELL CONCENTRATION
        self.lbl = tk.Label(self.input_frame, text="Choose one of the following")
        self.lbl.grid(row=0, column=0)

        self.c_btn = tk.Radiobutton(
            self.input_frame,
            text="Enter Cell Density in (x10^6 cells)/mL:",
            variable=self.is_od600,
            value="False",
            command=lambda: self.toggle_entry())
        self.c_btn.grid(row=1, column=0)

        self.c_entry = tk.Entry(self.input_frame)
        self.c_entry.grid(row=1, column=1)

        self.od_btn = tk.Radiobutton(
            self.input_frame,
            text="Enter Cell Density in OD600:",
            variable=self.is_od600,
            value="True",
            command=lambda: self.toggle_entry())
        self.od_btn.grid(row=2, column=0)

        self.od_entry = tk.Entry(self.input_frame)
        self.od_entry.grid(row=2, column=1)

        # ENTER SUBSTRATE
        tk.Label(self.input_frame, text="Enter substrate (NaCl) in grams:").grid(row=3, column=0)
        self.substrate_entry = tk.Entry(self.input_frame)
        self.substrate_entry.grid(row=3, column=1)

        # TIMING COMBOBOX
        tk.Label(self.input_frame, text="Run the simulation for").grid(row=4, column=0)
        self.time_combo = ttk.Combobox(self.input_frame, state='readonly')

        times = []
        for i in range(MIN_SIM_TIME, MAX_SIM_TIME+1):
            times.append(i)

        self.time_combo["values"] = times
        self.time_combo.grid(row=4, column=1)
        self.time_combo.set(28)

        tk.Label(self.input_frame, text="hours").grid(row=4, column=2)

        # TIMING INTERVAL
        tk.Label(self.input_frame, text="Time increment:").grid(row=5, column=0)
        self.interval_combo = ttk.Combobox(self.input_frame, state='readonly')

        times = []
        for i in range(MIN_INT_TIME, MAX_INT_TIME + 1):
            times.append(i)

        self.interval_combo["values"] = times
        self.interval_combo.grid(row=5, column=1)
        self.interval_combo.set(1)

        tk.Label(self.input_frame, text="hours").grid(row=5, column=2)

        # GENERATE BUTTON
        tk.Button(
            self.input_frame,
            text="Generate graph",
            command=lambda: self.embed_plot()
            ).grid(row=7, column=0)
        self.toggle_entry()  # Need to run this function at least once to disable one of the entries upon app start up

        self.create_plot(None, None)  # Generate an initial empty plot

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
    def create_plot(self, t, psoln):
        """Setting t and psoln as none signifies that an empty plot with no data should be constructed"""
        fig = plt.Figure(figsize=(11.5, 6), dpi=80) # create figure for subplots

        plt1 = fig.add_subplot(121)
        plt1.set_title("Cell Density vs. Time")
        plt1.set_xlabel('Time (hrs)')
        plt1.set_ylabel('X (od600)')

        plt2 = fig.add_subplot(122)
        plt2.set_title("Substrate vs. Time")
        plt2.set_xlabel('Time (hrs)')
        plt2.set_ylabel("Substrate (g)")

        fig.patch.set_facecolor("#F0F0F0")
        fig.subplots_adjust(wspace=0.30)  # Add spacing between plots

        if t is not None:
            plt1.plot(t, psoln[:, 0])
            plt2.plot(t, psoln[:, 1])

        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)

    def embed_plot(self):
        # Grab cell concentration value
        if self.is_od600.get() == "True":
            cell_conc = float(self.od_entry.get())
        else:
            cell_conc = float(self.c_entry.get())

        substrate = float(self.substrate_entry.get())  # Get substrate value
        t_stop = int(self.time_combo.get())
        t_inc = int(self.interval_combo.get())

        t, psoln = solve(cell_conc, substrate, t_stop, t_inc)

        self.create_plot(t, psoln)







