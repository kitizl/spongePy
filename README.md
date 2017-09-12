# spongPy - a Spongebob Meme
A CLI python program that is based on the popular [mocking spongebob meme](http://knowyourmeme.com/memes/mocking-spongebob).

## Download and Install
1. If you already have python then there should be no problem, really. Just clone this repo and run it like a normal python program.
2. If you don't, then:
    - For windows Users:
        1. Go to the official python website and download python.
        2. Run this in the terminal by running `python spongePy.py`
    - For Linux/Unix Users:
        1. Python is preinstalled, but if you want to be extra sure then `sudo apt install python3` ought to do it.
    - For Mac users:
        1. No idea.

## Usage
1. Once you run the program, there will be no prompt. Enter the string you want to be memefied.
2. Once you hit return, you should see the changed text.
3. Press Ctrl-D if you want it all to stop.

## Alternative Usage
1. If you want to use an input file, then type `python3 spongePy.py < [inputfile]`
2. If you want to output memefied thing, then type `python3 spongePy.py > [outputfile]`
3. If you want to be even more bonkers, and take an input file and output it to another file, then type `python3 spongePy.py < [inputfile] > [outputfile]`

If you want to test the file input-output features, you can use the sample files in the `sample-inputs` directory, in which case, `[file]` would then become `./sample-inputs/[filename]`. 

This project was inspired by [PenguinGovernor](https://github.com/PenguinGovernor/) who implemented the same idea in Go. You can find his version over [here](https://github.com/PenguinGovernor/GoSpongebob).


