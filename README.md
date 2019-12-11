# CMSI 385 Final Project: NFA Simulator

This repo is for Joe Maiocco's NFA simulator, implemented in Python.

__Note__: Lambdas are represented as the underscore "\_" character in input strings. Lambda moves must be explicitly stated when taken within strings, e.g. "aaa_a".

## Command Line Version

The command line version of the NFA simulator can be found in nfa_command_line.py. When run with no command line arguments (e.g. "python nfa_command_line.py" on a Windows machine), the program prompts the user for input that describes the NFA intended to be simulated. This input is written to a .txt file. The required input format is  

START=q0;ACCEPT=q2,q1|q0:a->q1|q0:a->q2|q0->q2|q0:a->q0

so that the program can reformat the newly created file to look like 

START=q0;ACCEPT=q2,q1  
q0:a->q1  
q0:a->q2  
q0->q2  
q0:a->q0  

for later parsing. When run with one command line argument and a .txt file passed via STDIN (e.g. "python nfa_command_line.py < input.txt aaa_a" on a Windows machine), the program will print out whether or not the given string is accepted by the machine described in the file. 

## Non-Command Line Version w/ Test Suite

The basic version of the NFA simulator can be found in nfa.py. This program runs the accompanying test suite, nfa_tests.py, with pytest.
