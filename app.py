import ssl
import moviepy.editor as mpe
import os
import pytubefix

ssl._create_default_https_context = ssl._create_unverified_context

video_url = input('Digite a URL do video: ')

yt = pytubefix
vname = "./temp/clip.mp4"
aname = "./temp/audio.mp3"

yt_source = yt.YouTube(video_url)
output_name = yt_source.title

# Download video and rename
video = (
    yt_source
    .streams.filter(subtype="mp4", res="1080p")
    .first()
    .download()
)
os.rename(video, vname)

# Download audio and rename
audio = (
    yt_source
    .streams.filter(only_audio=True)
    .first()
    .download()
)
os.rename(audio, aname)

# Setting the audio to the video
video = mpe.VideoFileClip(vname)
audio = mpe.AudioFileClip(aname)
final = video.set_audio(audio)

# Output result
final.write_videofile(f'./download/{output_name}.mp4')

# Delete video and audio to keep the result
os.remove(vname)
os.remove(aname)
