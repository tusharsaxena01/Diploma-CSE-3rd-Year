#Open Notepad using python
import subprocess as sp #subprocess package
#The Program name you wanna open
programName = "notepad.exe" #this case, Notepad
#File Name You Want to open
fileName = "happynumbers.txt" #in this case, happynumbers.txt
#passing the values in form of attributes to the function Popen in the form of a list
sp.Popen([programName, fileName])