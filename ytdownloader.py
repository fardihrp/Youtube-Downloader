import pytube

link = "https://www.youtube.com/watch?v=cloYOBXz0ZA&ab_channel=ZahidIbrahim"
yt= pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("Berhasil", link)

#Link Download Thumbnail Youtube
print(yt.thumbnail_url)
