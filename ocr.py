import easyocr
from PIL import Image
import io
import fitz 
import numpy as np


    
def read_text_from_pillow_image(image, language):
    # Initialize the EasyOCR reader for the specified language
    reader = easyocr.Reader([language])

    try:
        # Convert PIL Image to bytes
        img_bytes = io.BytesIO()
        image.save(img_bytes, format='PNG')
        img_bytes = img_bytes.getvalue()

        # Read text from the image
        result = reader.readtext(img_bytes)

        # Extract and return the text
        text = '\n'.join([item[1] for item in result])
        return text
    except Exception as e:
        return str(e)
    
def extract_text_from_scanned_pdf(pdf_path, language):
    # Initialize the EasyOCR reader for the English language
    reader = easyocr.Reader([language])

    try:
        text = ''
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)

        # Iterate through each page of the PDF
        for page_num in range(pdf_document.page_count):
            page = pdf_document[page_num]

            # Render the page as an image (Pillow image)
            pix = page.get_pixmap()
            img_bytes = pix.samples

            # Create a numpy array from the image bytes
            img_array = np.frombuffer(img_bytes, dtype=np.uint8).reshape(pix.height, pix.width, -1)

            # Extract text from the image using EasyOCR
            page_text = reader.readtext(img_array)

            # Concatenate the text from this page to the overall text
            text += ' '.join([item[1] for item in page_text]) + '\n'

        return text
    except Exception as e:
        return str(e)

# Example usage:
# img = Image.open('maithili.png')
# text = read_text_from_pillow_image(img, 'mai')
# print(text)



