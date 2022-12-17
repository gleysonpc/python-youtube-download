import ssl
from pytube import YouTube
import os

ssl._create_default_https_context = ssl._create_unverified_context

def download_you_tube(video_url: str, path: str = './download') -> None:
    """ Downloads YouTube video to local folder
    Args:
        video_url (str): YouTube video URL origin
        path (str, optional): Output folder destination. Defaults to './download'.
    """
    yt = YouTube(video_url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

download_you_tube('')