# ARWT-Python
Week4 excercise on the Automating Real World Task with Python - Final PRoject


El objetivo de este repositorio es realizar partes y pruebas en máquina del
proyecto Automating Real World Task with Python, semana 4, que corresponde
al último proyecto del curso.
Este proyecto busca alcanzar tocar los siguientes temas:

Review module documentation! You are going to need to use these modules to complete the final project. Reading the documentation takes time, but as you become more familiar with the APIs provided by these modules, it could save you from writing a bunch of custom code that could have just been a call to a module function! Remember, we’ve covered these modules in previous lessons too, so feel free to go back and review them if you need a refresher!

[Python Image Library (PIL)](https://pillow.readthedocs.io/) - [Tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)

[Requests](https://requests.readthedocs.io/) (HTTP client library) - [Quickstart](https://requests.readthedocs.io/en/master/user/quickstart/)

[ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf) (PDF creation library)

[email](https://docs.python.org/3/library/email.examples.html) (constructing email)

[psutil](https://psutil.readthedocs.io/) (processes and system utilization)

[shutil](https://docs.python.org/3/library/shutil.html) (file operations)

[smtplib](https://docs.python.org/3/library/smtplib.html) (sending email)


-----------------------------
-

Introduction

You work for an online fruits store, and you need to develop a system that will update the catalog information with data provided by your suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

You will create a Python script that will process the images and descriptions and then update your company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs). 

Finally, in parallel to the automation running, we want to check the health of the system and send an email if something goes wrong. 
What you’ll do

   Write a script that summarizes and processes sales data into different categories 

   Generate a PDF using Python

   Automatically send a PDF by email 

   Write a script to check the health status of the system 
