# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os
import datetime as dt
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import time

today = dt.datetime.now().date()
basepath = "D:/Videos"
output_path = "D:/Echaniz/Videos/"

convertedvideos=[]

#Folder IDs
SeptA_folder="1k6GCdOZ18UYi1dRljcr7dAwbOG-OiwvU"
tallerId="1Zsnrx7TbWmMatloVA5clkCmxtDKjBofO"
sistProg="19bpBL1g_saVOGWzHuGrGr_jWHW8swpp8"
silvia="1XpBakCT1deL_6g0ZtTeKxYIkkT1y4Q7X"
redes="1LYpj76_miS2UjWj7qXzQR37mrmP6Ki4B"
ProgWeb="1f5mb4015TrBVtZe4iZ5IMCkHfQjSXuof"
LengyAut="1kb6l0swGWVureFmXEp-5hx-k8fgkBXta"
japanese="1RJcb1DlLb0nWguNFUlbt3ckBz6O5bfr2"


def readDir():
    videos=os.listdir(basepath)
    print("videos found")
    for video in videos:
        videodate = dt.datetime.fromtimestamp(os.path.getctime(basepath +"/"+ video)).date()
        print(video +": date " + str(videodate))

        if videodate==today:
            convertedvideos.append(convert(video))

def convert(video):
    print(f"Converting: {video}")
    input_path = basepath +"/"+ video
    newVideoName=getClassName(video)+"_"+ video
    video_output = output_path +"/"+ newVideoName
    video_output = video_output.replace(" ","_")

    os.system(f'ffmpeg -i "{input_path}" -vcodec libx264 -crf 28 "{video_output}"')
    #os.system(f'ffmpeg -hwaccel nvec -i "{input_path}" -vcodec libx264 -crf 28 "{video_output}"')
    #os.system(f'ffmpeg -hwaccel_output_format cuda -i "{input_path}" -c:v h264_nvenc -preset fast -pixel_format yuv444p "{video_output}"')
    #ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i input.mp4 -c:a copy -c:v h264_nvenc -b:v 5M output.mp4
    #os.system(f'ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i "{input_path}" -crf 28 -c:a aac -c:v h264_nvenc -b:v 5M "{video_output}"')

    print("Done")
    return newVideoName

def upload():
    print(dt.datetime.now().time())

    #gauth.SaveCredentialsFile("mycreds.txt")
    if(today.weekday()==5): #Check if its saturday
       os.system(f"python youtube-upload --title='{cVideo}' --description='Japanese' --category=' Education' --tags='ITZ' --playlist='Japanese' {cVideo}")
    else:
        for cVideo in convertedvideos:
            cVideo=cVideo.replace(" ","_")
            print(f"Uploading: {cVideo}")
            os.system(f"python youtube-upload --title='{cVideo}' --description='{getClassName(cVideo)}' --tags='ITZ' --playlist={getClassName(cVideo)} {cVideo}")

            #Uses this program: https://github.com/tokland/youtube-upload to actually upload the video.
            time.sleep(10)

    print("DONE UPLOAD")
    print(dt.datetime.now().time())

def getFolderId(video):
    vidTime=int(video[-12: -10])
    print(f"Video Captured time: {vidTime}")

    switch={
        7:tallerId,
        8:ProgWeb,
        9:sistProg,
        10:redes,
        12:silvia,
        13:LengyAut
    }
    return switch.get(vidTime,SeptA_folder)

def getClassName(video):
    vidTime=int(video[-12: -10])
    print(f"Video Captured time: {vidTime}")

    switch={
        7:"taller",
        8:"ProgWeb",
        9:"sistProg",
        10:"redes",
        12:"silvia",
        13:"LengyAut"
    }
    return switch.get(vidTime,"7A")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readDir()
    upload()
    print("PROGRAM DONE")
    print(dt.datetime.now().time())

