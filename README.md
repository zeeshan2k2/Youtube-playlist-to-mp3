This program will convert youtube playlist to mp3 and store it in a file (python 3.10). 
Note: ideally this should work great if the videos on your playlist are about 1 to 6 min long(it was initially made to convert songs).It should convert longer videos, but if it gives an an error multiple times you might have to increase and adjust time.sleep(n). Also keep in mind that your internet connection being too slow or being highly unstable might effect how it runs. This program should work great at any stable connection speed(i.e 2mb or more). This program also depends on how yt5s.io.com is working if the website is slow there might be an issue you can check it by opening the site entering a random youtube video link and then downloading its mp3 (note: it should usually take couple of seconds if not that means website is not funcitoning properly).                                                                                                                                                                                                        
1. download adguard.crx the file is given in the repository 

2. download chrome driver (important : note that the chrome driver version you download matches or is mostly similar to the version of the chrome you've installed on your mac or windows) just google chrome driver and you'll be able to download it.

3. copy main.py and make sure all packages are installed.


9. for windows script change the path in line 48 -- chrome_options.add_extension(r"paste your adguard.crx file path here")
10. for windows script change the path in line 55 -- service = Service(r"paste your chromedriver file path here")
11. for windows script change the path in line 100 -- os.chdir("paste your downloads folder path here") 

after following all these steps if it shows an error because of line 55 and 56(browser = webdriver.Chrome(service=service, options=chrome_options), then comment those lines and remove comment from line 52 and remember to put your chrome driver path(browser = webdriver.Chrome(r"paste chrome driver path here", options=chrome_options), that should resolve any issue.
