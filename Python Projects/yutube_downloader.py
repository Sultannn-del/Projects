from pytube import YouTube
import os

def download_video():
    try:
        url = input("paste the youtube url")
        yt = YouTube(url)

        print(f"Title:{yt.title}")
        print(f"Views:{yt.Views}")

        stream = yt.streams.filter(progressive=True, file_extention='mp4').order_by('resolution').desc().first()

        print("Downloading...")
        stream.download()
        print("Download Complete!")

        except Exception as e:
            print(f"Error:{e}")
            is __name__ == "__main__" :
            download_video()