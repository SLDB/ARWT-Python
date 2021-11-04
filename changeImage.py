!/usr/bin/env python3
import os, sys, glob
from PIL import Image

source=os.environ["HOME"]+"/supplier-data/images/*.tiff"

# recorre el directorio Image y modifica los archivos .tiff unicamente

for i in glob.iglob(source):
    try:
      with Image.open(i) as im:
        fileOut=im.filename.rsplit(".tiff")[0]+".jpeg"
        im.resize((600,400)).convert("RGB").save(fileOut, format="JPEG")
    except OSError:
      pass

