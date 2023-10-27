import zipfile
import os

try:
    myzip = zipfile.ZipFile("archive.tk", "w")

    for folder, subfolders, files in os.walk("E:\\Проги\\auslogics-disk-defrag-setup"):
        for file in files:
            myzip.write(
                os.path.join(folder, file),
                os.path.relpath(os.path.join(folder, file), "E:\\Проги\\auslogics-disk-defrag-setup"),
                compress_type=zipfile.ZIP_DEFLATED
            )
finally:
    myzip.close()


"""file = zipfile.ZipFile("archive.tk", "w")
file.write("server-icon.png")
file.close()"""