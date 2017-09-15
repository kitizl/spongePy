# spongPy - a Spongebob Meme
A CLI python program that is based on the popular [mocking spongebob meme](http://knowyourmeme.com/memes/mocking-spongebob).

## Download and Install
1. If you already have python then there should be no problem, really. Just clone this repo and run it like a normal python program.
2. If you don't, then:
    - For windows Users:
        1. Go to the official python website and download python.
        2. Run this in the terminal by running `python spongePy.py [option]`
    - For Linux/Unix Users:
        1. Python is preinstalled, but if you want to be extra sure then `sudo apt install python3` ought to do it.
    - For Mac users:
        1. No idea.

## Usage
There are two ways in which you can run this program.

### Normal Way
1. Run the program as `python3 spongePy.py`
2. Once you run the program, there will be no prompt. Enter the string you want to be memefied.
3. Once you hit return, you should see the changed text.
4. Press Ctrl-D if you want it all to stop.

### Realistic Way
1. Run the program as `python3 spongePy.py -r`
2. Once you run the program, there will be no prompt. Enter the string you want to be memefied.
3. Once you hit return, you should see the changed text.
4. Press Ctrl-D if you want it all to stop.

The difference is that the Normal Way would only alternate capitalization and the Realistic Way (which is how we do it IRL) is where the capitalization is random, but mostly adheres to the every alternating letter rule.

## Alternative Usage
You can input and output from/to files using the `<` and `>` commands.
For instance, if you wanted to do it the realistic way and input and output to files, the following should work
`python3 spongePy.py -r < [input-file] > [output-file]

If you want to test the file input-output features, you can use the sample files in the `sample-inputs` directory, in which case, `[input-file]` would then become `./sample-inputs/[filename]`. 

Also, if you are on Windows, then `python3` command wouldn't work. Instead you should type `python` even though you have python 3.5 installed.

This project was inspired by [PenguinGovernor](https://github.com/PenguinGovernor/) who implemented the same idea in Go. You can find his version over [here](https://github.com/PenguinGovernor/GoSpongebob).


