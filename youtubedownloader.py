import os

import yt_dlp


def list_formats(video_url):
    ydl_opts = {
        "listformats": True,  # Lists all available formats
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(video_url, download=False)


def download_youtube_video(video_url, format_code, output_path):
    output_template = os.path.join(output_path, "%(title)s.%(ext)s")

    ydl_opts = {
        "format": format_code,  # Uses specified format
        "outtmpl": output_template,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])


# Specify output path
output_path = "C:/Users/Henrique/Downloads"

# Request video URL from user
video_url = input("Please enter the full URL of the YouTube video: ")

# List available formats
list_formats(video_url)

# Request format codeoutput_template = os.path.join(download_folder, '%(title)s.%(ext)s')
format_code = input("Please enter the format code to be downloaded (e.g. 137+140): ")

try:
    print(f"Download video in format {format_code}...")
    download_youtube_video(video_url, format_code, output_path)
    print("Download completed successfully.")
except ValueError as e:
    print(e)
