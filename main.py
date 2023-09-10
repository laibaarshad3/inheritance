#example of ARGPARSE library
import argparse

#ArgumentParser is a class provided by the argparse library. It is used to define and manage the command-line arguments
parser = argparse.ArgumentParser(description='This is a example of a argparse')

#define the command-line arguments using add_argument method, 
parser.add_argument('name' , help='define a name' , type=str)
parser.add_argument('number' , help='sum the given number' , type=int)
parser.add_argument('city' , help='define a city' , type= str)
parser.add_argument('-v', '--verbose' , help='gives the verbose' , action='store_true')

#args is a variable that holds the result of parsing the command-line arguments using the parse_args() 
args = parser.parse_args()

print(f"The name of user is {args.name}.")
print(f"The sum of the number is {args.number+20}.")
print(f"The city of the user is {args.city}.")
#verbose is optional parameter
if args.verbose :
    print(f"the square of {args.number} is {args.number**2} .")#use -v or -- verbose in the last of bash

#to print the output bash = python main.py (any name) (any num) (any city) 
