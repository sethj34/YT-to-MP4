from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

nonmutedoutputpath = "C:/Users/sethj/projects/YT to MP4/nonmutedoutputs"
mutedoutputpath = "C:/Users/sethj/projects/YT to MP4/mutedoutputs"

def download(link, nonmutedoutputpath):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download(nonmutedoutputpath)
        print("The download was successful!")
        defaultfilename = youtubeObject.default_filename
        return defaultfilename
    except:
        print("An error has occurred when downloading.")
        return None

def mute(nonmutedoutputpath, mutedoutputpath, defaultfilename):
    try:
        videopath = nonmutedoutputpath + "/" + defaultfilename
        video = VideoFileClip(videopath)
        videomuted = video.set_audio(None)
        mutedfilename = defaultfilename
        videomuted.write_videofile(mutedoutputpath + "/" + defaultfilename, codec="libx264", audio_codec="aac")
        video.close()
        return mutedfilename
    except:
        print("An error has occurred when muting.")
        return None

def deletenonmuted(mutedfilename):
    try:
        os.remove(nonmutedoutputpath + "/" + mutedfilename)
    except:
        print("An error has occurred when deleting original file.")
        return None