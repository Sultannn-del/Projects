from pytube import YouTube

def download_video(url, save_path="C:\Users\Hacka--X\Desktop\Python Projects")
try:
    yt = YouTube(url)
    video_stream = yt.streams
    .get_highest_resolution()
    print(f"Downloading: {yt.title}")
    video_stream.download(save_path)
    print("Download Completed!")
except Exception as e:
    print(f"Error: {e}")
    video_url = input("Enter Youtube Vidoe URL:")
    download_video(video_url)