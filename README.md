# Python Projects

This repository contains various Python projects created by Gautam Chauhan.

---

## 📌 Author

**Gautam Chauhan**

---

## 🗂️ Projects List

- **Project 1 – Snake, Water, Gun (CLI Version)**  
  A classic game where:
  - Snake drinks water 🐍 > 💧
  - Water damages gun 💧 > 🔫
  - Gun kills snake 🔫 > 🐍

- **Project 1 Again**  
  A repeat of Project 1 created to refresh coding skills after a short break.

- **Project 1 – GUI Version**  
  The Snake, Water, Gun game with a graphical user interface (GUI) built using Python.

- **Project 2 – Guess the Number**  
  A game where a random number is generated between 0 and 100. The player keeps guessing until the correct number is found. The total number of attempts is displayed.

- **Mega Project 1 – Jarvis Personal Assistant**  
  A voice- and text-based personal assistant using Python and the Google Gemini AI API. It can open desktop apps, perform web searches, and respond to queries.

  This project has four files:
  1. `main.py` – Run this for **speech input**
  2. `no_speech.py` – Use for **text input**
  3. `no_speech_GUI.py` – Use for **GUI with text input**
  4. `apps.py` – Contains file paths of installed apps. You can customize it to support more apps.

  **Note:** To open apps using text input, type:
  ```bash
  Your input here: open application appname
  ```
  Without the keyword "open application", you won't be able to open the app

# How to Run These Projects

## Projects Without `requirements.txt` File

  - **Step 1:**
    Ensure that you have python installed. If not installed, install python first

  - **Step 2:**
    Open Terminal or command prompt and navigate to the project folder. Example:-
    ```bash
    D:\Projects\my_python_project
    ```

  - **Step 3:**
    Run the following command:-
    ```bash
    python file.py
    ```


## Projects With `requirements.txt` File

  - **Step 1:**
    Ensure that you have python installed. If not installed, install python first

  - **Step 2:**
    Open Terminal or command prompt and navigate to the project folder. Example:-
    ```bash
    D:\Projects\my_python_project
    ```

  - **Step 3:**
    Install virtual environment (recommended but not necessary):-
    ```bash
    pip install virtualenv
    ```

  - **Step 4:**
    Create a virtual environment:-
    ```bash
    virtualenv myprojectenv
    ```

  - **Step 5:**
    Activate your virtual environment:
    ```bash
    ./myprojectenv/Scripts/activate.ps1
    ```

  - Note:- If you want to install all the packages in your system and not in any virtual environment then you can skip step 3, step 4 and step 5 and move to step 6

  - **Step 6:**
    Install all the required packages to run the python program:
    ```bash
    pip install -r requirements.txt
    ```

  - **Step 7:**
    After the installation of required packages, move to the next step

  - **Step 8:**
    Run the following command:-
    ```bash
    python file.py
    ```