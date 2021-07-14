# Filthsort
Sort / Organise Collections or Porn from a cluttered mess into designated folders
```
 /$$$$$$$$ /$$ /$$   /$$     /$$        /$$$$$$                        /$$    
| $$_____/|__/| $$  | $$    | $$       /$$__  $$                      | $$    
| $$       /$$| $$ /$$$$$$  | $$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$  /$$$$$$  
| $$$$$   | $$| $$|_  $$_/  | $$__  $$|  $$$$$$  /$$__  $$ /$$__  $$|_  $$_/  
| $$__/   | $$| $$  | $$    | $$  \ $$ \____  $$| $$  \ $$| $$  \__/  | $$    
| $$      | $$| $$  | $$ /$$| $$  | $$ /$$  \ $$| $$  | $$| $$        | $$ /$$
| $$      | $$| $$  |  $$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$        |  $$$$/
|__/      |__/|__/   \___/  |__/  |__/ \______/  \______/ |__/         \___/    
```                                                                                     
![Python application](https://github.com/spidermonkeee/Filthsort/workflows/Python%20application/badge.svg)
### Description
Inspired by the bash script [Filthmover](https://github.com/filthmover/filthmover), I tried to make some of the features more portable for any system (e.g. Windows). I hope to integrate a folder picture grabber feature that can label folders.

Clean up a messy folder with many downloaded but otherwise well named files into more managable folders. This can be based on an input driver file which is just a 2 column csv file. An example list is provided, which has the topic of adult film sites. Order does not matter. Although it is a manual process to create a list, this ensures that we can sort on specifics we want and apply consistency over many cleanup jobs. Some modes do not require the use of an input file, but makes sorting less powerful.

Currently there are 6 modes:
- Organise * files by keywords and put in extension folder (-i)
- Organise files by keywords and put in extension folder but only on 1 category (-i -e -t)
- Organise by keywords to sortlist locations (-i -t)

- Organise all by keywords only with X ext to sortlist locations (-i -e)
- Organise all files to extension folders (-e)
- Organise by filetype to ext folder (-e -t)

#### Parameters
'-i', '--input',
Name of sort file: User self defined csv of keywords to filter sorted files. <NAME OF SEARCHTERM>,<RELATIVE FILE PATH AS DESTINATION>

'-e', '--ext',
Use this to set to use extensions as sort destination.

'-t', '--type',
Preset defined categories to filter on eg Documents. Default = All files if flag not specified

### Customise
At the moment, the file types searched on are hardcoded within the script. It is easy to add and remove these by altering the code
e.g.
archives=('.rar', '.zip', '.7z', '.iso', '.arc', '.tar.gz', '.tar.xz', '.tgz', '.deb','<ADD YOUR OWN ARCHIVE FILE EXTENSION>'),


### Requirements
- Python 3 installed (should work on any 3.7+ version; 2.7 not tested)
 
- Additional package required for using the GUI version, 'filthsortgooey.py' `pip install Gooey`
#### Running

``` python filthsort.py -i sortlist.csv -e -t Videos ```

- I copy over the script and run it directly from the folder to be sorted via command line (with any sortlists). This should be changed in the future
 
 Optionally, there is a GUI version. Very barebones, and requires being in the working directory.
