import argparse

parser = argparse.ArgumentParser()

parser.add_argument('num' , help='squares the given number' , type = int)
#The choices parameter specifies a list of valid values that the argument can take.

parser.add_argument('-v' , '--verbose' , help='define a verbose description' ,
                    type=int , choices=[0 , 1 , 2])
 
args = parser.parse_args()

if args.verbose == 0:
    print('Option 1')
elif args.verbose == 1:
    print('Option 2')
elif args.verbose == 2:
    print('Option 3')

print(args.num ** 2)
