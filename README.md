# Vibr.IO
Vibr.IO is a program to model cell growth of Vibrio fischeri, developed by Charosa Research Incubator, a student group at the University of Minnesota - Twin Cities. 
Below are installation instructions as well as specific capabilities of the application.

## Installion and Use
The application can be used by downloading the release [here.](google.com) Once downloaded, simply double clicking the excutable file named "vibr.IO.exe" will start up the application. You can create a desktop shortcut by right-clicking and selecting "create shortcut" if desired.

Supported platforms are Windows...?

## Program Capabilities 
Vibr.IO offers a clean and easy-to-use UI for modeling vibrio fischeri growth. Users can specify the cell concentration as either a measure of od600 or x10^6 cells/mL and also allows graphs to be displayed in either unit of measure. Users can also specify the duration of the simulation in hours and can customize the time increment of the model. In addition to modeling cell growth, there is also an additional plot on the right that models the decrease in substrate over time.
![](https://user-images.githubusercontent.com/46146906/101276862-91b21300-3775-11eb-86bf-dba46f17403f.png)


In addition to modeling cell growth and substrate reduction, the vibrio fischeri growth plot also labels the peak with a red indicator and provides users with the predicted peak time and peak cell amount. Each peak is also followed by an estimated death curve to give users an indication of the rate of death as well. The application also allows users to take advantage of some of the convenient features of matplotlib such as saving figures, zooming into figures, panning, etc. These capabilities are made viable using the horizontal toolbar beneath the two plots.
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
A thanks to Y. Luna Lin from Hardvard for Vibrio Fischeri modeling advice.

## Contact
For any direct questions or comments, email charosa@umn.edu.

