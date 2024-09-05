# tiktok-downloader
TikTok Video Downloader
This script allows users to download TikTok videos by providing URLs in a url.txt file. The script is designed to run on Windows and uses the pyktok library to handle the download process.

Prerequisites
Before using this script, ensure you have the following installed on your Windows system:

1. Python: Version 3.6 or higher.
2. pip: Python package manager, which is included with Python installations.

**Installation Guide**
**Step 1: Install Python**
Visit the [Python Downloads page](https://www.python.org/downloads/).
Download the latest Python installer for Windows.
Run the installer and ensure you check the box that says "Add Python to PATH".
Complete the installation process.

**Step 2: Install Required Libraries**
Open Command Prompt.
Install the pyktok library by running the following command:
`pip install pyktok`

**Step 3: Prepare the url.txt File**
Create a file named url.txt in the same directory as the script.
Add TikTok video URLs to this file, each on a new line.
the content of the url.txt file should be videos link, you can achieve this by using chrome extension [Link Gropher](https://sites.google.com/site/linkgopher/)
after you installed the link gropher, open the tiktok account and scroll down until are videos are loaded, and extract all link using the extension, and copy it into url.txt file

**Usage Instructions**
Place the **script file** and **url.txt** in the same directory.
Open Command Prompt and navigate to the directory containing the script.
Run the script using the following command:
`python main_file.py`
The script will read the URLs from url.txt, download each video, and save them in the same directory.
NOTES :
Ensure Firefox is installed on your system

Troubleshooting
Ensure Browser Compatibility: The script uses a browser to access cookies. Ensure Firefox is installed on your system.
Check Python Path: If you encounter issues running the script, ensure that Python is added to your system's PATH.
Notes
The script is designed to skip non-video URLs.
Video files will be named based on their TikTok video ID.
