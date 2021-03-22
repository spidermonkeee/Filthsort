from pymediainfo import MediaInfo
import re
import os, os.path, fnmatch
import sys

# print(f"Name of the script      : {sys.argv[0]}")
# print(f"Arguments of the script : {sys.argv[1:]}")

root_directory = os.getcwd()
directory_files = os.listdir(root_directory)
fileExts = dict(videos=('.avi', '.mp4', '.mpeg', '.mpg', '.mkv', '.mov'))
tags = ['RARBG - ','RARBG.COM - ', '.MP4-KTR', '.XXX']
badmatches = [',','Downloaded from','Uploaded To','Encoded by','@','PornRips.to','pornolab.net','www.dvdvideosoft','GalaXXXy','excitemii','INOPORN.ME','_.  _ ','by EroticaShare','camwhores']

if len(sys.argv) <= 1:
    print("Dry run - please use -u to perform rename update")

fileList = fileExts.keys()
for types in fileList:
    exts = fileExts[types]
    for ext in exts:
        for File in directory_files:
            # If the extension of the file matches some text followed by ext...
            if fnmatch.fnmatch(File,'*' + ext):  
                # If the file is truly a file...
                media_info = MediaInfo.parse(File)
                for track in media_info.tracks:
                    if track.track_type == "General":
                        # print("Complete filename ",track.complete_name)
                        # print("Comment   :", track.comment)
                        # print("Movie Name:", track.movie_name)
                        x = track.comment
                        if x  is None or (len(x) == 0): 
                            # Skip this file if no comment
                            continue

                        if len(x) < 5:
                            print("Comment is too short to be good")
                            continue

                        if any(y in x for y in badmatches):
                            print("WARNING: Not renaming with bad comment " + x + " - " + File)
                            continue

                        for tag in tags:
                             x = re.sub(r'\b' + tag + r'\b', '', x)

                        # print(x)
                        renamed = x + ext
                        if len(sys.argv) > 1:
                            if  sys.argv[1] == "-u":
                                if  os.path.isfile(renamed):
                                    print("WARNING: "+ File + " exists in directory")
                                else:
                                    print("           "+ File)
                                    print("Renamed to ",renamed)
                                    print("")
                                    os.rename(File, renamed)
                        else:       
                            if  os.path.isfile(renamed):
                                print("WARNING: " + File + " exists in directory")
                            else:
                                print("                "+ File)
                                print("will renamed to ",renamed)
