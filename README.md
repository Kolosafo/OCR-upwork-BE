# Ocr-Upwork-BE
Backend for the image extraction project


> ⦁	How It Works

> ⦁	How to run on your device


To be able to run this api in your local machine you must first install python3.10 as well as-- tesseract on macOS, Windows or Linux


## Quick Overview
* git clone this project
* on macOS run - "brew install tesseract"
* on windows download - [here](https://github.com/UB-Mannheim/tesseract/wiki)
* cd to the base project directory (ocr_backend)
* run and activate a virtual env - "python -m venv env " (creates a virtual environment)
* run - "pip install -r requirements.txt"
* run - "python manage.py runserver" (takes your server live and accessible to any frontend)
* run - "python manage.py test" (runs the tests and returns result)
* PLEASE SEE HOW TO RUN SECTION OF THIS DOCUMENTATION FOR DETAILED INFO ON RUNNING THIS API

## How It Works
* This project uses tesseract to extract texts from image files - Tesseract is an open source optical character recognition (OCR) platform. OCR extracts text from images and documents without a text layer and outputs the document into a new searchable text file, PDF, or most other popular formats.
On this project, the api takes an image file format as payload and then it uses python to open the image and pass it to the tesseract extraction module.
After the extraction is complete, it returns a json response containing an optional id and text for all the texts extracted from the image given.

* Note: Please keep in mind that tesseract like every other machine learning module out there is not 100% accurate. However, these modules do learn and become better with each extraction. tesseract is not an exception :)

* This API is further built to take an optional parameter of "id" which I mentioned above. We use this to identify an extraction. This is necessary for the frontend when a user wants to extract texts from multiple image files. On the other hand, when a user only wants to extract text from just one image then there's no need to pass an id as parameter.

* I also built this API to only run with an API key, this is a security measure implemented to protect the API from unauthorized entities.

* In the case of multiple file extractions, The frontend must call this API in a loop with a given ID for each for file, the API will return extractions with the ID of each image passed. This becomes relevant to frontend to know which extraction belongs with which image.

* Furthermore, this API was built on django on purpose to satisfy the possibility for the need of a backend in the future. Where we might want to be saving some images, extractions or user data to a database. However, there's no backend implementation at the point of this commit and the API's sole purpose is to extract text from images.
* This API is also built to handle minimal complexities to reduce load on server we're hosting to, As we spoke about, we need this to work as great as possible in a relatively small server (1gb ram). For this reason, I built this API to collect and return extractions from text. Other functionalities such as converting the extractions to pdf format etc can be done on the frontend.


## How To Run This On Your Computer
> Please follow these steps in order.
* The first step to run this API on your local machine to install tesseract on macOS using "brew install tesseract", [Windows](https://github.com/UB-Mannheim/tesseract/wiki), Linux using "apt-get install -y tesseract-ocr"
* Then clone this repo
* Once cloned, navigate to the project base directory and create a .env file
* inside the .env file, create an api key variable e.g  APP_AUTH_TOKEN="api key value". (make sure the api key variable is called "APP_AUTH_TOKEN")
* Open your terminal and make sure you're in the project base directory where you have your manage.py and requirements.txt files (ocr_backend)
* run - "python -m venv env " (to create a virtual environment)
* run-  "env\Scripts\activate"(activates the virtual end)
* run - "pip install -r requirements.txt"
* run - "python manage.py runserver" (takes your server live and accessible to any frontend)
* alternativerly run - "python manage.py test" (runs the tests and returns result)

**IF YOU FOLLOW THESE STEPS ACCORDINGLY AND STILL AREN'T ABLE TO RUN THIS SUCCESSFULLY PLEASE CONTACT ME.**


