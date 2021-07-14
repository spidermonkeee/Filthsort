#!/usr/bin/env python3

# Drop this folder in a directory and run it, along with sortfile
import os, os.path, shutil, fnmatch, sys
from colorama import init, Fore, Style
from sys import exit
import argparse
from pathlib import Path
from gooey import Gooey
from gooey import GooeyParser
init(autoreset=True) ## Autorest color back to default after each print used with colorama

## Preset Colors
COLOR_END       = Style.RESET_ALL               ## RESET/END
COLOR_GREEN     = Fore.GREEN + Style.BRIGHT     ## SUCCESS
COLOR_RED       = Fore.RED + Style.BRIGHT       ## ERROR
COLOR_YELLOW    = Fore.YELLOW + Style.BRIGHT    ## INFO
COLOR_CYAN      = Fore.CYAN + Style.BRIGHT
## Version number
VERSION = '0.1'
sortdictname = ''
#filetype = ''
# THE CODE
#------------------------------------------------------------------------------
root_directory = os.getcwd()
directory_files = os.listdir(root_directory) # This is how you get all of the files and folders in a directory
root_size = os.path.getsize(root_directory) # Just a tip on how to get the size of a directory
listOfSites = dict()

fileExts = dict(archives=('.rar', '.zip', '.7z', '.iso', '.arc', '.tar.gz', '.tar.xz', '.tgz', '.deb'),
                images=('.jpeg', '.jpg', '.JPG', '.png', '.PNG', '.gif', '.bmp', '.svg', '.fig'),
                documents=('.txt', '.doc', '.docx', '.xls', '.xlsx', '.odt', '.ods', '.ppt', '.pptx'),
                pdfs=('.pdf', '.PDF'),
                videos=('.avi', '.mp4', '.mpeg', '.mpg', '.mkv', '.flv', '.mov', '.wmv'),
                audio=('.mp3', '.flac', ".wma", '.wav', '.3gpp'),
                executables=('.exe', '.bat', '.sh', '.jar'),
                other=('.csv', '.xxx'))


def organize_files_by_extension(ext):
    counter = 0
    for File in directory_files:
        # If the extension of the file matches some text followed by ext...
        if fnmatch.fnmatch(File,'*' + ext):
            print (File)        
            # If the file is truly a file...
            if os.path.isfile(File):
                try:
                    if not os.path.isdir(ext):
                        os.makedirs(ext)
                except:
                    None
                # Copy that file to the directory with that extension name
                try:
                    shutil.move(File,ext)
                    print ('\"' + File + '\" sorted to category:\t ' + ext)          
                except shutil.Error as e:
                    print('Error: Path exists renaming ' + File)
                    counter = counter + 1
                    p = Path(File)
                    target = Path(p.parent, "{}_{}_{}".format(p.stem, counter, p.suffix))
                    p.rename(target)
                    print (target)
                    shutil.move(str(target),ext)                

def organize_files_by_keyword(key,val):
    counter = 0
    for File in directory_files:
        # If the name of the file contains a keyword
        # Use REGEX here
        if fnmatch.fnmatch(File,'*' + key + '*'):
            # If the file is truly a file...
            if os.path.isfile(File):
                try:
                    # Make a directory with the keyword val if not existent...
                    if not os.path.isdir(val):
                        os.makedirs(val)
                except:
                    None
                try:
                    shutil.move(File,val)
                    print ('\"' + File + '\" sorted to :\t ' + val)                
                except shutil.Error as e:
                    print('Error: Path exists renaming ' + File)
                    counter = counter + 1
                    p = Path(File)
                    target = Path(p.parent, "{}_{}_{}".format(p.stem, counter, p.suffix))
                    p.rename(target)
                    print (target)
                    shutil.move(str(target),val)



def organize_files_by_keyword_and_ext(key,val,ext):
    counter = 0
    for File in directory_files:
        # If the name of the file contains a keyword
        # Use REGEX here
        if fnmatch.fnmatch(File,'*' + key + '*' + ext):
            # If the file is truly a file...
            if os.path.isfile(File):
                try:
                    # Make a directory with the keyword val if not existent...
                    if not os.path.isdir(ext):
                        os.makedirs(ext)
                except:
                    None
                # Copy that file to the directory with that keyword name
                try:
                    shutil.move(File,ext)
                    print ('\"' + File + '\" sorted to category:\t ' + ext)          
                except shutil.Error as e:
                    print('Error: Path exists renaming ' + File)
                    counter = counter + 1
                    p = Path(File)
                    target = Path(p.parent, "{}_{}_{}".format(p.stem, counter, p.suffix))
                    p.rename(target)
                    print (target)
                    shutil.move(str(target),ext)       


def organize_files_by_keyword_and_type(key,val,ext):
    counter = 0
    for File in directory_files:
        # If the name of the file contains a keyword
        # Use REGEX here
        if fnmatch.fnmatch(File,'*' + key + '*' + ext):
            # If the file is truly a file...
            if os.path.isfile(File):
                try:
                    # Make a directory with the keyword val if not existent...
                    if not os.path.isdir(val):
                        os.makedirs(val)
                except:
                    None
                # Copy that file to the directory with that keyword name
                try:
                    shutil.move(File,val)
                    print ('\"' + File + '\" sorted to :\t ' + val)                
                except shutil.Error as e:
                    print('Error: Path exists renaming ' + File)
                    counter = counter + 1
                    p = Path(File)
                    target = Path(p.parent, "{}_{}_{}".format(p.stem, counter, p.suffix))
                    p.rename(target)
                    print (target)
                    shutil.move(str(target),val)


