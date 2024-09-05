import pyktok as pyk
import os

def download_tiktok_video(url, output_file):
    try:
        # Specify the browser to use for accessing cookies
        pyk.specify_browser('firefox')  # Change 'firefox' to your preferred browser

        # Use pyktok to download the video
        pyk.save_tiktok(url, True, output_file, 'firefox')  # Ensure the browser matches the one specified

        print(f"Downloaded: {output_file}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def main():
    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.abspath(__file__))

    # Construct the path to the url.txt file in the same directory as the script
    urls_file = os.path.join(script_directory, 'url.txt')

    # Open and read the URLs from the file
    with open(urls_file, 'r') as file:
        urls = file.readlines()

    # Download each TikTok video from the URLs
    for url in urls:
        url = url.strip()  # Remove any leading/trailing whitespace

        if '/video/' in url:  # Ensure the URL is for a video
            # Generate a filename based on the URL
            video_id = url.split('/')[-1].split('?')[0]
            output_file = f"tiktok_{video_id}.mp4"
            download_tiktok_video(url, output_file)
        else:
            print(f"Skipping non-video URL: {url}")

if __name__ == '__main__':
    main()
