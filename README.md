[![MIT License](https://img.shields.io/badge/License-MIT-red.svg)](https://choosealicense.com/licenses/mit/)
[![Python](https://img.shields.io/badge/Python-3.12-blue)](https://choosealicense.com/licenses)

# Pythonious
This repository is meant to be an agglomeration of python scripts with many different uses.
As of this current commit the project contains 3 scripts, the main PythoniousMain.py script and 2 others in the cibersecurity foldier, each of these will be further explained bellow.

# Layout

 - [PythoniousMain.py](## PythoniousMain.py)
 - [CyberSecurity](## Cybersecurity Foldier)
    - [Hasher.py](### Hasher.py)
    - [HashMatcher.py](### HashMatcher.py)


## PythoniousMain.py
- This script acts as hub for all the scripts inside the project. All it does is run a recursive search on the foldier where it's stored with the objective of finding all .py files, it then stores them in a dictionary so they can be easily indicated and selected when running the program.
- When running the program the user is prompted to input the number of one of the found scripts, doing so will run the script in a new console window allowing the user to have multiple scripts running side by side.
- 
## Cybersecurity Foldier
**Any and all scripts found inside this foldier are strictly meant to be used for learning purposes or for ethical hacking. They were built with the purpose of furthering my knowledge of cybersecurity and letting curious minds learn as well.**

### Hasher.py
- This simples script allows any text input to be turned into a hash by passing throught the following selection of algorithms:
    - MD5
    - SHA1
    - SHA256
    - SHA512
    - BLAKE2b
    - BLAKE2s
    - SHA3-256
    - SHA3-512
- It's main purpose is to be used in conjunction with the [HashMatcher.py](### HashMatcher.py) by generating a hash that can be used for testing.

### HashMatcher.py
- This script is meant only to be used for learning purposes and nothing else.
- When executing the script it will first request a hash value that it will try to match, to generate one make use of the [Hasher.py](### Hasher.py) script.
- It will then look at the length of the hash value and sugest some algorithms that can be ran, the user can then choose to run all of the sugestions one by one, select just one or even manually select another algorithm to understand the resulting diferences between them.
- The user will then be prompt to insert the number of characters that the plaintext string contained if no number is input it will default to 10 characters.
- Following this the user will have the option of selecting what character set to run which makes the process faster when testing the script by just selecting the `"1.Numbers"` option for exemple.
- Finally the user will get prompted to select a number of threads to run the script with, however even thought the default is set to 4 the option of `"1. Single"` proved to be the fastest as every `brute_force` call will send multiple values to different variables to have them display the attempts in the console in real time making the use of threads not recomended for the purpose of speed but more so for proof of concept.

[Imgur](https://imgur.com/7xXbKw1)
