import subprocess
import tempfile
import secrets
import os
from PIL import Image, ImageOps
from fastapi import FastAPI, UploadFile, Response
import uvicorn

app = FastAPI()

@app.post("/ocr")
async def tesseract(uploaded_image : UploadFile):
   
      # Temporarily store image in this path
      temp_image_path = f"./{secrets.token_hex(4)}.png"

      with tempfile.TemporaryFile() as f:
        
            f.write(await uploaded_image.read())
            
            # Apply grayscale to image
            image_to_normalize = Image.open(f)
            ImageOps.grayscale(image_to_normalize).save(temp_image_path)

      try:
            
            extracted_text = subprocess.run(["tesseract", temp_image_path, "stdout"], capture_output=True, text=True, check=True)
            return Response(extracted_text.stdout, media_type="text/plain")
     
      finally:
            os.remove(temp_image_path)

if __name__ == "__main__":
      uvicorn.run("server:app", host="0.0.0.0", port=8000)







