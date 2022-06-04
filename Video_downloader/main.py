from pytube import YouTube

link=input("Enter the link of the video you want to download:")
yt=YouTube(link)
print("Title of the video:",yt.title)
print("Views of the video:",yt.views)
print("Length of the video:",yt.length/60)

video=yt.streams.get_highest_resolution()
print(video)
video.download()
print("Download complete!")
