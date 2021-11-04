#! /usr/bin/env python3
import os, sys, glob
import requests, json

#linux-instance-external-ip :: linexIP

linexIP=sys.argv[1]

url:"http://"+linexIP+"/fruits"
source=os.environ["HOME"]+"/supplier-data/descriptions/*"

#recorre directorio de las descripciones
#ejemplo
''' 
{
"name": "Watermelon", 
"weight": 500, 
"description": "Watermelon is good for relieving heat, eliminating annoyance and quenching thirst. It contains a lot of water, which is good for relieving the 
symptoms of acute fever immediately. The sugar and salt contained in watermelon can diuretic and eliminate kidney inflammation. Watermelon also contains substances that can lower blood pressure.",
 
"image_name": "010.jpeg"
} '''

traceKeys=['name', 'weight', 'description', 'image_name']
dataPost={}
errorCount=0

for descriptions in glob.iglob(source):
    with open(descriptions) as file:
      messaggio=file.read()
      for counter,keys in enumerate(traceKeys):
        dataPost[keys]=messaggio.split('/n')[counter]
      dataPost['weight']=int(dataPost[weight].strip("lbs"))
      dataPost['image_name']=file.filename.strip('.txt')+".jpeg"
      r=requests.post(url, json=dataPost)
      r.raise_for_status()