def open_wordlist(inputstr):
    global sortdictname

    try:
        sortdictname = inputstr
        if sortdictname:
            with open (sortdictname, "r") as sortfile:
                for line in sortfile:
                    currentline = line.strip().split(',')
                    key = currentline[0]
                    value = currentline[1]
                    listOfSites.update({key: value})     
    except FileNotFoundError:
        print(COLOR_RED + f'Unknown file {inputstr} not found.') 
        exit(-1)
    except Exception as ex:
        print(COLOR_RED + f'Error on\t: {inputstr} [FILE]\n')
        exit(-1)

    #print (listOfSites)

def checkType(args):
    #Simple guesser if you entered bad category
    if args.type:
        fileList = fileExts.keys()
        if args.type not in fileList:

            choices = {'ar': 'archivess', 'im': 'images', 'do': 'documents', 'pd': 'pdfs', 'vi': 'videos', 'au': 'audio', 'ex': 'executables', 'ot': 'other'}
            keyd= args.type[0:2]
            result = choices.get(keyd, 'other')
            try:
                confirm = str(input("Did you mean: " + result + "? (Y/N)"))
            except ValueError:
                print("Oops! I missed that.  Try again...")


            if confirm == 'Y' or confirm == 'y':
                args.type = result
            else:
                print(COLOR_RED + f'Exiting...')
                sys.exit()
    return args

#------------------------------------------------------------------------------
# Big mess of a method lol
def organise(args):

    if args.input:
        if args.ext:
            if not args.type:
                print('Organise files by keywords and put in extension folder')
                open_wordlist(args.input)
                fileList = fileExts.keys()
                for types in fileList:
                    exts = fileExts[types]
                    for ext in exts:
                        for key, val in listOfSites.items():
                            organize_files_by_keyword_and_ext(key,val,ext)
            if args.type:
                print('Organise files by keywords and put in extension folder but only on 1 category' + args.type)
                open_wordlist(args.input)
                fileList = fileExts.get(args.type)
                print (fileList)
                for ext in fileList:
                    for key, val in listOfSites.items():
                            organize_files_by_keyword_and_ext(key,val,ext)
        else:
            if not args.type:
                print('Organise by keywords to sortlist locations')
                open_wordlist(args.input)
                for key, val in listOfSites.items():
                    organize_files_by_keyword(key,val)
            if args.type:
                print('Organise all by keywords only with ' + args.type + ' ext to sortlist locations')
                open_wordlist(args.input)
                fileList = fileExts.get(args.type)
                print (fileList)
                for ext in fileList:
                    for key, val in listOfSites.items():
                            organize_files_by_keyword_and_type(key,val,ext)
    elif args.ext:
        if not args.type:
            print('Organise all files to extension folders')
            fileList = fileExts.keys()
            for types in fileList:
                exts = fileExts[types]
                for ext in exts:
                    organize_files_by_extension(ext)
        if args.type:
            print('Organise ' + args.type + ' by filetype to ext folder')
            fileList = fileExts.get(args.type)
            print (fileList)
            for ext in fileList:
                organize_files_by_extension(ext)
    else:
        print (COLOR_RED + f'No valid selection made. Need to specify at least 1 arg')


# Big money NE ascii type
def welcome():
    print(COLOR_CYAN + '''

 /$$$$$$$$ /$$ /$$   /$$     /$$        /$$$$$$                        /$$    
| $$_____/|__/| $$  | $$    | $$       /$$__  $$                      | $$    
| $$       /$$| $$ /$$$$$$  | $$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$  
| $$$$$   | $$| $$|_  $$_/  | $$__  $$|  $$$$$$  /$$__  $$ /$$__  $$|_  $$_/  
| $$__/   | $$| $$  | $$    | $$  \ $$ \____  $$| $$  \ $$| $$  \__/  | $$    
| $$      | $$| $$  | $$ /$$| $$  | $$ /$$  \ $$| $$  | $$| $$        | $$ /$$
| $$      | $$| $$  |  $$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$        |  $$$$/
|__/      |__/|__/   \___/  |__/  |__/ \______/  \______/ |__/         \___/  
                                                                                                                                                           
                                                          
''' + COLOR_RED + ' Version ' + COLOR_YELLOW + VERSION )


# EXTRA STUFF

#------------------------------------------------------------------------------            
def match_files(ext):
    # 'Prints files with extension ext'
    for File in directory_files:
        if fnmatch.fnmatch(File,'*' + ext):
            print (File)
    # * matches everything
    # ? matches any single character
    # [seq] matches any character in seq
    # [!seq] matches any character not in seq
#------------------------------------------------------------------------------
# match_files('txt')
# match_files('py')
#------------------------------------------------------------------------------
#----------------------------MAINLINE------------------------------------------


@Gooey(terminal_font_family='consolas')
def main():  
    argparser = GooeyParser(description='Sort out messy folders with many files')

    argparser.add_argument('-i', '--input', help="name of the sortfile to process", widget='FileChooser') 
    # argparser.add_argument(
    #     '-i', '--input',
    #     action='store',
    #     type=str,
    #     help='Name of sort file: User self defined csv of keywords to filter sorted files.'
    # )
    argparser.add_argument(
        '-e', '--ext',
        action='store_true',
        help='Use this to set to use extensions as sort destination'
    )
    argparser.add_argument(
        '-t', '--type',
        choices=fileExts.keys(),
        type=str.lower,
        help='Preset defined categories to filter on eg Documents. Default = All files if flag not specified'
    )

    args = argparser.parse_args()

    args = checkType(args)

    welcome()
    
    organise(args)

if __name__ == '__main__':
    main()