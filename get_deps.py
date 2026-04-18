import os
import urllib.request
from zipfile import ZipFile

python_zip = "https://www.python.org/ftp/python/3.12.9/python-3.12.9-embed-amd64.zip"

def main():
    print("Downloading python zip...")
    python_zip_filename = python_zip.split('/')[-1]
    urllib.request.urlretrieve(python_zip, python_zip_filename)
    print("...Complete. Removing python312._pth and sqlite3.dll...")
    with ZipFile(python_zip_filename, 'r') as zin:
        with ZipFile(python_zip_filename[:-4] + "-less-pth-sqlite.zip", 'w') as zout:
            for item in zin.infolist():
                if item.filename != "python312._pth" and item.filename != "sqlite3.dll":
                    buffer = zin.read(item.filename)
                    zout.writestr(item, buffer)
    os.remove(python_zip_filename)
    print("...Complete.")


if __name__ == "__main__":
    main()