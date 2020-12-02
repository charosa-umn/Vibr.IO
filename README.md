# BioLumenModeling
Cell growth modeling of Vibrio fischeri, developed by Charosa Research Incubator, a student group at the University of Minnesota - Twin Cities

## Notable Changes
    * "math_model.py" was renamed to "math_model_cmd.py"
    * "my_math_model.py" was renamed to "math_model.py"
    * Can now switch between pages
    * Added start_page.py and main.py to the repository
    
    math_model_cmd.py will refer to the command line interface for modeling Vibrio fischeri growth and math_model.py will
    be a math plotting module used by the other files in the project. 

## File Guide 
### main.py
Run this file to run the application. This'll be the main file that ties all of the other files together.

### start_page.py
Code for the start page of the application.

### model_page.py
Code for the page that allows you to model Vibrio fischeri growth.

### math_model.py
A helper module that model_page uses to help model growth. Basically, all of the math is computed in this file.

### math_model_cmd.py
A commandline interface that allows you to plot Vibrio fischeri growth.



