import requests

downloadUrl = "https://ve83.aadika.xyz/download/8aRCmMlCcY0/mp3/128/1673283102/4a6d36ab6ff40dfbd30d5bb0d76e7fa27ae30fc38a613dddf6529cfd9bc42163/1?f=yt5s.io"

req = requests.get(downloadUrl)
filename = req.url[downloadUrl.rfind("/")]


def download_file(url, filename=""):
    try:
        if filename:
            pass
        else:
            filename = requests.url[downloadUrl.rfind("/") + 1:]

        with requests.get(url) as req:
            with open(filename, "wb") as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None


download_file(downloadUrl, "goofy.mp3")
