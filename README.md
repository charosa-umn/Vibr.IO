# Vibr.IO
Vibr.IO is an open-source program to model the cell growth of *Vibrio fischeri* in culture, developed by Charosa Research Incubator, a student group at the University of Minnesota - Twin Cities. 
Read on for installation instructions as well as specific capabilities of the application.

## Installation and Use
Download the latest release of **Vibr.IO** [here.](google.com) Once downloaded, extract the .zip file and double-click the excutable file "Vibr.IO.exe" to start-up the application. You can create a desktop shortcut by right-clicking and selecting "create shortcut" if desired.

Supported platforms are Windows...?

## Program Capabilities 
**Vibr.IO** offers a clean and easy-to-use UI for modeling cell growth of Vibrio fischeri. Users can specify the initial cell concentration in either OD600 or (x10^6 cells)/mL; **Vibr.IO** allows graphs to be displayed in either unit of measure. Users can also specify the simulation duration in hours and can customize the time increment of the model. In addition to modeling cell growth over time, there is also a supplemental plot on the right which models the change in substrate over time.
![](https://user-images.githubusercontent.com/46146906/101276862-91b21300-3775-11eb-86bf-dba46f17403f.png)


In addition to modeling cell growth and substrate change with time, the cell growth plot also labels the point of peak cell density with a red indicator and provides users with the predicted peak time and peak cell density. Each peak is followed by an estimated death curve to provide users an indication of the rate of cell death. **Vibr.IO** also allows users to take advantage of convenient features from **matplotlib**, such as saving figures, zooming into figures, panning, etc. These capabilities are accessible from the horizontal toolbar beneath the two plots.
![](https://user-images.githubusercontent.com/46146906/101277025-fb7eec80-3776-11eb-8b76-bf369e0174b9.png)

## Model Theory
Model theroy goes heeeeere.

## Built With
* [Python 3](https://www.python.org/downloads/) - The primary programming language used
* [Tkinter](https://docs.python.org/3/library/tkinter.html) - The GUI framework used
* [NumPy](https://numpy.org/)Numpy - Used to aide in computation
* [Matplotlib](https://matplotlib.org/) - Used for plotting and displaying cell growth as graphs in the app
* [Scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html) - Used for mathematical calculations
* [PyInstaller](https://pypi.org/project/PyInstaller/)  - Used to package the code as an executable 

## Contributors
* David Wang
* Alessandro Snyder
* Gaurav Behera 

## Acknowledgements
A thanks to Y. Luna Lin from Harvard for *Vibrio fischeri* modeling advice.

## Contact
For any direct questions or comments, email charosa@umn.edu.

