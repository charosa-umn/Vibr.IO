# Vibr.IO
Vibr.IO is an open-source program to model the cell growth of *Vibrio fischeri* in culture, developed by Charosa Research Incubator, a student group at the University of Minnesota - Twin Cities. 
Both Windows and macOS are supported.
Read on for installation instructions as well as specific capabilities of the application.

## Build from Source (PyInstaller)
Download the source code from the latest **[release](https://github.com/charosa-umn/Vibr.IO/archive/1.0.0.zip)**. Ensure that the required dependences are installed to your local Python installation (see **Built With** section).
### Build on Windows
From the command line, navigate to the source code folder and run the following command: 

`pyinstaller --windowed --icon="vibrio_icon_rounded.ico" --add-data vibrio_icon_rounded.ico;. main.py`

Then open **main.exe** from the generated **/dist** folder in the source code directory.

### Build on macOS
From the command line, navigate to the source code folder and run the following command: 

`pyinstaller --windowed --icon="vibrio_icon_rounded.icns" --add-data vibrio_icon_rounded.icns:. main.py`

Then open **main.app** from the generated **/dist** folder in the source code directory.

## Install
### Install on Windows
Download **[Vibr.IO_Windows_v1.0.0.zip](https://github.com/charosa-umn/Vibr.IO/releases/download/1.0.0/Vibr.IO_Windows_v1.0.0.zip)**, unzip the directory, and open **Vibr.IO.exe** to run the application. You can create a desktop shortcut by right-clicking and selecting "create shortcut" if desired.

### Install on macOS
Download **[Vibr.IO_macOS_v1.0.0.zip](https://github.com/charosa-umn/Vibr.IO/releases/download/1.0.0/Vibr.IO_macOS_v1.0.0.zip)**, unzip the directory, and open **Vibr.IO.app** to run the application.


## Program Capabilities 
**Vibr.IO** offers a clean and easy-to-use UI for modeling cell growth of Vibrio fischeri. Users can specify the initial cell concentration in either OD600 or (x10^6 cells)/mL. The program allows graphs to be displayed in either unit of measure. Users can also specify the simulation duration in hours and can customize the time increment of the model. In addition to modeling cell growth over time, there is also a supplemental plot on the right which models the change in substrate over time.
![](https://user-images.githubusercontent.com/46146906/101292658-8ba04e80-37d6-11eb-99b8-863fcb0af43f.png)


In addition to modeling cell growth and substrate change with time, the cell growth plot also labels the point of peak cell density with a red indicator and provides users with the predicted peak time and peak cell density. Each peak is followed by an estimated death curve to provide users an indication of the rate of cell death. **Vibr.IO** also allows users to take advantage of convenient features from **matplotlib**, such as saving figures, zooming into figures, panning, etc. These capabilities are accessible from the horizontal toolbar beneath the two plots.
![](https://user-images.githubusercontent.com/46146906/101292660-8d6a1200-37d6-11eb-8d06-7658b328d384.png)

## Model Theory
The model represents cell growth in culture as a batch process described by Monod growth kinetics. For the model, NaCl was considered the limiting substrate for cell growth. The growth constants umax, Ks, and Yxs were fit from experimental data of *Vibrio fischeri* growth in medium containing yeast extract, tryptone, and NaCl ([**Castillo-Gomez et al. 2019**](https://doi.org/10.1002/bio.3683)). The fit values were: **umax** = 0.43 hr^-1, **Ks** = 1.2 g/L, **Yxs** = 1.21. 

Peak cell density was approximated as the point where the cell population grew by less than 0.01% versus the previous timestep. 

Cell death was approximated by first-order kinetics, with a death constant of **Kd** = 0.43 hr^-1. This value from the literature describes the death rate of *E. coli* in culture, and was used as a first approximation to estimate the death rate of *V. fischeri* ([**Schink et al. 2019**](https://doi.org/10.1016/j.cels.2019.06.003)).

## Built With
* [Python 3](https://www.python.org/downloads/) - The primary programming language used
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - The GUI framework used
* [NumPy](https://numpy.org/) - Used to aide in model computation
* [Matplotlib](https://matplotlib.org/) - Used for plotting and displaying cell growth 
* [Scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html) - Used for model ODE integration
* [PyInstaller](https://pypi.org/project/PyInstaller/)  - Used to package the code as an executable 

## Contributors
* David Wang
* Alessandro Snyder
* Gaurav Behera 

## Acknowledgements
Thank you to [Y. Luna Lin](https://ylunalin.com/) of Harvard University for their *Vibrio fischeri* modeling advice.

## Contact
For any direct questions or comments, email charosa@umn.edu.

