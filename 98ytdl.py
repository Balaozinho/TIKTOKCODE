from yt_dlp import YoutubeDL

def baixar_video (url):
    options = {
        "format": "bestvideo+bestaudio/best",
        "merge_output_format": "mp4",
        "outtmpl": "%(title)s.%(ext)s"
    }

    with YoutubeDL (options) as ydl:
        ydl.download([url])
    

video_url = "https://www.youtube.com/watch?v=nHalaFUqnTI"
baixar_video(video_url)


