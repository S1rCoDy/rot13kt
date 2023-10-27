import zipfile
import os

os.mkdir("papka")
dir = 'papka'
with zipfile.ZipFile('archive.tk') as zf:
    zf.extractall(dir)

"""file = zipfile.ZipFile("archive.tk", "w")
file.write("server-icon.png")
file.close()"""