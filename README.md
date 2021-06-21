# Step7-DatablockPdfReport-to-Json
Transform Simatic step7 Pdf reports to Json format. 

In PLC word only way to get variable names and location in datablock is to look at project file.
This class is made to ease this process, especially if the are 100s of variables in project.

Siemens Step7 provides only PDF exports of datablock, with variable names and adresses.

Instantiate class with path to PDF reports folder, and class will take all pdf file whitin folder to create 
JSON with variable names and adresses.

This Json data is more practical to feed to programs reading from PLC (with snap7 library for exsample)


markoravnik@gmail.com
