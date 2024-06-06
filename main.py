from pytube import YouTube # pip install pytube

def download_video(url, path):
    try:
        if 'youtube' in url:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            print("-- Downloading --")
            stream.download(output_path=path)
            print(f"\n Downloaded: {yt.title}")
        else:
            print("Invalid Url < Check Again")
    except Exception as e:
        print(f"An error occurred , Please Try Again : {e}")

# URL of the video to be downloaded
video_url = input("Enter URL : ")
# Path where the video will be saved
download_path = 'C:\\Users\\User1\\Downloads'

download_video(video_url, download_path)
