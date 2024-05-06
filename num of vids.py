from pytube import Playlist

playlist_link = "https://www.youtube.com/playlist?list=PLvz8W-_DSfFoHb3CvjYAjgndJtu_IOPyV"
video_links = Playlist(playlist_link).video_urls

length = len(video_links)

print(length)


how_many_vids = input("Do you want to download (type the corresponding number) \n1. first few \n2. last few \n3. all "
                      "of them\n:")

if how_many_vids == "1":
    num_of_vids = int(input("How many videos do you want to convert from the start of this playlist? :"))
    video_links1 = video_links[:-(length - num_of_vids)]
if how_many_vids == "2":
    num_of_vids = int(input("How many videos do you want to convert from the end of this playlist? :"))
    video_links1 = video_links[int(length - num_of_vids):length]
elif how_many_vids == "3":
    video_links1 = video_links
