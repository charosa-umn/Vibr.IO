"""
Alessandro Snyder
Allows users to enter in input and then creates an embedded graph based on that input

Some possible things to change and work on
-Better layout management
-Make UI easier on the eyes
-Add peak information to the graph or display that time to the user
-Add axes titles to graphs (this wont work with current implementation for some reason)
-Add graph navigation toolbar
-Buttons that let you switch between the different pages
-A constructor and class for this UI window; implementing this
will make it easier to use with the other code
"""

import tkinter as tk
from matplotlib.pyplot import Figure
from my_math_model import get_plot_data, get_peak
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
W = 600  # width in pixels
H = 400  # height in pixels


def toggle_entry():
    """A helper function that toggles the input entries on and off depending on which
    radio button is selected. Also clears the contents of the entries once they're disabled"""
    if is_od600.get() == "True":
        c_entry.delete(0, tk.END)
        c_entry.config(state="disabled")

        od_entry.config(state="normal")
    else:
        od_entry.delete(0, tk.END)
        od_entry.config(state="disabled")

        c_entry.config(state="normal")


# TODO: Check to ensure that input is a float
# TODO: is y axis always in od600?
def embed_plot():
    if is_od600.get() == "True":
        yo = float(od_entry.get())
        t, y = get_plot_data(yo, True)
    else:
        yo = float(c_entry.get())
        t, y = get_plot_data(yo, False)

    peak = get_peak(y)

    fig = Figure(figsize=(5, 5), dpi=100)
    plot = fig.add_subplot(111)

    plot.plot(t, y)
    plot.set_title('Cell Density vs Time')
    # plot.xlabel('Time (hrs)')
    # plot.ylabel('Density (OD600)')

    canvas = FigureCanvasTkAgg(fig, master=master)
    canvas.draw()
    canvas.get_tk_widget().pack()


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cell Model")

    is_od600 = tk.StringVar()  # Will be used to track which radio button is selected
    is_od600.set("False")

    window = tk.Canvas(root, height=H, width=W)
    window.pack()

    master = tk.Frame(root)
    master.place(relheight=1, relwidth=1)

    input_frame = tk.Frame(master)
    input_frame.pack()

    lbl = tk.Label(input_frame, text="Choose one of the following")
    lbl.grid(row=0, column=0)

    c_btn = tk.Radiobutton(
        input_frame,
        text="Enter Cell Density in (x10^6 cells)/mL:",
        variable=is_od600,
        value="False",
        command=lambda: toggle_entry())
    c_btn.grid(row=1, column=0)

    c_entry = tk.Entry(input_frame)
    c_entry.grid(row=1, column=1)

    od_btn = tk.Radiobutton(
        input_frame,
        text="Enter Cell Density in OD600:",
        variable=is_od600,
        value="True",
        command=lambda: toggle_entry())
    od_btn.grid(row=2, column=0)

    od_entry = tk.Entry(input_frame)
    od_entry.grid(row=2, column=1)

    tk.Button(
        input_frame,
        text="Generate graph",
        command=lambda: embed_plot()
        ).grid(row=3, column=0)
    toggle_entry()  # Need to run this function at least once to disable one of the entries upon app start up

    root.mainloop()


