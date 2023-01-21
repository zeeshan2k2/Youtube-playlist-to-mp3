# Youtube-playlist-to-mp3.
this program will convert youtube playlist to mp3 and store it in a file. For now this code only works on mac os.


1. download adguard.crx the file is given in the repository (doesn't matter if your are using windows or mac os)

2. download chrome driver (important : note that the chrome driver version you download matches or is mostly similar to the version of the chrome you've installed on your mac or windows) just google chrome driver and you'll be able to download it.

3. copy main-for-windows.py or main-for-pac.py code depending on your os and make sure the packages are installed.


4. for mac os script change the path in line 33 -- chrome_options.add_extension("paste your adguard.crx file path here")
5. for mac os script change the path in line 38 -- browser = webdriver.Chrome("paste your chromedriver file path here", options=chrome_options)
6. for mac os script change the path in line 82 -- (os.chdir("paste your downloads folder path here") 



9. for windows script change the path in line 35 -- chrome_options.add_extension(r"paste your adguard.crx file path here")
10. for windows script change the path in line 42 -- service = Service(r"paste your chromedriver file path here")
11. for windows script change the path in line 86 -- os.chdir("paste your downloads folder path here") 
