# Youtube-playlist-to-mp3.
This program will convert youtube playlist to mp3 and store it in a file (python 3.10 required). 
Note: ideally this should work great if the videos on your playlist are about 1 to 6 min long(it was initially made to convert songs), but if you want to convert longer videos(i.e podcasts etc) you'll have to increase and adjust time.sleep(n).                                                                                                                                                                                                             
1. download adguard.crx the file is given in the repository 

2. download chrome driver (important : note that the chrome driver version you download matches or is mostly similar to the version of the chrome you've installed on your mac or windows) just google chrome driver and you'll be able to download it.

3. copy main.py and make sure all packages are installed.


9. for windows script change the path in line 48 -- chrome_options.add_extension(r"paste your adguard.crx file path here")
10. for windows script change the path in line 55 -- service = Service(r"paste your chromedriver file path here")
11. for windows script change the path in line 100 -- os.chdir("paste your downloads folder path here") 
