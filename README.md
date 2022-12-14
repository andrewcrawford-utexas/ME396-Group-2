# ME396 Group 2: The PesSIMists' Final Project:

## Goal:

The goal of this project is to make a custom static optimization framework using the OpenSim Python API that will allow us to estimate muscle forces from experimental muscle data and then visualize the results in an interactive app make with TKinter. To learn more check out our presentation(you have to be logged in with a UT account to access):

[Google Slides
](https://docs.google.com/presentation/d/1001nQLlKApqGVK3FBlL6m0zl2NVXI9csGdyS3ltmNaE/edit?usp=sharing)

To access the custom static optimization code go to our GoogleColab at:

[Google Colab Code](https://colab.research.google.com/drive/1sTfZjfxMwOXnfKJiklIjZ2WANvQyiTAx?usp=sharing)

### How to Use This Code
#### Static Optimization
You must first manually run the first two blocks of code to set up the environment in the correct format. This code was written in Google Colab so that you can use the OpenSim package without having to download lots of software and check dependencies in your personal environment, but this means the first time you run this code these packages will take time to install (5+ minutes). Once that is complete, then you can run the rest of the code and the custom static optimization. In this code are setup files that can be found in the Gait10dof18musc folder in the github.

The output of this code is then pushed to a Google Drive folder (pushing it straight to the Github required open passwords and was a security risk). If the folder is not created already, it will be created for you.
[Static Optimization Output](https://drive.google.com/file/d/1--L0b-tM9QQMzow9YPXU55FJUQUOtLuw/view?usp=sharing)

We then transferred the output from Google Drive to this github repo that our second part of the code will read. 

#### TKinter Visualizer App
Once the GoogleColab is run take the output file folder and run the visualizer code to see the outputs.

The output from the custom static optimizaton is then fed into the Tkinter Visualizer App that can be found in the files:

FinalProject_TkInter_NotepadInput.py

FinalProject_TkInter_CSVInput.py

The notepad input parses an output from OpenSim whereas the CSVInput pulls the CSV file for the github into a Pandas dataframe. The notepad input is great for use looking at full output files from OpenSim with the CSVinput being preferred for quickly updating the data. 

To utilize our code, make sure to install all the necessary packages, download front_small.png, download back_small.png, download ExampleStaticOPtimizationOutput.sto and then run the code. The code will create a TKinter Gui that can be used to visualize the outputfrom the custom static optimization. 
