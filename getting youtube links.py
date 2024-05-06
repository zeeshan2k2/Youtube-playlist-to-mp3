from pytube import Playlist


playlist_link = input("Enter the link of the playlist: ")
video_links = Playlist(playlist_link).video_urls
print(video_links)