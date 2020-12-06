"""
Main modeling page of the app.
"""
# TODO Make font bigger

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from model_math import generate_growth, convert_cell_density, generate_peak, generate_death
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

MIN_SIM_TIME = 5    # Minimum possible duration of simulation in hours
MAX_SIM_TIME = 120  # Maximum possible duration of simulation in hours

MIN_INT_TIME = 1  # Minimum increment time in hours
MAX_INT_TIME = 10   # Maximum increment time in hours
STEP = 0.5          # Start at MIN_INT_TIME and increment by STEP until MAX_INT_TIME (hours)

SPACING_BETWEEN_WIDGETS = (0, 10)
SPACING_BETWEEN_GROUPS = (0, 30)  # Spacing between widget groups under the input frame

od600 = 'OD\u2086\u2080\u2080'

class ModelPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller    # Set the controller

        """Model page will be divided into these frames"""
        self.input_frame = tk.Frame(self, height=400)            # frame for input panel
        self.plot_frame = tk.Frame(self, width=100, height=400)  # frame to display plots and plot info

        self.input_frame.grid(row=0, column=0)
        self.plot_frame.grid(row=0, column=1)

        """Create a separator that separates input panel and graph display"""
        sep = ttk.Separator(self.input_frame, orient=tk.VERTICAL)
        sep.grid(rowspan=50, column=3, sticky="ns")  # ipady = 330

        ttk.Separator(self.input_frame, orient=tk.HORIZONTAL).grid(column=0, columnspan=3, row=0, sticky='ew')

        """BEGIN ADDING WIDGETS TO INPUT FRAME"""

        """Cell Concentration Group"""
        self.is_od600 = tk.StringVar()  # Will be used to track which radio button is selected below
        self.is_od600.set("True")      # Initialize to false
        tk.Label(
            self.input_frame,
            text="Enter in Cell Density",
            font=("Helvetica", 12, "bold")
        ).grid(row=1, column=0, sticky="w")

        self.c_btn = tk.Radiobutton(
            self.input_frame,
            text="Enter cell density in (x10\u2076 cells)/mL:",
            variable=self.is_od600,
            value="False",
            command=lambda: self.toggle_entry())
        self.c_btn.grid(row=2, column=0, sticky="w")

        self.c_entry = tk.Entry(self.input_frame)
        self.c_entry.grid(row=2, column=1)

        self.od_btn = tk.Radiobutton(
            self.input_frame,
            text=f"Enter cell density in {od600}:",
            variable=self.is_od600,
            value="True",
            command=lambda: self.toggle_entry())
        self.od_btn.grid(row=3, column=0, sticky="w", pady=SPACING_BETWEEN_GROUPS)

        self.od_entry = tk.Entry(self.input_frame)
        self.od_entry.grid(row=3, column=1, pady=SPACING_BETWEEN_GROUPS)

        """Substrate Group"""
        tk.Label(
            self.input_frame,
            text="Enter in Substrate",
            font=("Helvetica", 12, "bold")
        ).grid(row=4, column=0, sticky="w")
        tk.Label(self.input_frame, text="Enter substrate (NaCl) in grams:").grid(row=5, column=0, sticky="w", pady=SPACING_BETWEEN_GROUPS)
        self.substrate_entry = tk.Entry(self.input_frame)
        self.substrate_entry.grid(row=5, column=1, pady=SPACING_BETWEEN_GROUPS)

        """Timing Combobox Group"""
        tk.Label(
            self.input_frame,
            text="Enter in Time",
            font=("Helvetica", 12, "bold")
        ).grid(row=6, column=0, sticky="w")
        tk.Label(self.input_frame, text="Duration in hours:").grid(row=7, column=0, sticky="w")
        self.time_combo = ttk.Combobox(self.input_frame, state='readonly')

        times = []  # Generate times for the combo box
        for i in range(MIN_SIM_TIME, MAX_SIM_TIME+1):
            times.append(i)

        self.time_combo["values"] = times
        self.time_combo.grid(row=7, column=1)
        self.time_combo.set(28)  # set default to 28 hours

        """Timing Interval Group"""
        tk.Label(self.input_frame, text="Time increment in hours:").grid(row=8, column=0, sticky="w", pady=SPACING_BETWEEN_GROUPS)
        self.interval_combo = ttk.Combobox(self.input_frame, state='readonly')  # set to readonly so people can't change input

        times = []
        num_times = int(MAX_INT_TIME / MIN_INT_TIME)  # generate times for combobox
        cur = MIN_INT_TIME
        times.append(cur)
        for i in range(0, num_times):
            cur = cur + STEP
            times.append(cur)

        self.interval_combo["values"] = times
        self.interval_combo.grid(row=8, column=1, pady=SPACING_BETWEEN_GROUPS)
        self.interval_combo.set(MIN_INT_TIME)  # set default to MIN_INT_TIME

        "Graph Units Group"
        self.graph_units_is_od600 = tk.StringVar()  # Used to determine which radio button is elected below
        self.graph_units_is_od600.set("True")      # Init to false

        tk.Label(self.input_frame, text="Graph Units", font=("Helvetica", 12, "bold")).grid(row=9, column=0, sticky="w")

        tk.Radiobutton(
            self.input_frame,
            text="Plot in nominal cell density",
            variable=self.graph_units_is_od600,
            value="False"
        ).grid(row=10, column=0, sticky="w")

        tk.Radiobutton(
            self.input_frame,
            text=f"Plot in {od600}",
            variable=self.graph_units_is_od600,
            value="True"
        ).grid(row=11, column=0, pady=SPACING_BETWEEN_GROUPS, sticky="w")

        """Generate button"""
        tk.Button(
            self.input_frame,
            text="Generate graph",
            command=lambda: self.generate_graph()
            ).grid(row=12, column=0, columnspan=2, sticky="ew")
        self.toggle_entry()  # Need to run this function at least once to disable one of the entries upon app start up

        """Back and Exit Buttons"""
        tk.Button(
            self.input_frame,
            text="Back",
            command=lambda: controller.show_frame("StartPage"),
            width=20
        ).grid(row=13, column=0, sticky="w")

        tk.Button(
            self.input_frame,
            text="Exit",
            command=lambda: exit(),
            width=20
        ).grid(row=13, column=1, sticky="e")

        ttk.Separator(self.input_frame, orient=tk.HORIZONTAL).grid(row=14, column=0, columnspan=3, sticky='ew')

        """BEGIN SET UP OF GRAPH DISPLAY"""
        self.create_plot()  # Generate an initial empty plot with matplotlib toolbar

        # Create a frame to display information about when the peak occurs
        self.peak_frame = tk.Frame(self.plot_frame)
        self.peak_frame.grid(row=2, column=0)

        tk.Label(self.peak_frame, text="Peak cell density:", font=("Helvetica", 9, "bold")).grid(row=1, column=0)
        self.peak_cells = tk.Label(self.peak_frame, text="")
        self.peak_cells.grid(row=1, column=1)

        tk.Label(self.peak_frame, text="Peak time:", font=("Helvetica", 9, "bold")).grid(row=2, column=0)
        self.peak_t = tk.Label(self.peak_frame, text="")
        self.peak_t.grid(row=2, column=1)

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

    def create_plot(self):
        fig = plt.Figure(figsize=(11.5, 6), dpi=80)  # create figure for subplots

        plt1 = fig.add_subplot(121)  # create subplot for cell density vs time
        plt2 = fig.add_subplot(122)  # create subplot for substrate vs time

        if self.graph_units_is_od600.get() == "True":
            units = f"Cell Density in {od600}"  # change y-axis label if user wants to graph in od600
        else:
            units = "Cell Density in (x10\u2076 cells)/mL"  # y-axis label for first plot

        # Set labels and titles for the two plots
        plt1.set_title("Cell Density vs. Time")
        plt1.set_xlabel('Time (hrs)')
        plt1.set_ylabel(units)

        plt2.set_title("Substrate vs. Time")
        plt2.set_xlabel('Time (hrs)')
        plt2.set_ylabel("Substrate (g)")

        fig.patch.set_facecolor("#F0F0F0")  # set to tkinter window color for aesthetic purposes
        fig.subplots_adjust(wspace=0.30)  # Add spacing between plots for readability

        # create a canvas to store the plots in
        canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
        canvas.draw()

        # Create a frame for the matplotlib toolbar; set it so it's underneath the plots
        toolbar_frame = tk.Frame(self.plot_frame)
        toolbar_frame.grid(row=1, column=0)

        toobar = NavigationToolbar2Tk(canvas, toolbar_frame)  # add matplotlib toolbar to toolbar frame
        canvas.get_tk_widget().grid(row=0, column=0)

        # add info
        # self.peak_lbl = tk.Label(self.toolbar_frame, text="Peak:")

        return plt1, plt2

    def plot_data(self, plt1, plt2, cell_conc, substrate, t_stop, t_inc):
        t, psoln = generate_growth(cell_conc, substrate, t_stop, t_inc)  # grab times and growth data
        cell_data = psoln[:, 0]  # grab cell growth data
        substr_data = psoln[:, 1]  # grab substrate data

        if self.graph_units_is_od600.get() == "False":
            cell_data = list(map(lambda x: convert_cell_density(x, False), cell_data))  # convert data points to nominal cell density if needed

        peak, peak_i, peak_time, t_stop_peak = generate_peak(psoln, t)  # determine index that peak occurs

        # Plot cell growth and decay
        if peak < 0:
            plt1.plot(t, cell_data)  # plot cell growth data up until peak
            self.peak_cells['text'] = "Could not determine a peak."
            self.peak_t['text'] = "Could not determine a peak."
        else:
            psoln_d = generate_death(peak, t_inc, t_stop_peak)  # grab data for cell death

            if self.graph_units_is_od600.get() == "False":
                psoln_d[:, 0] = list(map(lambda x: convert_cell_density(x, False), psoln_d[:, 0]))
                units = "x10\u2076 cells/mL"
            else:
                units = od600

            plt1.plot(t[:peak_i+1], cell_data[:peak_i+1])  # plot cell growth data up until peak
            plt1.plot(t[peak_i], cell_data[peak_i], marker='o', color='red')  # plot peak point
            plt1.plot(t[peak_i:], psoln_d[:, 0], '--k')

            self.peak_cells['text'] = f'{round(cell_data[peak_i], 3)} {units}'
            self.peak_t['text'] = f'{t[peak_i]} hours'

        # Plot substrate decay
        plt2.plot(t, substr_data)

    def generate_graph(self):
        try:
            # Grab cell concentration value
            if self.is_od600.get() == "True":
                cell_conc = float(self.od_entry.get())
            else:
                cell_conc = float(self.c_entry.get())
                cell_conc = convert_cell_density(cell_conc, True)  # calculations are in od600 so do a conversion

            substrate = float(self.substrate_entry.get())  # Get substrate value

            # Raise ValueError if negative numbers or zero are entered
            if substrate <= 0 or cell_conc <= 0:
                raise ValueError

            t_stop = float(self.time_combo.get())
            t_inc = float(self.interval_combo.get())

            plt1, plt2 = self.create_plot()  # create an empty plot
            self.plot_data(plt1, plt2, cell_conc, substrate, t_stop, t_inc)  # plot wanted data given this info

        # Value error = bad input such as strings or negative numbers
        except ValueError as err:
            tk.messagebox.showwarning("Invalid Input Detected:", f"Invalid input.\nPlease enter only positive real numbers.\n Error: {err}\n")
        except Exception as err:
            tk.messagebox.showwarning("Unexpected error", f'Something unexpected happened. Error: {err}')








