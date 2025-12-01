
# Tiny OCR API with Tesseract OCR and Python FastAPI

An API that extracts text from an image using [Tesseract OCR](https://tesseract-ocr.github.io/) and Python [FastAPI](https://fastapi.tiangolo.com/).

Refer to this [guideline](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html) to improve the quality of the output. Grayscaling is the only normalization applied for this project.

---

## __Setup:__   

_You need to have Python and Tesseract OCR installed within your system._

Setup using the terminal inside the project directory:

```
# Create a venv
>> py -m venv pyEnv
>> pyEnv/Scripts/activate

# Install libraries
>> pip install -r requirements.txt

# Run the server 
>> py server.py

💡 The server will be at http://localhost:8000
```

---

## __Setup with Docker:__

You need to have docker installed within your system.

Setup using the terminal inside the project directory:

```
# Build the image 
>> docker build -t python/tesseract-ocr .

# Run a container
>> docker run -d -p 8000:8000 python/tesseract-ocr

💡 The server will be at http://localhost:8000
```

---

## __Testing:__

Test the API in your browser here:
```
http://localhost:8000/docs
```

The main API endpoint is here:
```
http://localhost:8000/ocr
```
Send a POST request with an attached FormData image file with the name "uploaded_image", the api will response with the extracted text as plain text.
