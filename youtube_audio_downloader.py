import subprocess
import sys

def download_audio(youtube_url):
    try:
    
        subprocess.call(['yt-dlp', '-x', '--audio-format', 'mp3', '-o', '(enter the path where you want to save the audio)%(title)s.%(ext)s', youtube_url])



        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python youtube_audio_downloader.py <YouTube_URL>")
        sys.exit(1)
    
    youtube_url = sys.argv[1]
    download_audio(youtube_url)
