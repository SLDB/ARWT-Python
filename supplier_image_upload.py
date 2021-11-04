#!/usr/bin/env python3
import requests
import os, glob

#upload similar to example_upload.py

url = "http://localhost/upload/"
source=os.environ["HOME"]+"/supplier-data/images/*.jpeg"

# recorre el directorio de imagenes filtardo por archivos tipo JPEG

for i in glob.iglob(source):
    with open(i, 'rb') as opened:
      r=requests.post(url, files={'file': opened})

