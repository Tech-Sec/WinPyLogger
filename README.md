# WinPyLogger
WinPyLogger is a keylogger made in purely python for only for Windows. 

To get started:

First clone WinPyLogger repository, type:\
**git clone https://github.com/Tech-Sec/PyLogger.git**

Then change your directory to WinPyLogger:\
**cd WinPyLogger**

Then type:\
**pip3 install -r requirements.txt**


Enable less secure apps option in your google account settings:\
![](imgs/img_2.JPG)

Next set your frequency of email, Email Address and Password in the [utils.py](utils.py) file, line 6:\
![](imgs/img_1.JPG)

To start the keylogger type:\
**python3 WinPyLogger.py**

It will show you all other commands within it.

If you want to select an icon of your own for your executable, choose 'no' when it asks you and type the path of the image. The image should be in ico format. You can use this website for converting your image to .ico format - [ico converter](https://www.icoconverter.com/)

After the file is generated, it will be saved in the dist folder. You can delete all other extra files and folders such as build and .specs if you don't want them.


**Right now, the keylogger can only be stopped from the target machine. If you have got some way to stop it from the user machine or want to give any suggestions, DM me on [Instagram](https://www.instagram.com/_imad._.1/).**\
To stop the keylogger, open taskmanager on the target machine and stop the exe file.

This can be operated from any OS. But the target machine should be Windows.\
If you are using Linux, use python 3.6

Virus detection report:
![](imgs/virus_scan.JPG)

The antivirus of your target detcts this keylogger ?\
Here are some tips to make it FUD (fully undetectable):\
1. The best tip and most effective way to make our keylogger is adding trash code and changing the code a bit. Change the names of the variables in utils.py file and some trash code, anything such as useless variables add some useless functions etc. Trash code should be atleast 100 lies of code.\
2. Make sure to add an icon to the finel exe file, this too helps in bypassing antiviruses. This function is by default in WinPyLogger.\
3. Change the names of the imports. Eg: instead of saying "import pynput", change it to " import pynput as py" or anything you like. Change your code accordingly.
4. By using all these tips you should be able to successfullY bypass your antivirus.
        
Any problems, open an issue.

# FOR EDUCATIONAL AND PENTESTING PURPOSES ONLY 
# The developer is not resposible for any harm with this
