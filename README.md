[![MIT License](https://img.shields.io/badge/License-MIT-red.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://choosealicense.com/licenses)
![Cyber Security](https://img.shields.io/badge/Cyber%20Security-yellow)
![Ethical Hacking](https://img.shields.io/badge/Ethical%20Hacking-lightblue)

# Pythonious
This repository is meant to be an agglomeration of python scripts with many different uses.
As of this current commit the project contains 3 scripts, the main PythoniousMain.py script and 2 others in the cibersecurity folder, each of these will be further explained bellow.

# Layout
- [PythoniousMain.py](#pythoniousmainpy)
- [CyberSecurity Folder](#cybersecurity-folder)
  - [Hasher.py](#hasherpy)
  - [HashMatcher.py](#hashmatcherpy)


## PythoniousMain.py
- This script acts as hub for all the scripts inside the project. All it does is run a recursive search on the folder where it's stored with the objective of finding all .py files, it then stores them in a dictionary so they can be easily indicated and selected when running the program.
- When running the program the user is prompted to input the number of one of the found scripts, doing so will run the script in a new console window allowing the user to have multiple scripts running side by side.
  
## Cybersecurity Folder
**Any and all scripts found inside this folder are strictly meant to be used for learning purposes or for ethical hacking. They were built with the purpose of furthering my knowledge of cybersecurity and letting curious minds learn as well.**

### Hasher.py
- This simple script turns any text input into it's matching hash value by passing it through one of the following algorithms:
    - MD5
    - SHA1
    - SHA256
    - SHA512
    - BLAKE2b
    - BLAKE2s
    - SHA3-256
    - SHA3-512
- It's main purpose is to be used in conjunction with the [HashMatcher.py](#hashmatcherpy) by generating a hash value that can be used for testing.
- Bellow is an exemple of the result from the plaintext `"H4sh"` being passed through the MD5 algorithm returning the hash value of:
  - Hash = 469c42850914d6f323656ece681749ce
  
<div align="center">
 <img src="https://github.com/user-attachments/assets/65d78b54-ebd5-4da8-ad45-904124333ea0" alt="HasherImg" height="300"/>
</div>

### HashMatcher.py
- **This script is meant only to be used for learning purposes and nothing else.**
- When executing the script it will first request a hash value that it will try to match, to generate one make use of the [Hasher.py](#hasherpy) script.
- It will then look at the length of the hash value and sugest the algorithms who output hash values of the same length, the user can then choose to run all of the sugestions one by one, select just one or even manually select another algorithm to understand the resulting diferences between them.
- The user will then be prompt to insert the number of characters that the plaintext string contained, if no number is input it will default to 10 characters. If a number of characters is manullay inputted then the matcher will only experiment with plaintext of the same length as indicated, but if nothing is inputted and the `brute_force` function is ran with the default 10 characters the script will go through and test plaintext with various lengths `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> 10` going through them one by one.
- Following this the user will have the option of selecting what character set to run which makes the process faster when testing the script by just selecting the `"1.Numbers"` option for exemple.
- Finally the user will get prompted to select a number of threads to run the script with, however even thought the default is set to 4 the option of `"1. Single"` proved to be the fastest as every `brute_force` call will send multiple values to different variables to have them display the attempts in the console in real time making the use of threads not recomended for the purpose of speed but more so for proof of concept.
- Bellow is the demonstration of how long it took to find the matching hash value to the plaintext `"H4sh"` while running the script on only 1 thread and the specs of my CPU used to test it:
  - **CPU**:   
    - **Current Clock Speed:** 2592 MHz
    - **Max Clock Speed:** 2592 MHz
    - **Name:** Intel(R) Core(TM) i7-10750H CPU @ 2.60GHz
    - **Number of Cores:** 6
    - **Number of Logical Processors:** 12
    
  - **Total Time**:
    - **671.94s** or **671940 ms** or **11m 12s**
    
  - **Number of Attempts**:
    - **10,265,234** (or **15.3 attempts/ms**)
  
<div align="center">
  <img src="https://github.com/user-attachments/assets/002c0d95-5c6f-46c2-b2ee-1bd93783e2d6" alt="HashMatcherImg01" height="600"/>
  <img src="https://github.com/user-attachments/assets/11c2a591-4c03-4968-ae92-ff2fbc95a7ac" alt="HashMatcherImg02"/>
</div>
