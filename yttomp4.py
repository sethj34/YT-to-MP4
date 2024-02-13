from functions import *
from pytube import YouTube

link = input("Enter the YouTube video URL: ")
nonmutedoutputpath = "C:/Users/sethj/projects/YT to MP4/nonmutedoutputs"
mutedoutputpath = "C:/Users/sethj/projects/YT to MP4/mutedoutputs"
youtubeObject = YouTube(link)

# Option loop

while True:
    try:
        muteoption = input("Would you like to mute the video? (Y or N): ")

        if muteoption.upper() == "Y":
            muteyn = 1
            break

        elif muteoption.upper() == "N":
            muteyn = 0
            break
    
    except ValueError:
        print("Please make a valid choice.")

try:
    if muteyn == 1:
        downloadedfilename = download(link, nonmutedoutputpath)
        if downloadedfilename:
            mutedfilename = mute(nonmutedoutputpath, mutedoutputpath, downloadedfilename)
            deletenonmuted(mutedfilename)
    elif muteyn == 0:
        download(link, nonmutedoutputpath)
except Exception:
    print("An error occured.")