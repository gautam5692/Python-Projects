# Python Projects

This repository contains various python projects

# Author:
Gautam Chauhan

# Projects List

- Project 1: This project is a snake, water, gun game in which snake defeats water, water defeats gun and gun defeats snake.

- Project 1 again: This project is also same as project 1 which is snake, water, gun game but I created it because I had not touched coding for a few days after learning python and creating the project 1.

- Project 1 GUI version: This project is a snake, water, gun game in GUI (Graphical User Interface) version.

- Project 2: This project is "Guess the number" game in which a random number is generated using random module within a range of 0 to 100 you have to the number until you guess the correct number. It also shows the number of attempts taken to guess the correct number.

- Mega_Project_1 - Jarvis: This project is a personal assistant named Jarvis created using various modules and google gemini api for AI integration. This assistant can open applications or web applications on speech input and also we can ask it for any information which it will response using the google gemini ai.
This mega project has four python files:
1. main.py: Run this program if you want speech input
2. no_speech.py: Run this program if you want text input
3. no_speech_GUI.py: Run this program if you want to use it with GUI
4. apps.py: On running this file, nothing will happen because it only contains the common file locations of apps so that if you tell your assistant to open an app in computer, it can find the location of your app and open it. You can add more apps and their locations to access those apps

- Note:- while opening app with text input, you have to write:
```bash
Your input here: open application appname
```
without the keyword "open application", you won't be able to open the app

# How to run these projects

# Projects without requirements.txt file

- Step 1:
Ensure that you have python installed. If not installed, install python first

- Step 2:
Open Terminal or command prompt and navigate to the project folder. Example:-
```bash
D:\Projects\my_python_project
```

- Step 3:
Run the following command:-
```bash
python file.py
```


# Projects with requirements.txt file

- Step 1:
Ensure that you have python installed. If not installed, install python first

- Step 2:
Open Terminal or command prompt and navigate to the project folder. Example:-
```bash
D:\Projects\my_python_project
```

- Step 3:
Install virtual environment (recommended but not necessary):-
```bash
pip install virtualenv
```

- Step 4:
Create a virtual environment:-
```bash
virtualenv myprojectenv
```

- Step 5:
Activate your virtual environment:
```bash
./myprojectenv/Scripts/activate.ps1
```

- Note:- If you want to install all the packages in your system and not in any virtual environment then you can skip step 3, step 4 and step 5 and move to step 6

- Step 6:
Install all the required packages to run the python program:
```bash
pip install -r requirements.txt
```

- Step 7:
After the installation of required packages, move to the next step

- Step 3:
Run the following command:-
```bash
python file.py
```