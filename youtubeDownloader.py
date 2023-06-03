from pytube import YouTube
from pytube.cli import on_progress

def resolutionChoose():
    print("====================Downloader====================")
    print("Choose between three options below:")
    print("1. Lowest Resolution")
    print("2. Highest Resolution")
    print("3. Exit")
    print("====================Downloader====================")

    while True:
        choose = input("Choose and type (1, 2, 3): ")
        if choose == '1':
            link = input("Enter the YouTube URL: ")
            lowestResolution(link)
        elif choose == '2':
            link = input("Enter the YouTube URL: ")
            highestResolution(link)
        elif choose == '3':
            exit()
        else:
            print("Invalid option. Please choose (1, 2, 3).")

def lowestResolution(link):
    ytDownloader = YouTube(link)
    ytDownloader.register_on_progress_callback(on_progress)
    ytDownloader.streams.get_lowest_resolution().download()
    print("Your download has completed successfully.")

def highestResolution(link):
    ytDownloader = YouTube(link)
    ytDownloader.register_on_progress_callback(on_progress)
    ytDownloader.streams.get_highest_resolution().download()
    print("Your download has completed successfully.")

resolutionChoose()