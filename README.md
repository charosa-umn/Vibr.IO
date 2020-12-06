# Vibr.IO
Vibr.IO is an open-source program to model the cell growth of *Vibrio fischeri* in culture, developed by Charosa Research Incubator, a student group at the University of Minnesota - Twin Cities. 
Read on for installation instructions as well as specific capabilities of the application.

## Installation and Use
Download the latest release of **Vibr.IO** [here.](google.com) Once downloaded, extract the .zip file and double-click the excutable file "Vibr.IO.exe" to start-up the application. You can create a desktop shortcut by right-clicking and selecting "create shortcut" if desired.

Supported platforms are Windows...?

## Program Capabilities 
**Vibr.IO** offers a clean and easy-to-use UI for modeling cell growth of Vibrio fischeri. Users can specify the initial cell concentration in either OD600 or (x10^6 cells)/mL. The program allows graphs to be displayed in either unit of measure. Users can also specify the simulation duration in hours and can customize the time increment of the model. In addition to modeling cell growth over time, there is also a supplemental plot on the right which models the change in substrate over time.
![](https://user-images.githubusercontent.com/46146906/101276862-91b21300-3775-11eb-86bf-dba46f17403f.png)


In addition to modeling cell growth and substrate change with time, the cell growth plot also labels the point of peak cell density with a red indicator and provides users with the predicted peak time and peak cell density. Each peak is followed by an estimated death curve to provide users an indication of the rate of cell death. **Vibr.IO** also allows users to take advantage of convenient features from **matplotlib**, such as saving figures, zooming into figures, panning, etc. These capabilities are accessible from the horizontal toolbar beneath the two plots.
![](https://user-images.githubusercontent.com/46146906/101277025-fb7eec80-3776-11eb-8b76-bf369e0174b9.png)

## Model Theory
The model represents cell growth in culture as a batch process described by Monod growth kinetics. For the model, NaCl was considered the limiting substrate for cell growth. The growth constants umax, Ks, and Yxs were fit from experimental data of *Vibrio fischeri* growth in medium containing yeast extract, tryptone, and NaCl (**Castillo-Gomez et al. 2019**). The fit values were: **umax** = 0.43 hr^-1, **Ks** = 1.2 g/L, **Yxs** = 1.21. 

Peak cell density was approximated as the point where the cell population grew by less than 0.01% versus the previous timestep. 

Cell death was approximated by first-order kinetics, with a death constant of **Kd** = 0.43 hr^-1. This value from the literature describes the death rate of *E. coli* in culture, and was used as a first approximation to estimate the death rate of *V. fischeri* (**Schink et al. 2019**).

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
Thank you to Y. Luna Lin of Harvard University for their *Vibrio fischeri* modeling advice.

## Contact
For any direct questions or comments, email charosa@umn.edu.

