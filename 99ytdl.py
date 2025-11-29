from yt_dlp import YoutubeDL

def baixar_audio(url):
    options = {
        "format": "bestaudio/best",
        "extractaudio": True,
        "audioformat": "mp3",
        "outtmpl": "%(title)s.%(ext)s"
    }

    with YoutubeDL(options) as ydl:
        ydl.download([url])

audio_url = "https://www.youtube.com/watch?v=KPZpWPIoqhw&list=RDKPZpWPIoqhw&start_radio=1"

baixar_audio(audio_url)