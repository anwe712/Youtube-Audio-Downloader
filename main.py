import subprocess

def download_audio(youtube_url):
    try:
        subprocess.run(['youtube-dl', '-x', '--audio-format', 'mp3', youtube_url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    youtube_url = input("Enter the YouTube URL: ")
    download_audio(youtube_url)
