import ssl
from pytubefix import YouTube
import os

ssl._create_default_https_context = ssl._create_unverified_context


def get_video_resolutions(video_url: str):
    yt = YouTube(url=video_url)
    resolutions = yt.streams.filter(progressive=True).all()
    for i in resolutions:
        print(i)


def download_you_tube(video_url: str, path: str, itag: int) -> None:
    """Downloads YouTube video to local folder
    Args:
        video_url (str): YouTube video URL origin
        path (str, optional): Output folder destination.
    """
    yt = YouTube(url=video_url)

    if not os.path.exists(path):
        os.makedirs(path)
    yt.streams.get_by_itag(itag).download(path)


title_message = "=" * 23

print(
    f"""{title_message}
    \n\033[0;31mYOUTUBE VIDEO DOWNLOADER by Gleyson Carvalho
    \033[0;0m\n{title_message}"""
)

# yt = YouTube(input('Digite a URL do vídeo: '))

video_url = input("Digite a URL do video: ")

get_video_resolutions(video_url)

video_itag = input("Digite a iTag do video: ")

download_you_tube(video_url=video_url, itag=video_itag, path='./download')