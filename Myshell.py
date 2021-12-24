#!/usr/bin/python3
import os
import sys
import shlex


HOME = os.getenv("HOME")
err = "An error has occurred"

def basicCommand(inputUser):
    try:
        listInputWhitoutSpaces = shlex.split(inputUser)

        if not listInputWhitoutSpaces:
            return None

        if listInputWhitoutSpaces[0].find('ls') != -1:
            if listInputWhitoutSpaces[0]=='ls' and len(listInputWhitoutSpaces)==1:
                print(os.listdir())
            elif len(listInputWhitoutSpaces)==3 and listInputWhitoutSpaces[1]==">":
                str = ""
                for mot in os.listdir():
                    str += mot +" "
                open(listInputWhitoutSpaces[2],'w').write(str)
            elif '>' in listInputWhitoutSpaces[0] and len(listInputWhitoutSpaces)==1:
                strUpdate=listInputWhitoutSpaces[0][0:2]+' '+listInputWhitoutSpaces[0][2] + ' ' + listInputWhitoutSpaces[0][3:]
                print(strUpdate)
                basicCommand(strUpdate)
            else:
                print(err, file=sys.stderr)

        
        elif listInputWhitoutSpaces[0]== './mysh':
            print('mysh$ pwd')
            return basicCommand('pwd')

        elif listInputWhitoutSpaces[0] == 'pwd' or (listInputWhitoutSpaces[0]=='echo' and listInputWhitoutSpaces[1]=='$PWD'):
            print(os.getcwd())

        elif listInputWhitoutSpaces[0] == 'cd':
            if len(listInputWhitoutSpaces) == 1:
                print("You forgot to write the name of the directory you want to access.")
                os.chdir(HOME)
            else:
                os.chdir(listInputWhitoutSpaces[1].replace('/', ''))
        elif listInputWhitoutSpaces[0] == 'exit':
            sys.exit(0)


    except Exception:
        print(err, file=sys.stderr)


def shell():
    while True:
        inputUser = input("mysh$ ")
        basicCommand(inputUser)


def batch_mode(fileInput):
    with open(fileInput, 'r') as file:
        stderr_fileno = sys.stderr.fileno()
        for line in file:
            os.write(stderr_fileno, line.encode())
            basicCommand(line)

if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) > 1:
        batch_mode(sys.argv[1])
    else:
        shell()