# Youtube-playlist-to-mp3.
This program will convert youtube playlist to mp3 and store it in a file. 
Note: ideally this should work great if the videos on your playlist are about 1 to 6 min long(it was initially made to convert songs), but if you want to convert longer videos(i.e podcasts etc) you'll have to increase and adjust time.sleep(n).                                                                                                                                                                                                             
1. download adguard.crx the file is given in the repository (doesn't matter if your are using windows or mac os)

2. download chrome driver (important : note that the chrome driver version you download matches or is mostly similar to the version of the chrome you've installed on your mac or windows) just google chrome driver and you'll be able to download it.

3. copy main-for-windows.py or main-for-pac.py code depending on your os and make sure the packages are installed.


4. for mac os script change the path in line 46 -- chrome_options.add_extension("paste your adguard.crx file path here")
5. for mac os script change the path in line 51 -- browser = webdriver.Chrome("paste your chromedriver file path here", options=chrome_options)
6. for mac os script change the path in line 96 -- os.chdir("paste your downloads folder path here") 



9. for windows script change the path in line 48 -- chrome_options.add_extension(r"paste your adguard.crx file path here")
10. for windows script change the path in line 55 -- service = Service(r"paste your chromedriver file path here")
11. for windows script change the path in line 100 -- os.chdir("paste your downloads folder path here") 
