import pytesseract
from PIL import Image


# Load the image
image_path = "images/nutrition.jpg"
image = Image.open(image_path)

# Preprocess the image
grayscale_image = image.convert("L")
threshold_value = 140  # 135 Adjust this value based on the image quality
binary_image = grayscale_image.point(
    lambda x: 0 if x < threshold_value else 255, '1')
resized_image = binary_image.resize((image.width * 2, image.height * 2))

# Perform OCR using PyTesseract
# Correctly specifying the Page Segmentation Mode (PSM) as an argument
text = pytesseract.image_to_string(resized_image, config='--psm 6')

print(text)
